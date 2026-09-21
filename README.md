# 👑 SMM Kingdom Tasks Automation Bot - Official README

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

## 6. Required Applications

| Application | Requirement / Source |
|:------------|:---------------------|
| **MacroDroid** | Download and purchase its pro license. |
| **Termux** | Download and install it on your device. |
| **Shizuku** | Download, install and run it on your device. |
| **ZArchiver** | Download and open it once to grant necessary permissions.|
| **Instagram** | Official app required. |
| **Telegram** | Official app required. |

## 7. Required Android Settings & Permissions

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

## 10. Termux Setup

1. Ensure termux is installed on your device.
2. Open Termux, paste the following command and press Enter.

   ```bash
   curl -sSL https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh | bash
   ```

3. When the Android storage permission popup appears, tap **Allow** and return to Termux.
4. When prompted by the setup wizard, input your **API ID**, **API Hash**, **License Key**, and **Instagram Usernames** and press enter on empty line to save.

## 11. MacroDroid Installation

1. Ensure Macrodroid is installed and you have its pro license.
2. **Import automation Download:** `Replica.mdr` file.
3. **Open MacroDroid:** Tap the **Export/Import** tile.
4. Check the box for **"Reset variables on import"**.
5. Tap **Storage**, select the `Replica.mdr` file from your **Download** folder, and tap **"Clear existing and import all"**.
6. You will be asked to give few permission, just grant them.

## 12. Complete Installation Sequence

1. **Check compatibility:** Confirm Android version, architecture, RAM, required apps and current limitations.
2. **Prepare Android:** Log in to all your working VIP Instagram accounts inside the official Instagram app.
3. **Set 600 dp:** Configure the minimum width/dpi of your device.
4. **Install and configure Shizuku:** Verify it is running.
5. **Install and configure Termux:** Run the installation script.
6. **Install MacroDroid:** Import the current automation.
7. **Grant ALL required permissions:** You must manually grant permissions; do not skip any, or the bot will fail.
8. **Configure required language settings:** Set to English.
9. **Configure API ID / API Hash:** Generate from [my.telegram.org](https://my.telegram.org) and input during Termux setup.
10. **Enter license key:** Paste during the Termux wizard.
11. **Add Instagram accounts:** Enter during the Termux wizard.
12. **Complete Telegram authentication:** Use your second phone to scan the QR code generated in Termux.

### Final verification checklist

- [ ] Shizuku running
- [ ] Termux configured
- [ ] MacroDroid enabled
- [ ] Accessibility enabled
- [ ] Battery settings correct
- [ ] 600 dp configured
- [ ] Correct language configuration
- [ ] License active
- [ ] Instagram accounts connected
- [ ] Telegram authenticated
- [ ] Required apps locked in Recent Apps

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
