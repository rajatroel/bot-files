import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import random
import json
import sys
import re
import io
import os
import time
import base64
import subprocess
import requests
from datetime import datetime, timedelta

import qrcode
from telethon import TelegramClient, events, errors
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.types import MessageEntityTextUrl

from aiohttp import web
from PIL import Image
import cv2
import numpy as np

# ADD THESE 3 LINES RIGHT HERE
DIAG_K1 = np.eye(4, dtype=np.uint8)
DIAG_K2 = np.fliplr(np.eye(4, dtype=np.uint8))
RECT_K = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# ==========================================
# STARTUP MENU
# ==========================================
print("\n========================================")
print(" 👑 SMM Kingdom Automation")
print("========================================")
print(" 1 - Start Automation Script")
print(" 2 - Exit to Terminal")
print("========================================\n")

while True:
    user_choice = input("Type 1 or 2 and press Enter: ").strip()
    if user_choice == '1':
        print("\nStarting...")
        break
    elif user_choice == '2':
        sys.exit(0)
    else:
        print("Invalid input. Please type 1 or 2.")

# ==========================================
TARGET_CHAT = "@SmmKingdomTasksBot"
AI_PROXY_URL = "https://captcha-solver.imrajatroel.workers.dev"
# ==========================================

# LOAD EXTERNAL CONFIGURATION
try:
    with open(os.path.expanduser('~/config.json'), 'r') as f:
        config = json.load(f)
        
    API_ID = int(config["api_id"])
    API_HASH = config["api_hash"]
    LICENSE_KEY = config.get("license_key", "NONE")
    accounts = config["accounts"]
    
except Exception as e:
    print(f"ERROR: config.json issue: {e}")
    sys.exit(1)
    
HWID = API_HASH

print(f"Authenticating License (HWID: {HWID})...")

try:
    verify_req = requests.post(AI_PROXY_URL, json={"license_key": LICENSE_KEY, "hwid": HWID, "action": "verify"}, timeout=10)
    if verify_req.status_code == 403:
        error_msg = verify_req.json().get("error", "Invalid or Expired License")
        print(f"\n❌ License Error: {error_msg}\n")
        sys.exit(0)
    print("✅ License Validated!")
except Exception as e:
    print(f"\n❌ Authentication server offline! ({e})\n")
    sys.exit(0)

current_account_index = 0
active_phone_account_index = None  # TRACKER: Knows which IG account is open on screen

ABSOLUTE_BLOCKS = ["replenished", "audit", "wasn't completed", "arena", "news", "thank you, we will check it", "new order in the system", "money was sent", "rename", "penalty was applied", "screenshots failed", "demand", "withdraw", "+1", "you've set account", "was not rewarded", "language :", "cancel notifications", "promo codes and news", "my cashcoins :", "please write to our manager"]
SOFT_BLOCKS = ["warnings"]

pending_task = None
pending_text = None
bot_replied_event = asyncio.Event()

client = TelegramClient('/sdcard/userbot', API_ID, API_HASH)

def open_qr_image(img_path):
    try:
        # 1. Try ZArchiver (Free version)
        res_free = subprocess.run(
            ["am", "start", "-a", "android.intent.action.VIEW", "-d", f"file://{img_path}", "-t", "image/png", "-p", "ru.zdevs.zarchiver"],
            capture_output=True, text=True
        )
        # Android's Activity Manager outputs "Error" if the package isn't installed
        if "Error" not in res_free.stderr and "Error" not in res_free.stdout:
            return

        # 2. Try ZArchiver (Pro version)
        res_pro = subprocess.run(
            ["am", "start", "-a", "android.intent.action.VIEW", "-d", f"file://{img_path}", "-t", "image/png", "-p", "ru.zdevs.zarchiver.pro"],
            capture_output=True, text=True
        )
        if "Error" not in res_pro.stderr and "Error" not in res_pro.stdout:
            return
            
    except Exception:
        pass
        
    # 3. Universal Failsafe (Default Gallery/Chooser) if ZArchiver is missing
    os.system(f"termux-open {img_path} > /dev/null 2>&1")


