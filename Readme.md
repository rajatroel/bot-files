# 👑 SMM Kingdom Tasks Automation Bot (Android 11+) 

A fully automated, background task-completion engine built for @SmmKingdomTasksBot. This system automates Instagram Likes, Comments, account switching, and intelligent AI-powered vision captcha solving.

## 📱 Section 1: Compatibility & Device Requirements
Before purchasing, please ensure your device meets the following criteria:

*   **Supported OS:** Android 11 and above. 
*   **Architecture:** 32-bit and 64-bit devices are fully supported.
*   **Minimum Hardware:** 4GB RAM is recommended for stable background processing.
*   **Tested & Confirmed:** Devices running Android 11 to 16 with standard manufacturer UIs.
*   **Untested:** Non-standard custom Android ROMs.
*   **Known Incompatible:** Android 10 and below, or very low-end hardware configurations (these will experience system instability or background task killing).
*   **Display Limitation (600 dp):** The current version relies on fixed screen coordinates, which requires changing your device's "Smallest width" to 600 dp via developer settings. **Warning:** This will significantly reduce the size of your entire Android interface, making text and icons much smaller, which may be less comfortable for normal everyday phone use.
*   **Language Requirement:** The phone system language (or at least the specific app languages for Chrome and Instagram) must be set to English (United States or English UK). The language inside @SmmKingdomTasksBot on Telegram must also be set to English. *(Note: This is a temporary limitation of the MacroDroid setup and will be fully resolved in our future dedicated app).*

## ⚙️ Section 2: Prerequisites & System Settings
Before installing any files, configure your Android phone with these exact settings:

1.  **Instagram Accounts:** Log in to all your working VIP Instagram accounts inside the official Instagram app, and ensure they are added to @SmmKingdomTasksBot.
2.  **Required System Permissions:** You must manually grant the following permissions when prompted. Do not skip any, or the bot will fail:
    *   **Accessibility:** Required for MacroDroid to interact with the screen.
    *   **Display Over Other Apps:** Required for automation overlays.
    *   **Files & Storage / Media:** Required for ZArchiver and Termux to read and write your session files.
    *   **Camera:** Required for the Telegram QR scanner.
    *   **Battery Optimization (Unrestricted):** You must set Termux, MacroDroid, and Shizuku to "Unrestricted" or "No Restrictions" in your Android battery settings to prevent the system from killing them in the background.
3.  **App Pinning / Locking:** After completing the whole setup, lock both Termux and MacroDroid in your phone's Recent Apps (App Switcher) screen so Android's memory manager never kills them.

## 🔑 Section 3: Step 1 — Generate Telegram API ID & Hash
The bot connects directly to the Telegram network and binds your license to your unique Telegram credentials.

> **Crucial:** You must generate your API ID and Hash using the exact Telegram phone number you will be using to run the automation bot.

