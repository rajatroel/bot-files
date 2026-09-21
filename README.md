# 👑 SMM Kingdom Tasks Automation Bot

![Version](https://img.shields.io/badge/version-v1.0-blue?style=flat-square) ![Android](https://img.shields.io/badge/Android-11%2B-3DDC84?style=flat-square&logo=android&logoColor=white) [![Support](https://img.shields.io/badge/support-Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/iamrajatroel)

Completes Instagram **Like** and **Comment** tasks for **@SmmKingdomTasksBot**, switches between your Instagram accounts, and solves the bot's captcha for you with AI.

*Version v1.0 · Last updated 21 September 2026*

---

## ✅ Before You Buy

> [!IMPORTANT]
> Please read this section first. This version needs a few changes to your phone's settings, and not every phone is suitable.

| | Requirement |
| :--- | :--- |
| 📱 **Android** | **Android 11 or newer.** Tested on Android 11 to 16. Android 10 and below **does not work**. |
| 🧩 **Phone type** | 32-bit and 64-bit phones both work. Custom (non-standard) Android versions are untested. |
| 💾 **Memory** | **4 GB RAM recommended.** Very low-end phones are unstable and may close the app in the background. |
| 🔍 **Screen size** | Must be set to exactly **600 dp**. This makes **everything** on your phone smaller (text, icons, buttons). You can change it back later. |
| 🌐 **Language** | **English (US or UK)** in Chrome, Instagram and the @SmmKingdomTasksBot chat. |
| 📲 **Second phone** | Needed **once**, with Telegram, to scan a login QR code. |
| 🔑 **Telegram API ID + Hash** | You create your own. It's free and explained below. |
| 🌍 **Internet** | Needed at all times. Wi-Fi is needed to start Shizuku. |
| 🧰 **Apps** | MacroDroid, Termux, Shizuku and ZArchiver. |

Not sure your phone is suitable? **[Ask support](https://t.me/iamrajatroel) before you buy.**

---

## 💳 Buy Your License

| Package | Validity | Price |
| :--- | :--- | :--- |
| **Pro (1 Device)** | 30 days | **$10 USDT** |

1. **Message [@iamrajatroel](https://t.me/iamrajatroel) first** and wait for confirmation.
2. Send **$10 USDT** on the **TON network** to this address:

   ```text
   @@WALLET@@
   ```

3. Take a clear screenshot of the completed transaction.
4. Send the screenshot to [@iamrajatroel](https://t.me/iamrajatroel).
5. Your license key arrives in your chat within **5 minutes**.

> [!WARNING]
> Send **USDT on TON only**. Coins sent on other networks (TRC-20, ERC-20, etc.) are **lost permanently**.

Your key works on **one device**. Sharing it with another person is prohibited and leads to a **permanent ban**.

---

## 🛠 Setup Guide

Follow the steps **in order**.

### Step 1 — Prepare your phone

1. In the official Instagram app, log in to **all** the accounts you want to use.
2. Add those accounts to **@SmmKingdomTasksBot**, and set the bot's language to **English**.
3. Set **Chrome and Instagram to English (US or UK)**. The simplest way is to set your whole phone to English. On Android 13 and newer you can set just those two apps: *Settings → System → Languages & input → App languages*.

### Step 2 — Get your Telegram API ID and Hash

> [!IMPORTANT]
> Use the **same Telegram phone number** that will run the automation.

1. Go to **[my.telegram.org](https://my.telegram.org)** and log in with your phone number (international format, e.g. `+1234567890`).
2. Type the code that Telegram sends to your Telegram app.
3. Click **API development tools**.
4. Enter any **App title** (e.g. `Runner`) and **Short name** (e.g. `runner1`). Leave the other fields as they are.
5. Click **Create application**.
6. Save your **api_id** (numbers) and **api_hash** (letters and numbers) in a private note. Never share them.

Your license is linked to this API Hash. If you ever need to change it, contact support first.

### Step 3 — Install the apps

| App | Where to get it |
| :--- | :--- |
| **Termux** | [Download `termux.apk`](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk) |
| **Shizuku** | [Download `Shizuku.apk`](https://github.com/rajatroel/bot-files/releases/download/v1.0/Shizuku.apk) |
| **MacroDroid** | [Google Play](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) — the **Pro** version is recommended |
| **ZArchiver** | [Google Play](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) — open it once, allow its permissions, then close it |

> [!WARNING]
> Only use these links. Don't install these apps from other websites. Use a **fresh Termux install**, because the setup replaces Termux's files.

### Step 4 — Turn on Developer options

1. Open **Settings → About phone** and tap **Build number** 7 times.
   *(Samsung: About phone → Software information → Build number. Xiaomi: tap "OS version" or "MIUI version".)*
2. Open **Developer options** and switch on **Wireless debugging** and **USB debugging**.

### Step 5 — Start Shizuku

Shizuku is a helper app that must be running whenever you use the automation.

1. Connect to **Wi-Fi**.
2. Open **Shizuku** (allow notifications if asked) and tap **Pairing**. In Developer options, tap **Wireless debugging → Pair device with pairing code**.
3. Pull down your notifications, tap the Shizuku notification and type the 6-digit code. You only pair once.
4. Go back to Shizuku and tap **Start**. It should say **"Shizuku is running"**.

> [!IMPORTANT]
> If Shizuku isn't running, **don't continue**. After **every phone restart**, open Shizuku and tap **Start** again. If it won't start, switch Wireless debugging off and on, then tap **Start**.

### Step 6 — Allow permissions

Don't skip any of these, or the automation will fail.

| App | Set to |
| :--- | :--- |
| **MacroDroid** | **Accessibility: ON** · **Display over other apps: ON** · **Files & media: Allow** · **Battery: Unrestricted** |
| **Termux** | **Battery: Unrestricted** |
| **Shizuku** | **Battery: Unrestricted** |
| **ZArchiver** | **Files & media: Allow** |

*"Unrestricted" may be called "Don't optimize" or "No restrictions" on some phones.*

### Step 7 — Install the automation in Termux

1. Open **Termux**, paste this command and press **Enter**:

   ```bash
   curl -sSL https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh | bash
   ```

2. When Android asks for storage access, tap **Allow** and return to Termux.
3. Wait for the download to finish. Then type your details, pressing **Enter** after each:

   | When asked for | Type |
   | :--- | :--- |
   | **API ID** | Your API ID (numbers only) |
   | **API HASH** | Your API Hash |
   | **License Key** | Your license key, e.g. `SMMK-1D-XXXX-XXXX-XXXX` |
   | **Account 1, Account 2…** | Your **Instagram usernames**, one per line. Check the spelling carefully. |

4. When all accounts are entered, press **Enter** on an empty line. You'll see **`CONFIGURATION SAVED`**.

Made a mistake? Run the same command again and re-enter your details.

### Step 8 — Log in to Telegram (one time only)

You need your **second phone**, with Telegram logged in to the same number.

1. **Second phone:** open Telegram → **Settings → Devices → Link Desktop Device**.
2. **Main phone:** in Termux, press **Enter** to start. A QR code appears.
3. Open it with **ZArchiver** and **scan it straight away** with the second phone. A new QR code appears every 30 seconds.
4. If you use Two-Step Verification, type your password in Termux and press **Enter**.
5. When Termux says **`Logged in successfully!`**, press Back to close the image. Then close Termux: swipe it away from Recent Apps, reopen it, pull down the notification panel and tap **Exit**.

### Step 9 — Import the automation into MacroDroid

1. Download **[Replica.mdr](https://github.com/rajatroel/bot-files/releases/download/v1.0/Replica.mdr)** to your phone's **Download** folder.
2. Open **MacroDroid** and tap **Export/Import**.
3. Tick **Reset variables on import**, tap **Storage**, choose **Replica.mdr**, then tap **Clear existing and import all**.
4. Watch the **[video tutorial](https://t.me/+2QbpNDGSQc05YjQ1)** for the remaining MacroDroid adjustments.

> [!NOTE]
> "Clear existing" removes any macros you already had in MacroDroid. Back them up first if you use it for other things.

### Step 10 — Set the screen size to 600 dp

1. Open **Developer options → Smallest width** and **write down the current value** (or take a screenshot):

   My original value: `________ dp`

2. Change it to **600** and confirm.

> [!TIP]
> It must be **exactly 600**. If it's slightly off, taps land in the wrong place. To go back to normal later, enter your original value again.

### Step 11 — Final check

Tick every box before you start:

- [ ] Shizuku is running
- [ ] MacroDroid is imported and enabled
- [ ] Accessibility is ON
- [ ] Battery is **Unrestricted** for MacroDroid, Termux and Shizuku
- [ ] Screen is set to **600 dp**
- [ ] Chrome, Instagram and the bot are in **English**
- [ ] Your license and Instagram accounts are entered in Termux
- [ ] **Termux, MacroDroid and Shizuku are locked** in Recent Apps *(open Recent Apps and choose **Lock** on each — the way depends on your phone)*

---

## ▶️ Start the Automation

1. Make sure **Shizuku is running**.
2. Turn the **MacroDroid switch ON**.
3. In Termux you'll see messages like these:

   ```text
   License validated!
   AUTOMATION STARTED SUCCESSFULLY
   Bot restarted
   ```

As tasks arrive you'll see **`Like task detected`** or **`Comment task detected`**. **`No task detected`** just means the bot has nothing for you right now.

- Every start clears your chat with @SmmKingdomTasksBot. This is normal.
- Follow tasks, and comments that contain an `@`, are skipped.

---

## 📌 Daily Tips

- Keep **Termux, MacroDroid and Shizuku running** and locked in Recent Apps. Don't swipe them away.
- **Don't switch Instagram accounts yourself.** The automation remembers which account is open and would run tasks on the wrong one.
- The automation taps the screen for you, so **keep the screen on** and avoid using the phone while it works.
- **After a phone restart:** connect to Wi-Fi → start **Shizuku** → open **MacroDroid** and check it's ON → start the automation.
- It **stops by itself** after a license error, a failed captcha check, or if the bot stops responding. Fix the problem, then start it again.
- **To stop it:** switch MacroDroid OFF and close Termux (swipe it away → reopen → pull down notifications → **Exit**).

---

## 🔄 Renew Your License

When your 30 days end, Termux shows **`License Error`**. To renew:

1. Contact [@iamrajatroel](https://t.me/iamrajatroel) to renew and get your new key.
2. Run this in Termux:

   ```bash
   curl -sL -o license.py https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py && python license.py && rm license.py
   ```

3. Paste your new key and press **Enter**. You'll see **`License Key successfully updated!`**
4. Start the automation again. No reinstall needed.

---

## 🩺 Troubleshooting

| Problem | What to do |
| :--- | :--- |
| **Automation stops, or MacroDroid / Termux closes** | Set MacroDroid, Termux and Shizuku to **Unrestricted** battery, lock them in Recent Apps, and check that Shizuku is running. |
| **Shizuku isn't running** | Connect to Wi-Fi → switch Wireless debugging off and on → open Shizuku → tap **Start**. |
| **Accessibility switched itself off** | *Settings → Accessibility → MacroDroid* → **ON**. Android sometimes turns it off. |
| **Captcha fails, or Termux says `Verification Failed!`** | The automation stops after a failed check. Restart it and make sure the screen is exactly **600 dp** and the apps are in **English**. Still failing? Send support a screen recording. |
| **Instagram link won't open, or the wrong page opens** | Check **600 dp** and **English**, and make sure links open in the **Instagram app**, not the browser. |
| **QR camera is black** | On the **second phone**: *Settings → Apps → Telegram → Permissions → Camera → Allow*. |
| **Login or API error** | Use the API ID and Hash created for the **same phone number**. The API ID is **numbers only**. Scan the newest QR code. |
| **`License Error`** | Copy your key exactly as sent (no extra spaces) and update it as shown in *Renew Your License*. If it has expired, renew it. |
| **Running, but nothing happens** | Check Termux for `License validated!`. Then check the MacroDroid switch, Accessibility, Shizuku and 600 dp. `Account switching failed` means an Instagram username is spelled wrong. Some steps can take up to 3 minutes. |
| **After a phone restart** | Wi-Fi → start Shizuku → check MacroDroid is ON → start the automation. |
| **Problem started after an update** | Re-check 600 dp, English, Accessibility, battery settings and Shizuku. |

---

## 💬 Need Help?

Contact **[@iamrajatroel](https://t.me/iamrajatroel)** on Telegram and include:

- Your phone brand and model
- Your Android version
- A screenshot or screen recording of the problem
- The exact error message, and what happened just before it
- A screenshot of Developer options showing **600 dp**

> [!TIP]
> Hide your license key and API Hash in any screenshot you share publicly, and never send anyone your Telegram login codes.

---

## 🚀 Coming Later

A standalone app is planned. It aims to need less manual setup and to support more screen sizes and languages. It is **not** part of v1.0, so everything above describes the current version only.