async def login_via_qr():
    await client.connect()

    if not await client.is_user_authorized():
        qr_login = await client.qr_login()

        while True:
            # 1. Generate clean QR Code image
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(qr_login.url)
            qr.make(fit=True)
            
            img_path = "/sdcard/login_qr.png"
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(img_path)

            # 2. POP OPEN IN ZARCHIVER (OR FALLBACK)
            open_qr_image(img_path)

            print("\n========================================")
            print("       QR CODE OPENED ON SCREEN         ")
            print("========================================")
            print("Scan the image showing on your screen with your other phone!")
            print("Waiting for scan (timeout 30s)...")

            try:
                # Wait for user to scan (30s timeout per QR token)
                await qr_login.wait(timeout=30)
                break  # Logged in successfully without 2FA
            except errors.SessionPasswordNeededError:
                # Account has 2FA enabled: prompt for password
                pwd = input("\n[!] 2FA Cloud Password detected. Enter your password: ")
                await client.sign_in(password=pwd)
                break
            except asyncio.TimeoutError:
                print("\n[!] QR code expired. Refreshing on screen...")
                await qr_login.recreate()

        # Clean up the image file after successful login
        if os.path.exists(img_path):
            os.remove(img_path)
            
        print("\n✅ Logged in successfully! Session saved inside Termux.")

# ==========================================
# MACRODROID WEBHOOK & INTENT SERVER
# ==========================================
macro_event = asyncio.Event()
macro_status = ""

async def handle_callback(request):
    global macro_status
    macro_status = request.query.get('status', '')
    macro_event.set()
    return web.Response(text="OK")

async def fire_intent(action, extras=None):
    macro_event.clear()
    cmd = ["broadcast", "-a", action]
    if extras:
        for key, val in extras.items():
            cmd.extend(["--es", key, str(val)])
            
    # Non-blocking async execution
    proc = await asyncio.create_subprocess_exec(
        "am", *cmd,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )
    await proc.wait()

async def wait_for_macro(timeout_seconds):
    try:
        await asyncio.wait_for(macro_event.wait(), timeout=timeout_seconds)
        return macro_status
    except asyncio.TimeoutError:
        return "timeout"

# ==========================================
# AI
# ==========================================
def process_image_in_ram(pil_img):
    try:
        img_array = np.array(pil_img.convert("RGB"))
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        
        _, base_img = cv2.threshold(gray, 15, 255, cv2.THRESH_BINARY)
        
        if np.sum(base_img == 0) < 50:
            _, base_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            if np.sum(base_img == 0) < 50:
                base_img = gray
                
        inverted = cv2.bitwise_not(base_img)
        healed = cv2.morphologyEx(inverted, cv2.MORPH_CLOSE, DIAG_K1)
        healed = cv2.morphologyEx(healed, cv2.MORPH_CLOSE, DIAG_K2)
        healed = cv2.morphologyEx(healed, cv2.MORPH_CLOSE, RECT_K)
        
        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(healed, connectivity=8)
        clean_foreground = np.zeros_like(healed)
        for i in range(1, num_labels):
            if stats[i, cv2.CC_STAT_AREA] >= 8:
                clean_foreground[labels == i] = 255
                
        final_img = cv2.bitwise_not(clean_foreground)
        _, buffer = cv2.imencode('.jpg', final_img)
        return base64.b64encode(buffer).decode('utf-8')
    except Exception:
        return None

def get_math_answer(target_emoji, b64_images):
    print("Solving captcha...")

    payload = {
        "license_key": LICENSE_KEY,
        "hwid": HWID,
        "action": "solve",
        "target_emoji": target_emoji,
        "images": b64_images
    }

    for attempt in range(1, 4):
        try:
            response = requests.post(AI_PROXY_URL, json=payload, timeout=30)
            
            if response.status_code == 403:
                print(f"\n❌ {response.json().get('error', 'License Error')}\n")
                os._exit(0)
                
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
            
        except Exception as e:
            print(f"Server error (Attempt {attempt}/3): {str(e)}")
            if attempt < 3:
                time.sleep(3) 
            else:
                return "ERROR"

# ==========================================
# TASKER
# ==========================================
async def kill_everything(reason):
    print(f"\n UNKNOWN ERROR: {reason}")
    os._exit(0)

async def smart_send(text_to_send):
    delay = random.uniform(5.0, 7.0)
    await asyncio.sleep(delay)
    
    for attempt in range(1, 3): 
        bot_replied_event.clear() 
        print(f"Clicking : {text_to_send} (Attempt {attempt}/2)")
        await client.send_message(TARGET_CHAT, text_to_send, parse_mode=None, link_preview=False)
        
        try:
            await asyncio.wait_for(bot_replied_event.wait(), timeout=60.0)
            return 
        except asyncio.TimeoutError:
            if attempt == 1:
                print("Bot didn't reply in 60s! Trying ONE more time...")
            else:
                print("Bot still didn't reply after 2nd attempt!")
                
    await kill_everything("Bot server stopped responding after 2 attempts.")