1. Open your browser and navigate to **[my.telegram.org](https://my.telegram.org)**.
2. Enter your Telegram phone number in international format (e.g., +1234567890 or +919876543210) and click **Next**.
3. Telegram will send a login confirmation code to your official Telegram app. Copy that code, paste it into the website, and click **Sign In**.
4. Click on **API development tools**.
5. Fill in the required fields: App title (e.g., `Runner`), Short name (e.g., `runner1`). URL and Platform fields can be left default/empty.
6. Click **Create application**.
7. Copy your **`api_id`** (numeric string) and **`api_hash`** (alphanumeric string) and save them securely in your Notes app.

## 📲 Section 4: Step 2 — Install Required Applications
Install these four tools onto your device:

1. **Termux:** Download & install the [Termux](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk) app.
2. **MacroDroid:** Download & install the [Macrodroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) app (Recommended: Purchase its pro license).
3. **ZArchiver:** Download & install the [Zarchiver](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) app. (After downloading Zarchiver, open it and allow permissions then close it simply).
4. **Shizuku:** Download & install the [Shizuku](https://github.com/rajatroel/bot-files/releases/download/v1.0/Shizuku.apk) app. Run it on your device using wireless debugging. (You can search for how to run it on YouTube, for your specific device).

## 💻 Section 5: Step 3 — Run Termux Installer & Configuration
1. Open **Termux**.
2. Paste the following command and press **Enter**: 
   ```bash
   curl -sSL https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh | bash
   ```
3. When the Android storage permission popup appears, tap **Allow** and return to Termux.
4. When prompted by the setup wizard, input your details line by line:
   * **API ID:** Paste your numeric API ID → Press **Enter**.
   * **API Hash:** Paste your alphanumeric API Hash → Press **Enter**.
   * **License Key:** Paste your license key (e.g., `SMMK-1D-XXXX-XXXX-XXXX`) → Press **Enter**.
   * **Instagram Usernames:** Paste each Instagram account display name one by one, pressing **Enter** after each name.
5. When all accounts have been entered, prepare your second phone as given in the next section.

## 📷 Section 6: Step 4 — One-Time Telegram QR Login
Prepare a **second phone** that has the official Telegram app logged into your target number.

1. **Prepare the Scanner:** On your second phone, open Telegram and navigate to **Settings → Devices → Link Desktop Device**. (If the camera shows a black screen, go to your Android Settings → Apps → Telegram → Permissions, and allow **Camera** access. Verify the camera is working in Telegram).
2. **Generate QR Code:** In Termux (on your main phone), Press **Enter** to start the script and generate the QR code.
3. **Open & Scan:** When prompted on your main screen, choose to open the file with **ZArchiver**. Immediately scan the QR code using your second phone.
4. **2FA Password:** If your Telegram account has Two-Step Verification enabled, Termux will prompt you for your password. Type it in and press **Enter**.
5. **Success:** Once authenticated, the temporary image file is deleted, and your session file remains permanently stored in your internal storage. You will see a new device logged in on your Telegram app.
6. **Safe Exit:** Press the back button on your main phone to exit the image. To securely close Termux, swipe it away from your Recent Apps menu, reopen Termux, pull down your Android notification panel, and tap **Exit**.

## ⚙️ Section 7: Step 5 — Complete the Initial Setup
1. Ensure the **Shizuku** app is installed and running on your device.
2. Download the Latest Macrodroid [Replica.mdr](https://github.com/rajatroel/bot-files/releases/download/v1.0/Replica.mdr) file to your phone's `Download` folder.
3. Open **MacroDroid** → tap the **Export/Import** tile on the home screen. Check the box for **Reset variables on import**. Tap **Storage** (under Import), select the downloaded `backup.mdr` file from your Download folder, and tap **Clear existing and import all**.
4. Change the minimum width/dpi of your device to **600** via developer settings in your settings app.
5. Follow the visual [Tutorial](https://t.me/+2QbpNDGSQc05YjQ1) video for any further MacroDroid adjustments.
6. Start the automation by toggling the MacroDroid switch. 

## 🛠 Section 8: Troubleshooting Common Issues
If you encounter problems during setup or daily operation, check these solutions before contacting support:

*   **Automation stops or MacroDroid closes:** Ensure both MacroDroid and Shizuku are set to "Unrestricted" in your Android Battery settings and are locked in the Recent Apps menu.
*   **Termux stops in the background:** Lock Termux in the Recent Apps menu and verify battery optimization is disabled for it.
*   **Instagram link does not open correctly:** Ensure your default browser or link-handling settings are correctly routing straight to the Instagram app.
*   **Captcha fails consistently:** Ensure your device resolution is strictly set to exactly 600 dp in Developer Options. If it is even slightly off, fixed coordinates will miss the target.
*   **Authentication/Login problems:** Ensure you used the exact API ID and Hash linked to the phone number on the device. Re-scan the QR code if the session expired.
*   **Permissions become disabled:** Android occasionally revokes Accessibility permissions for security if an app isn't actively opened. Re-enable them in Settings → Accessibility.
*   **Contacting Support:** If an issue persists, please contact support and include: 1) Your exact device model and Android version, 2) A clear screenshot or screen recording of the error, and 3) A screenshot of your Developer Options showing your screen is set to 600 dp.

## 💳 Section 9: License Package & Purchasing
All licenses are strictly bound to your hardware via security verification. Sharing your license key with another user is prohibited and will result in a permanent system ban and loss of access for your devices. Please keep your key private.

| Package | Validity | Price |
| :--- | :--- | :--- |
| **Pro (1 Device)** | 30 Days | **$10 USDT** |

**Accepted Crypto: USDT (TON Network)**
```bash
UQBk7Dto--IPECy0br6vPDN9YbIBu-T2xdYtqia3ob4DdOOP
```

Copy the address above and ensure you are strictly sending **USDT-TON**. Sending tokens from other networks (like TRC-20 or ERC-20) to this address will result in the permanent loss of your funds.

### How to Order Your License
Before sending any payment, please contact the [@Developer](https://t.me/iamrajatroel). Once confirmed by the developer, follow these steps:
1. Send the exact plan amount to the payment address above.
2. Take a clear screenshot of the completed transaction receipt.
3. Send the screenshot to **[@Developer](https://t.me/iamrajatroel)** on Telegram.
4. Your unique license key and its information will be delivered to your chat within 5 minutes.

### 🔑 How to Update Your License Key
If you need to apply a new license key or renew an expired one, you can update it quickly without reinstalling the bot.
1. Copy and paste the following command into Termux and press **Enter**: 
   ```bash
   curl -sL -o license.py https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py && python license.py && rm license.py
   ```
2. Paste your new license key when prompted and press **Enter**.
