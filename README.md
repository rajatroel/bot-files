# 👑 SMM Kingdom Tasks Automation Bot (Termux)

A fully automated, background task-completion engine built for **@SmmKingdomTasksBot**. This system automates Instagram Likes, Comments, account switching, and intelligent AI-powered vision captcha solving.

---

## ⚙️ Section 1: Prerequisites & Device Setup

Before installing any files, configure your Android phone with these required settings:

1. **System Language:** Set your Android phone language to **English (United States or English UK)**. 
   * *App-specific alternative:* If you prefer to keep your phone in another language, go to **Settings → Apps** and manually set the individual language for **Chrome** and **Instagram** to **English**. 
   * **Note:** The language inside `@SmmKingdomTasksBot` on Telegram must also be set to English.
2. **Instagram Accounts:** Log in to all your working VIP Instagram accounts inside the official **Instagram app**, and ensure they are added to `@SmmKingdomTasksBot`.
3. **App Pinning / Locking:** Lock both **Termux** and **MacroDroid** in your phone's Recent Apps (App Switcher) screen so Android's memory manager never kills them after completing the initial setup.
   
---

## 🔑 Section 2: Step 1 — Generate Telegram API ID & Hash

The bot connects directly to the Telegram network and binds your license to your unique Telegram credentials.

> **Crucial:** You must generate your API ID and Hash using the **exact Telegram phone number** you will be using to run the automation bot.

1. Open your browser and navigate to **[my.telegram.org](https://my.telegram.org)**.
2. Enter your Telegram phone number in international format (e.g., `+1234567890` or `+919876543210`) and click **Next**.
3. Telegram will send a login confirmation code to your **official Telegram app**. Copy that code, paste it into the website, and click **Sign In**.
4. Click on **API development tools**.
5. Fill in the required fields:
   * **App title:** Enter any name (e.g., `Runner`)
   * **Short name:** Enter any short word (e.g., `runner1`)
   * *URL and Platform fields can be left default/empty.*
6. Click **Create application**.
7. Copy your **`api_id`** (numeric string) and **`api_hash`** (alphanumeric string) and save them securely in your Notes app.

---

## 📲 Section 3: Step 2 — Install Required Applications

Install these three tools onto your device:

1. **Termux (Terminal Runner):** **[Download Termux APK](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk)**  
   *(Strictly use this download link; the version on the Google Play Store is deprecated and will not work).*
2. **MacroDroid (Macro Automation):** **[Download MacroDroid from Play Store](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid)**.
3. **ZArchiver (Image Viewer for QR Login):** **[Download ZArchiver from Play Store](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver)**.

---

## 💻 Section 4: Step 3 — Run Termux Installer & Configuration

1. Open **Termux**.
2. Paste the following command and press **Enter**:

```bash
bash <(curl -sL [https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh)
```

3. When the Android storage permission popup appears, tap **Allow** and return to Termux.
4. When prompted by the setup wizard, input your details line by line:
   * **API ID:** Paste your numeric API ID → Press **Enter**.
   * **API Hash:** Paste your alphanumeric API Hash → Press **Enter**.
   * **License Key:** Paste your license key (e.g., `SMMK-1D-XXXX-XXXX-XXXX`) → Press **Enter**.
   * **Instagram Usernames:** Paste each Instagram account display name one by one, pressing **Enter** after each name.
5. When all accounts have been entered, press **Enter on an empty line** to save your configuration.

---

## 📷 Section 5: Step 4 — One-Time Telegram QR Login

Before starting the automation, prepare a **second phone** that has the official Telegram app logged into your target number.

1. **Prepare the Scanner:** On your second phone, open Telegram and navigate to **Settings → Devices → Link Desktop Device**. 
   * *Troubleshooting:* If the camera shows a black screen, go to your Android Settings → Apps → Telegram → Permissions, and allow **Camera** access. Verify the camera is working in Telegram.
2. **Generate QR Code:** In Termux (on your main phone), type `1` and hit **Enter** to start the script and generate the QR code.
3. **Open & Scan:** When prompted on your main screen, choose to open the file with **ZArchiver**. Immediately scan the QR code using your second phone.
4. **2FA Password:** If your Telegram account has Two-Step Verification enabled, Termux will prompt you for your password. Type it in and press **Enter**.
5. **Success:** Once authenticated, the temporary image file is deleted, and your session file remains permanently stored in your internal storage. You will see a new device logged in on your Telegram app.
6. **Safe Exit:** Press the back button on your main phone to exit the image. To securely close Termux, swipe it away from your Recent Apps menu, reopen Termux, pull down your Android notification panel, and tap **Exit**.

---

## 🛠️ Section 6: Step 5 — Import & Configure MacroDroid

1. **[Download the Latest Macro File (`backup.mdr`)](https://github.com/rajatroel/bot-files/releases/download/v1.0/backup.mdr)** to your phone's `Download` folder.
2. Open **MacroDroid** → tap the **Export/Import** tile on the home screen.
3. Check the box for **Reset variables on import**.
4. Tap **Storage** (under Import), select the downloaded `backup.mdr` file from your `Download` folder, and tap **Clear existing and import all**.
5. Grant all 4 required system permissions prompted on the screen (Accessibility, Display Over Other Apps, Write Settings, Usage Access).
6. Toggle the main MacroDroid switch in the top-right corner **OFF**, wait 2 seconds, and toggle it back **ON**. Grant any remaining permission popups.
   
---

## 💳 Section 7: License Packages & Purchasing

All licenses are strictly bound to your hardware via security verification. Sharing your license key with another user is prohibited and will result in a permanent system ban and loss of access for your devices. Please keep your key private.

| Package | Validity | Price |
| :--- | :--- | :--- |
| **Standard (1 Device)** | 90 Days | **$25 USDT** |
| **Premium (4 Devices)** | 90 Days | **$50 USDT** |

### Accepted Crypto
**USDT (TON Network)** OR **Native TON (GRAM)**

`UQCa9g8JwGSZWbgd2qfBGhG-92CAhV1k_cwkePfcOAJTsFJE`

Copy the address above and ensure you are strictly sending **USDT-TON** or **TON (GRAM)**. Sending tokens from other networks (like TRC-20 or ERC-20) to this address will result in the permanent loss of your funds. 

### How to Order Your License

**Before sending any payment, please contact the [@Developer](https://t.me/iamrajatroel). Once confirmed by the developer, follow these steps:**
   
1. Send the exact plan amount to the payment address above.
2. Take a clear screenshot of the completed transaction receipt.
3. Send the screenshot to **[@Developer](https://t.me/iamrajatroel)** on Telegram.
4. Your unique license key and setup files will be delivered to your chat within 5 minutes.
   