async def smart_send_photo():
    photo_path = "/sdcard/Latest.png"
    delay = random.uniform(3.0, 4.0)
    await asyncio.sleep(delay)
    
    if not os.path.exists(photo_path):
        print(f"ERROR: Screenshot not found at {photo_path}")
        return False

    for attempt in range(1, 3): 
        bot_replied_event.clear()
        print(f"Uploading screenshot... (Attempt {attempt}/2)")
        
        try:
            await client.send_file(TARGET_CHAT, photo_path)
            await asyncio.wait_for(bot_replied_event.wait(), timeout=60.0)
            print("Bot replied successfully after photo upload!")
            return True
        except asyncio.TimeoutError:
            if attempt == 1:
                print("Bot didn't reply to photo in 60s! Retrying...")
            else:
                print("Bot still didn't reply to photo after 2nd attempt!")
                return False
        except Exception as e:
            print(f"Network error uploading photo: {e}")
            if attempt == 1:
                print("Retrying in 3 seconds...")
                await asyncio.sleep(3.0)
            else:
                return False

async def do_switch_account(target_display_name):
    print(f"Switching to: {target_display_name}")
    await fire_intent("com.bot.SWITCH", {"Account": target_display_name})
    
    status = await wait_for_macro(180.0)
    if status == "switched":
        return True
    else:
        print("Account switching failed (Not found / Banned)")
        return False

async def do_like_task(link):
    print(f"Like task detected")
    await fire_intent("com.bot.LIKE", {"Link": link})
    
    status = await wait_for_macro(60.0)
    if status == "success":
        await smart_send("✅Completed")
    else:
        await smart_send("❌Skip")
    
async def do_comment_task(link, full_msg_text):
    print("Comment task detected")
    
    comment_text = ""
    if "Text to comment :" in full_msg_text:
        comment_text = full_msg_text.split("Text to comment :")[1].strip()
    else:
        comment_text = full_msg_text.strip()

    # === FILTER: Skip comments containing @ mentions ===
    if "@" in comment_text:
        print(f"Skipping comment with @ mention: {comment_text}")
        await smart_send("❌Skip")
        return
    # ====================================================
        
    print(f"Instructing MacroDroid to comment: {comment_text}")
    
    await fire_intent("com.bot.COMMENT", {
        "Link": link, 
        "Comment": comment_text
    })
    
    status = await wait_for_macro(90.0)
    if status == "success":
        photo_sent = await smart_send_photo()
        if not photo_sent:
            await smart_send("❌Skip")
    else:
        await smart_send("❌Skip")

# ==========================================
# ROUTER
# ==========================================
@client.on(events.NewMessage(chats=TARGET_CHAT, incoming=True))
async def handle_msg(event):
    message = event.message  # Map event back to your 'message' variable
    global pending_task, pending_text, current_account_index, active_phone_account_index
    
    # Use raw_text to strip Telethon's invisible markdown brackets
    text = message.raw_text or message.text or message.caption
    if not text: return
    text_lower = text.lower()
    
    if any(word in text_lower for word in ABSOLUTE_BLOCKS): return
    if "warnings" in text_lower and "profile's username" not in text_lower and "too many" not in text_lower: return

    if "verification failed" in text_lower:
        print("Verification Failed! Telling MacroDroid...")
        await fire_intent("com.bot.CAPTCHA_FAILED")
        os._exit(0)

    bot_replied_event.set()

    # ==========================================
    # CAPTCHA SOLVER
    # ==========================================
    if "security check" in text_lower:
        print("Captcha detected")
        
        emoji_match = re.search(r'(?i)link(.*?)👉', text, re.DOTALL)
        if not emoji_match: return
        target_emoji = emoji_match.group(1).strip()

        hidden_url = None
        entities = message.entities or message.caption_entities
        if entities:
            for ent in entities:
                if isinstance(ent, MessageEntityTextUrl):
                    hidden_url = ent.url
                    break
        if not hidden_url: return

        await fire_intent("com.bot.OPEN_CAPTCHA", {"Link": hidden_url})

        photo_messages = []
        time_threshold = message.date - timedelta(seconds=15)
        
        async for past_msg in client.iter_messages(TARGET_CHAT, limit=10):
            # Telethon dates are UTC, so we compare directly
            if past_msg.date < time_threshold: break
            if past_msg.photo:
                photo_messages.append(past_msg)
                if len(photo_messages) == 3: break
        
        if len(photo_messages) != 3: return
        
        # Telethon downloads directly to bytes in memory
        downloads = await asyncio.gather(*[client.download_media(msg, bytes) for msg in photo_messages])
        downloads.reverse()
        b64_images = [process_image_in_ram(Image.open(io.BytesIO(d))) for d in downloads]
        
        math_answer = await asyncio.to_thread(get_math_answer, target_emoji, b64_images)
        print(f"Captcha answer : {math_answer}")

        await fire_intent("com.bot.CAPTCHA", {"Answer": math_answer})
        return 
        
