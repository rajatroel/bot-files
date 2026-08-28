# 👑 SMM Kingdom Tasks Automation Bot (Termux)

A fully automated, background task-completion engine built for **@SmmKingdomTasksBot**. This system automates Instagram Likes, Comments, account switching, and magical AI-powered vision captcha solving.

---

## ⚙️ Section 1: Prerequisites & Device Setup

Before installing any files, configure your Android phone with these required settings:

1. **System Language:** Set your Android phone language to **English (United States or English UK). The language inside `@SmmKingdomTasksBot` on Telegram must also be set to English.**
   * *App-specific alternative:* If you prefer to keep your phone in another language, go to **Settings → Apps** and set the individual language for **Chrome** and **Instagram** to **English**. The language inside `@SmmKingdomTasksBot` on Telegram must also be set to English.
2. **Instagram Accounts:** Log in to all your working VIP Instagram accounts inside the official **Instagram app**, and ensure they are added to `@SmmKingdomTasksBot`.
3. **App Pinning / Locking:** Lock both **Termux** and **MacroDroid** in your phone's Recent Apps (App Switcher) screen so Android's memory manager never kills them.
4. **Battery Optimization:** Turn off Battery Optimization / Power Saving for both **Termux** and **MacroDroid** in your phone settings.

---

## 🔑 Section 2: Step 1 — Generate Telegram API ID & Hash

The bot connects directly to the Telegram MTProto network and binds your license to your unique Telegram credentials.

> **Crucial:** You must generate your API ID and Hash using the **exact Telegram phone number** you will be using to run the automation bot.

1. Open your browser and navigate to **[my.telegram.org](https://my.telegram.org)**.
2. Enter your Telegram phone number in international format (e.g., `+1234567890` or `+919876543210`) and click **Next**.
3. Telegram will send a login confirmation code to your **official Telegram app**. Copy that code, paste it into the website, and click **Sign In**.
4. Click on **API development tools**.
5. Fill in the required fields:
   * **App title:** Enter any name (e.g., `SMMRunner`)
   * **Short name:** Enter any short word (e.g., `runner1`)
   * *URL and Platform fields can be left default/empty.*
6. Click **Create application**.
7. Copy your **`api_id`** (numeric string) and **`api_hash`** (alphanumeric string) and save them in your Notes app.

---

## 📲 Section 3: Step 2 — Install Required Applications

Install these three tools onto your device:

1. **Termux (Terminal Runner):** **[Download Termux APK](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk)**  
   *(Strictly use this download link; the version on Google Play Store is deprecated and will not work).*
2. **MacroDroid (Macro Automation):** **[Download MacroDroid from Play Store](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid)**.
3. **ZArchiver (Image Viewer for QR Login):** **[Download ZArchiver from Play Store](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver)**.

---

## 🛠️ Section 4: Step 3 — Import & Configure MacroDroid

1. **[Download the Latest Macro File (`backup.mdr`)](https://github.com/rajatroel/bot-files/releases/download/v1.0/backup.mdr)** to your phone's `Download` folder.
2. Open **MacroDroid** → tap the **Export/Import** tile on the home screen.
3. Check the box for **Reset variables on import**.
4. Tap **Storage** (under Import), select the downloaded `backup.mdr` file from your `Download` folder, and tap **Clear existing and import all**.
5. Grant all 4 required system permissions:
   * *Accessibility Service*
   * *Write System Settings*
   * *Draw Over Other Apps (Overlay)*
   * *Usage Access*
6. Toggle the main MacroDroid switch in the top-right corner **OFF**, wait 2 seconds, and toggle it back **ON**. Grant any remaining permission popups.

---
## 💻 Section 5: Step 4 — Run Termux Installer & Configuration

1. Open **Termux**.
2. Paste the following command and press **Enter**:

```bash
bash <(curl -sL [https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh](https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh))
```

3. When the Android storage permission popup appears, tap **Allow** and return to Termux.
4. When prompted by the setup wizard, input your details line by line:
   * **API ID:** Paste your numeric API ID → Press **Enter**.
   * **API Hash:** Paste your alphanumeric API Hash → Press **Enter**.
   * **License Key:** Paste your license key (e.g., `SMMK-1D-XXXX-XXXX-XXXX`) → Press **Enter**.
   * **Instagram Usernames:** Paste each Instagram account display name one by one, pressing **Enter** after each name.
5. When all accounts have been entered, press **Enter on an empty line** to save your configuration.

---

## 📷 Section 6: Step 5 — One-Time Telegram QR Login

Your session is automatically saved to `/sdcard/userbot.session` so you will only ever need to link your Telegram account once.

```text
========================================
       QR CODE OPENED ON SCREEN         
========================================
Scan the image showing on your screen with your other phone!
Waiting for scan (timeout 30s)...
```

1. The script will generate a QR code and open it directly on your screen via ZArchiver or your image viewer.
2. **How to Scan the Code:**
   * **Using a Second Phone:** Open Telegram on your second device → **Settings → Devices → Link Desktop Device** → Scan the QR code displaying on your primary phone.
   * **Using One Phone:** Take a quick screenshot of the QR code → Send the image to another screen or friend → Open Telegram on your phone → **Settings → Devices → Link Desktop Device** → Scan the screenshot.
3. **2FA Cloud Password:** If you have Two-Step Verification enabled, Termux will prompt:
   ```text
   [!] 2FA Cloud Password detected. Enter your password:
   ```
   Type your Telegram password into Termux and press **Enter**.
4. Once authenticated, the temporary image file is deleted, and your session file remains permanently stored.

---

## ⚡ Section 7: Step 6 — Live Operation, Stopping & Restarting

### Live Execution
* Termux will output:
  ```text
  Bot restarted
  Clicking : 📝Tasks📝
  ```
* The bot will automatically delete previous chat history, start the tasks flow, switch accounts, and resolve vision captchas via AI. **Do not touch your screen while tasks are executing.**

### How to Stop the Bot
1. Pull down your Android notification shade.
2. Tap **Exit** on the persistent Termux notification.
3. Open **MacroDroid** and toggle the top-right switch to **OFF**.

### How to Restart the Bot
* Open **MacroDroid** and toggle the main switch to **ON**. MacroDroid will automatically start Termux, restore your saved session, and begin tasks immediately.

---

## 💳 Section 8: License Packages & Purchasing

All licenses include 24/7 automated vision captcha solving, auto-account switching, and macro updates.

| Package | Devices Allowed | Validity | Price | Key Features |
| :--- | :--- | :--- | :--- | :--- |
| **Single Runner** | 1 Phone / HWID | 90 Days | **$25 USDT** | Auto-Likes, Comments, AI Captcha Solver |
| **Farm Master** | 4 Phones / HWIDs | 90 Days | **$50 USDT** | Multi-Device Sync, Farming Speed |

### Accepted Payment Methods

* **USDT (TON Network):** `YOUR_TON_WALLET_ADDRESS` *(Fastest, sub-second confirmation)*
* **Native TON Coin:** `YOUR_TON_WALLET_ADDRESS`
* **Binance Pay ID:** `YOUR_BINANCE_PAY_ID`
* **USDT (TRC-20 Network):** `YOUR_TRC20_WALLET_ADDRESS`

*(Self-custody TON wallet transactions do not require a MEMO or Tag).*

---

### How to Order Your License

1. Send the exact plan amount to one of the payment addresses above.
2. Take a screenshot of the completed transaction receipt.
3. Send the screenshot and your selected plan to **[@iamrajatroel](https://t.me/iamrajatroel)** on Telegram.
4. Your unique license key and setup files will be delivered to your chat within 15 minutes.
   
