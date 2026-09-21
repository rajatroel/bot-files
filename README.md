# 👑 SMM Kingdom Tasks Automation Bot

A fully automated, background task-completion engine built for @SmmKingdomTasksBot. This system automates Instagram Likes, Comments, account switching, and intelligent AI-powered vision captcha solving.


[![Version](https://img.shields.io/badge/version-v1.0-blue?style=flat-square)](#18-updates--changelog)
[![Android](https://img.shields.io/badge/Android-11%20to%2016-3DDC84?style=flat-square&logo=android&logoColor=white)](#2-compatibility-requirements)
[![Setup](https://img.shields.io/badge/setup-MacroDroid-orange?style=flat-square)](#11-macrodroid-installation)
[![Support](https://img.shields.io/badge/support-%40iamrajatroel-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/iamrajatroel)

## 1. Current Version Information

| Item | Details |
|:-----|:--------|
| **Current version** | v1.0 |
| **Setup type** | MacroDroid based |
| **Documentation last updated** | September 21, 2026 |
| **License price** | $10 per month |
| **Support contact** | [@iamrajatroel](https://t.me/iamrajatroel) |

## 2. Compatibility Requirements

| Android Version | Status |
|:----------------|:-------|
| **Android 10** | ❌ Unsupported |
| **Android 11** | ✅ Supported |
| **Android 12** | ✅ Supported |
| **Android 13** | ✅ Supported |
| **Android 14** | ✅ Supported |
| **Android 15** | ✅ Supported |
| **Android 16** | ✅ Supported |

## 4. Hardware Requirements

| Category | Details |
|:---------|:--------|
| **RAM** | 4GB Minimum Recommended. |
| **Storage** | 4GB Minimum Recommended. |

**Known incompatible configurations**
Very low-end hardware configurations (these will experience system instability or background task killing).

## 5. Important - Current MacroDroid Version Limitations

> [!WARNING]
> The current version requires Android system changes. The changes described here apply to the **CURRENT** MacroDroid version.

### Language requirements

| Application | Language Requirement |
|:------------|:---------------------|
| **Android system** | English (United States or English UK). |
| **Instagram** | English (United States or English UK) required. |
| **Chrome** | English (United States or English UK) required. |
| **Telegram / Telegram bot** | English required. |
| **MacroDroid** | English required. |

### Minimum width - 600 dp

- The current MacroDroid automation uses fixed screen coordinates. Changing this setting affects the scale of the **ENTIRE** Android interface. Text, icons, buttons and other interface elements may become significantly smaller, which may be less comfortable for normal everyday phone use.


## 8. Developer Options Setup

1. Enable Developer Options/settings.
2. Open **Developer Options/settings**.
3. **Smallest width / Minimum width:** Set to `600 dp`.
4. **USB debugging:** Set to `ON`.
5. **Wireless debugging:** Set to `ON`.
6. (If available) **Disable permission monitoring:** Set to `ON`.
7. (If available) **Disable child process restrictions:** Set to `ON`.
8. (If available) **USB security settings:** Set to `ON`.

## 9. Shizuku Setup

1. **Installation:** Install the Shizuku application.
2. **Start Shizuku:** Run it on your device using wireless debugging. You can search for how to do it on youtube, for your specific device.
3. **Verify Shizuku:** Ensure Shizuku is running properly on your device.

> [!IMPORTANT]
> If Shizuku is not running, do **NOT** continue.

> [!NOTE]
> **After phone reboot:** Shizuku needs to be started again via Wireless Debugging.

## 10. Generate Telegram API ID & Hash
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


## 7. Required Android Settings &
Permissions

| Application | Setting | Required State |
|:------------|:--------|:---------------|
| **MacroDroid** | Accessibility | Must be ON |
| **MacroDroid** | attery optimization | Must be Unrestricted / No Restrictions |
| **MacroDroid** | Display over other apps | Must be ON |
| **Termux** | Battery optimization | Must be Unrestricted / No Restrictions |
| **Termux** | Files & Storage / Media | Must be ON |
| **Shizuku** | Battery optimization | Must be Unrestricted / No Restrictions |
| **Shizuku** | Wireless debugging | Must be ON |
| **ZArchiver** | Files & Storage / Media | Must be ON |
| **Telegram on other device** | Camera access | Must be ON (required for the Telegram QR scanner) |

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

## 13. First Run

- **Start the automation:** Toggle the MacroDroid switch.
- **How do I know it is working?** The bot will automate Instagram Likes, Comments, account switching, and captcha solving in the background.

### First-run test

- [ ] Instagram opens correctly
- [ ] Correct account is used
- [ ] Link opens correctly
- [ ] Automation performs expected action
- [ ] Telegram communication works
- [ ] No permission errors appear

## 14. Daily Use

| Topic | Details |
|:------|:--------|
| **Start automation** | Toggle the MacroDroid switch. |
| **Can I lock the screen?** | No, the screen must remain active for UI interactions. |
| **Can I use the phone while automation is running?** | Manual interference will disrupt the automation coordinates. |
| **Must Termux stay open?** | Yes, lock it in your phone's Recent Apps screen so Android's memory manager never kills it. |
| **Must MacroDroid stay open?** | Yes, lock it in your phone's Recent Apps screen. |
| **Must Shizuku remain running?** | Yes. |

## 15. Troubleshooting

| Problem | Solution |
|:--------|:---------|
| **MacroDroid stops working** | Ensure both MacroDroid and Shizuku are set to "Unrestricted" in your Android Battery settings and are locked in the Recent Apps menu. |
| **Termux stops / closes in background** | Lock Termux in the Recent Apps menu and verify battery optimization is disabled for it. |
| **Accessibility permission turns off** | Android occasionally revokes Accessibility permissions for security if an app isn't actively opened; re-enable them in Settings → Accessibility. |
| **Instagram link cannot be opened** | Ensure your default browser or link-handling settings are correctly routing straight to the Instagram app. |
| **Captcha fails** | Ensure your device resolution is strictly set to exactly `600 dp` in Developer Options. If it is even slightly off, fixed coordinates will miss the target. |
| **Telegram authentication fails** | Ensure you used the exact API ID and Hash linked to the phone number on the device. |
| **QR camera is black** | Go to your Android Settings → Apps → Telegram → Permissions, and allow Camera access. |

## 16. Contacting Technical Support

**Before contacting support, prepare:**

- Phone manufacturer and exact model
- Android version
- RAM
- Screenshot or screen recording of the problem
- Exact error message
- What happened immediately before the error
- Whether the problem happens every time or occasionally

> [!TIP]
> Include a screenshot of your Developer Options showing your screen is set to 600 dp.

- **Support contact:** Contact [@iamrajatroel](https://t.me/iamrajatroel) on Telegram.
- Technical support is handled directly by the developer.

## 17. License & Purchase

- **Price:** $10 USDT / device / 30 days
- **Before purchasing:** Confirm that the device meets the [compatibility requirements](#2-compatibility-requirements) above.
- **Purchase:** Send the exact plan amount to the USDT (TON Network) address `UQBk7Dto--IPECy0br6vPDN9YbIBu-T2xdYtqia3ob4DdOOP`, take a clear screenshot of the completed transaction receipt, and send it to [@iamrajatroel](https://t.me/iamrajatroel).
- **Activation:** Your unique license key and its information will be delivered to your chat within few minutes.
- **Renewal:** Paste the following command in Termux, press Enter, and paste your new license key when prompted.

  ```bash
  curl -sL -o license.py https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py && python license.py && rm license.py
  ```

## 18. Updates & Changelog

- **Current version:** v1.0
- **Release date:** September 21, 2026
- **Added:** Initial release of the fully automated, background task-completion engine with intelligent AI-powered vision captcha solving.

## 19. Known Issues

> [!NOTE]
> No confirmed known issues beyond the documented 600 dp resolution requirement and the Android 10 and below incompatibility at this time.

## 20. Before You Buy - Final Checklist

- [ ] My Android version is supported.
- [ ] My device architecture is supported.
- [ ] My device meets the hardware requirements.
- [ ] I understand the current 600 dp requirement.
- [ ] I understand the current language requirements.
- [ ] I understand that MacroDroid, Termux and Shizuku are required for the current version.
- [ ] I understand the required permissions/system changes.
- [ ] I have read the known limitations.
- [ ] I know how to contact technical support.

## 21. Future Dedicated App

- A standalone application is planned/developed separately from the current MacroDroid version.
- The goal is to reduce manual configuration, improve screen/DPI adaptability and provide broader language support.