# ==========================================

    if "leave the comment" in text_lower:
        if pending_text:
            text = f"{text}\n\nText to comment : {pending_text}"
            pending_text = None
            text_lower = text.lower() 
        else:
            pending_task = text
            return
    elif pending_task:
        text = f"{pending_task}\n\nText to comment : {text}"
        pending_task = None
        text_lower = text.lower() 

    # Safely extract the link, ignoring any trailing brackets or parentheses
    match = re.search(r'(https?://[^\s\]\)\>]+)', text)
    extracted_link = match.group(1) if match else None

    if "choose social network" in text_lower:
        await smart_send("Instagram")
        
    elif any(phrase in text_lower for phrase in ["profile's username for tasks completing", "is on review", "please choose account from the list", "too many"]):
        account_info = accounts[current_account_index]
        current_account_index = (current_account_index + 1) % len(accounts)
        
        await smart_send(account_info["username"])
        
    elif "1.1 cashcoins" in text_lower:
        if extracted_link: 
            target_index = (current_account_index - 1) % len(accounts)
            
            if active_phone_account_index != target_index:
                success = await do_switch_account(accounts[target_index]["display_name"])
                if not success:
                    await smart_send("❌Skip")
                    return # Stop here, do not run the like task
                active_phone_account_index = target_index
                
            await do_like_task(extracted_link)
        else: 
            await smart_send("❌Skip")
            
    elif "6.0 cashcoins" in text_lower or ("leave the comment" in text_lower and extracted_link):
        target_index = (current_account_index - 1) % len(accounts)
        
        if active_phone_account_index != target_index:
            print(f"Switching to : {accounts[target_index]['display_name']}...")
            success = await do_switch_account(accounts[target_index]["display_name"])
            if not success:
                await smart_send("❌Skip")
                return # Stop here, do not run the comment task
            active_phone_account_index = target_index

        await do_comment_task(extracted_link, text)

    elif "2.5 cashcoins" in text_lower or "1.0 cashcoins" in text_lower:
        print("Follow task detected")
        await smart_send("❌Skip")
        
    elif "saved successfully" in text_lower:
        await smart_send("✅Completed")
        
    elif "no active tasks" in text_lower:
        print("No task detected")
        await smart_send("Instagram")
        
    elif "verification passed" in text_lower:
        print("Verification successful")
        await fire_intent("com.bot.CAPTCHA_SUCCESS")
        
        status = await wait_for_macro(60.0)
            
        await smart_send("✅Completed")
  
    else:
        if "cashcoins" not in text_lower and "verification" not in text_lower:
            pending_text = text

async def main():
    app_web = web.Application()
    app_web.router.add_get('/callback', handle_callback)
    runner = web.AppRunner(app_web)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8080)
    await site.start()

    print(" ")
    print("========================================")
    print("AUTOMATION STARTED")
    print("========================================")
    print(" ")

    # 1. Run QR / Session Authentication
    await login_via_qr()

    # 2. Clear previous chat history cleanly
    await asyncio.sleep(7)
    
    try:
        await client(DeleteHistoryRequest(peer=TARGET_CHAT, max_id=0, revoke=True))
    except Exception as e:
        print(f"Could not clear history: {e}")

    await asyncio.sleep(7)

    # 3. Start bot interaction
    print("")
    print("Bot restarted")
    await client.send_message(TARGET_CHAT, "/start", parse_mode=None, link_preview=False)

    delay = random.uniform(5.0, 7.0)
    await asyncio.sleep(delay)

    print("Clicking : 📝Tasks📝")
    await client.send_message(TARGET_CHAT, "📝Tasks📝", parse_mode=None, link_preview=False)

    # 4. Keep script running
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop.run_until_complete(main())
