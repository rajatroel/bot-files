import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

from pyrogram.raw.functions.messages import DeleteHistory

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

from aiohttp import web
from pyrogram import Client, filters, idle
from pyrogram.enums import ParseMode, MessageEntityType
from PIL import Image
import cv2
import numpy as np

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
    
try:
    verify_req = requests.post(AI_PROXY_URL, json={"license_key": LICENSE_KEY, "action": "verify"}, timeout=10)
    if verify_req.status_code == 403:
        print("\nTrial Expired! Contact developer to upgrade.\n")
        sys.exit(0)
except Exception:
    print("Unknown error! Please restart the automation.")
    sys.exit(0)

current_account_index = 0
active_phone_account_index = None  # TRACKER: Knows which IG account is open on screen

ABSOLUTE_BLOCKS = ["replenished", "audit", "wasn't completed", "arena", "news", "thank you, we will check it", "new order in the system", "money was sent", "rename", "penalty was applied", "screenshots failed", "demand", "withdraw", "+1", "you've set account", "was not rewarded", "language :", "cancel notifications", "promo codes and news", "my cashcoins :", "please write to our manager"]
SOFT_BLOCKS = ["warnings"]

pending_task = None
pending_text = None
bot_replied_event = asyncio.Event()

app = Client(os.path.expanduser('~/userbot'), api_id=API_ID, api_hash=API_HASH)

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
    img_array = np.array(pil_img)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    _, clean_img = cv2.threshold(gray_img, 15, 255, cv2.THRESH_BINARY)
    _, buffer = cv2.imencode('.jpg', clean_img)
    return base64.b64encode(buffer).decode('utf-8')

def get_math_answer(target_emoji, b64_images):
    print("Solving captcha...")

    payload = {
        "license_key": LICENSE_KEY,
        "action": "solve",
        "target_emoji": target_emoji,
        "images": b64_images
    }

    for attempt in range(1, 4):
        try:
            response = requests.post(AI_PROXY_URL, json=payload, timeout=30)
            
            if response.status_code == 403:
                print("\nTrial Expired! Contact developer to upgrade.\n")
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
        await app.send_message(TARGET_CHAT, text_to_send, parse_mode=ParseMode.DISABLED)
        
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
            await app.send_photo(TARGET_CHAT, photo=photo_path)
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
@app.on_message(filters.chat(TARGET_CHAT) & filters.incoming)
async def handle_msg(client_app, message):
    global pending_task, pending_text, current_account_index, active_phone_account_index
    
    text = message.text or message.caption
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
                if ent.type == MessageEntityType.TEXT_LINK:
                    hidden_url = ent.url
                    break
        if not hidden_url: return

        await fire_intent("com.bot.OPEN_CAPTCHA", {"Link": hidden_url})

        photo_messages = []
        time_threshold = message.date - timedelta(seconds=15)
        
        async for past_msg in app.get_chat_history(TARGET_CHAT, limit=10):
            if past_msg.date < time_threshold: break
            if past_msg.photo:
                photo_messages.append(past_msg)
                if len(photo_messages) == 3: break
        
        if len(photo_messages) != 3: return
        
        downloads = await asyncio.gather(*[app.download_media(msg, in_memory=True) for msg in photo_messages])
        downloads.reverse()
        b64_images = [process_image_in_ram(Image.open(io.BytesIO(d.getvalue()))) for d in downloads]
        
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

    extracted_link = re.search(r'(https?://[^\s]+)', text).group(1) if re.search(r'(https?://[^\s]+)', text) else None

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
    await app.start()
    
    try:
        peer = await app.resolve_peer(TARGET_CHAT)
        await app.invoke(DeleteHistory(peer=peer, max_id=0, revoke=True))
    except Exception as e:
        print(f"Could not clear history: {e}")
    
    await asyncio.sleep(7)
    
    print("Bot restarted")
    await app.send_message(TARGET_CHAT, "/start", parse_mode=ParseMode.DISABLED)
    
    delay = random.uniform(5.0, 7.0)
    await asyncio.sleep(delay)
    
    print("Clicking : 📝Tasks📝")
    await app.send_message(TARGET_CHAT, "📝Tasks📝", parse_mode=ParseMode.DISABLED)
    
    await idle()
    await app.stop()

if __name__ == "__main__":
    loop.run_until_complete(main())
