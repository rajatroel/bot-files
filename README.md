Here is the complete README.md file split into 4 separate, clean code blocks. You can copy and paste them one by one in order into your file, and it will perfectly combine into the full document.
Part 1: Introduction to Required Applications
# 👑 SMM Kingdom Tasks Automation Bot - Official README
**Compatibility • Installation • Daily Use • Troubleshooting • Support**

**IMPORTANT:** Please read the Compatibility Requirements and Current Version Limitations BEFORE purchasing a license. Do not purchase until the device has been checked against the verified requirements below.

---

## 1. Current Version Information

| Field | Information |
| :--- | :--- |
| **Product version** | v1.0 |
| **Setup type** | MacroDroid-based automation |
| **Documentation last updated** | September 21, 2026 |
| **Current license price** | $10 USDT / device / 30 days |
| **Developer / Support contact** | @iamrajatroel on Telegram |

---

## 2. Compatibility Requirements

| Android version | Status |
| :--- | :--- |
| **Android 10** | Unsupported (Known Incompatible) |
| **Android 11** | Tested / Supported |
| **Android 12** | Tested / Supported |
| **Android 13** | Tested / Supported |
| **Android 14** | Tested / Supported |
| **Android 15** | Tested / Supported |
| **Android 16** | Tested / Supported |

* **Tested** - physically tested by the developer/test team and confirmed working.
* **Supported** - officially supported, although not necessarily tested on every device model.
* **Untested** - compatibility has not yet been verified. Untested does NOT mean supported.
* **Unsupported** - known not to work reliably with the current version.

---

## 3. 32-bit / 64-bit Compatibility

| Architecture | Status |
| :--- | :--- |
| **32-bit Android** | Tested / Supported |
| **64-bit Android** | Tested / Supported |

**How to check device architecture:**
Download a free app like "Device Info HW" from the Google Play Store. Go to the "CPU" or "System" tab and look for "Instruction Set" or "Architecture" to verify if your device is 32-bit or 64-bit.
*If you are unsure whether the phone is 32-bit or 64-bit, please contact support BEFORE purchasing.*

---

## 4. Hardware Requirements

| Requirement | Minimum | Recommended |
| :--- | :--- | :--- |
| **RAM** | 4GB | 6GB+ |
| **Free storage** | 1GB | 2GB+ |
| **CPU / hardware limitations** | Standard CPUs | Mid-range to High-end Snapdragon/MediaTek |

**Tested devices:**

| Brand / Model | Android | Architecture | Result |
| :--- | :--- | :--- | :--- |
| Standard Manufacturer UIs (Samsung, Xiaomi, Pixel) | 11 - 16 | 32/64-bit | Working |
| Non-standard Custom ROMs | Varies | Varies | Untested / Unsupported |

**Known incompatible or problematic configurations:**
* Devices running Android 10 and below.
* Very low-end hardware configurations (these will experience system instability or background task killing).

---

## 5. Important - Current MacroDroid Version Limitations
*The current version requires Android system changes. These limitations must be visible BEFORE purchase.*

### 5.1 Screen scaling - 600 dp
The current MacroDroid automation uses fixed screen coordinates. For correct operation:
**Developer Options -> Smallest width / Minimum width -> 600 dp**

**IMPORTANT:** Changing this setting affects the scale of the ENTIRE Android interface. Text, icons, buttons and other interface elements may become significantly smaller.
Before changing the setting, WRITE DOWN OR SCREENSHOT THE ORIGINAL VALUE.
Original value: __________ dp
*If you stop using the automation, restore the original value.*

### 5.2 Language requirements

| Application | Required language / status |
| :--- | :--- |
| **Android system** | English (United States or English UK) (Recommended) |
| **Instagram** | English (United States or English UK) (Required) |
| **Chrome** | English (United States or English UK) (Required) |
| **Telegram / Telegram bot** | English (United States or English UK) (Required) |
| **MacroDroid** | English (United States or English UK) (Required) |

*Note: The Android system can remain in Ukrainian or another language ONLY IF individual app languages for Chrome, Instagram, and Telegram are manually forced to English via Settings -> Apps.* 
*The language restrictions described here apply to the CURRENT MacroDroid version. Planned standalone-app capabilities must be described separately.*

---

## 6. Required Applications
*   **MacroDroid:** Play Store (Pro license recommended)
*   **Termux:** Verified Source - [Termux v1.0 APK](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk)
*   **Shizuku:** Verified Source - [Shizuku v1.0 APK](https://github.com/rajatroel/bot-files/releases/download/v1.0/Shizuku.apk)
*   **ZArchiver:** Play Store
*   **Instagram:** Official app from Play Store
*   **Telegram:** Official app from Play Store

*IMPORTANT: Do not direct customers to random APK files or unknown download sources.*

Part 2: Android Settings to Complete Installation Sequence
---

## 7. Required Android Settings & Permissions

| Application | Permission / Setting | Required value |
| :--- | :--- | :--- |
| **MacroDroid** | Accessibility | ON |
| **MacroDroid** | Battery optimization | Unrestricted / No Restrictions |
| **MacroDroid** | Display over other apps | ON |
| **MacroDroid** | Exact alarms | ON |
| **MacroDroid** | Notifications | ON |
| **Termux** | Battery optimization | Unrestricted / No Restrictions |
| **Termux** | Background activity | ON |
| **Termux** | Files & Storage / Media | ON |
| **Shizuku** | Battery optimization | Unrestricted / No Restrictions |
| **Shizuku** | Wireless debugging | ON |
| **ZArchiver** | Files & Storage / Media | ON |
| **Telegram** | Camera | ON (For QR Scanner) |

**App Pinning / Locking:** After completing setup, lock both Termux and MacroDroid in your phone's Recent Apps (App Switcher) screen so Android's memory manager never kills them.

---

## 8. Developer Options Setup
1. Open **Settings -> About phone**.
2. Tap **Build Number** 7 times to enable Developer Options.
3. Open **Developer Options** (usually found in Settings -> System).

| Setting | Value |
| :--- | :--- |
| **Smallest width / Minimum width** | 600 dp |
| **Wireless debugging** | ON |

---

## 9. Shizuku Setup
Shizuku is required to bypass system restrictions for automation.

**Installation & Starting via Wireless Debugging:**
1. Open the **Shizuku** app.
2. Scroll down to "Start via Wireless debugging" and tap **Pairing**.
3. Tap **Developer options** -> **Wireless debugging**.
4. Tap **Pair device with pairing code**. A 6-digit code will appear.
5. Enter this code into the Shizuku notification that pops up at the top of your screen.
6. Once paired successfully, return to the Shizuku app and tap **Start**.

**Verify Shizuku:**
The user should see: "Shizuku is running" at the top of the app with a version number.
*IMPORTANT: If Shizuku is not running, do NOT continue.*

**After phone restart:**
Does Shizuku need to be started again? **YES.** You must repeat the "Start" step in Shizuku every time your phone reboots.

---

## 10. Termux Setup
*   **Download source:** [Verified Termux APK](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk)
*   **Required version:** v1.0

**Commands:**
Open Termux, paste the following command and press Enter:
```bash
curl -sSL [https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh](https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh) | bash

When the Android storage permission popup appears, tap Allow. When prompted by the setup wizard, input your API ID, API Hash, License Key, and Instagram Usernames line by line.
11. MacroDroid Installation
 * Verified source: Google Play Store
 * Import automation Download: Replica.mdr
Steps:
 * Open MacroDroid -> tap the Export/Import tile on the home screen.
 * Check the box for Reset variables on import.
 * Tap Storage (under Import), select the downloaded Replica.mdr file from your Download folder, and tap Clear existing and import all.
Verify import:
The user should see: The imported macros listed in the "Macros" tab at the bottom of the screen.
12. Complete Installation Sequence
 * Check compatibility: Confirm Android version (11+), architecture, 4GB+ RAM, and current 600 dp limitations.
 * Generate Telegram API ID & Hash: Go to my.telegram.org using your target phone number. Create an application and save your API ID and Hash.
 * Install Apps: Install Termux, MacroDroid, ZArchiver, and Shizuku.
 * Prepare Android: Log in to VIP Instagram accounts in the official app. Ensure language is set to English.
 * Configure Shizuku: Enable Wireless Debugging and start Shizuku.
 * Set 600 dp: Change Smallest Width in Developer Options to 600 dp.
 * Install and configure Termux: Run the install script provided in Section 10. Enter API details, License Key, and IG Usernames.
 * Complete Telegram authentication (One-Time QR): Use a second phone to scan the QR code generated in Termux via ZArchiver.
 * Import the current automation: Import Replica.mdr into MacroDroid.
 * Grant ALL required permissions: Ensure Accessibility, Display Over Other Apps, and Unrestricted Battery are set. Lock Termux and MacroDroid in Recent Apps.
Final verification checklist:
 * [ ] Shizuku running
 * [ ] Termux configured
 * [ ] MacroDroid enabled
 * [ ] Accessibility enabled
 * [ ] Battery settings correct
 * [ ] 600 dp configured
 * [ ] Correct language configuration
 * [ ] License active
 * [ ] Instagram accounts connected
 * [ ] Telegram authenticated
 * [ ] Required apps locked in Recent Apps if necessary

### Part 3: First Run, Daily Use, and Troubleshooting
```markdown
---

## 13. First Run
**How to start the automation:**
1. Open **MacroDroid**.
2. Toggle the main MacroDroid switch at the top right of the home screen to ON.
3. Follow the visual [Tutorial Video](https://t.me/+2QbpNDGSQc05YjQ1) for any further trigger adjustments.

**How do I know it is working?**
The automation will bring Instagram to the foreground, automatically switch to the target account, and begin processing Likes, Comments, and Captchas in the background sequence.

**First-run test:**
*   [ ] Instagram opens correctly
*   [ ] Correct account is used
*   [ ] Link opens correctly
*   [ ] Automation performs expected action
*   [ ] Telegram communication works
*   [ ] No permission errors appear

---

## 14. Daily Use

| Question / action | Verified instruction |
| :--- | :--- |
| **Start automation** | Open MacroDroid and toggle the master switch to ON. |
| **Stop automation** | Open MacroDroid and toggle the master switch to OFF. |
| **Restart automation** | Toggle the MacroDroid switch OFF, then ON. |
| **Can I lock the screen?** | NO. The phone screen must remain unlocked and awake, as UI automation requires active screen coordinates. |
| **Can I use the phone while automation is running?** | NO. The automation controls the screen and taps buttons automatically. Manual touches will disrupt the sequence. |
| **Must Termux stay open?** | It must run in the background. Keep it locked in Recent Apps. |
| **Must MacroDroid stay open?** | It must run in the background. Keep it locked in Recent Apps. |
| **Must Shizuku remain running?** | YES. |
| **What happens after restarting the phone?** | You must manually restart Shizuku via Wireless Debugging, open Termux, and toggle MacroDroid ON. |
| **Can I use Instagram manually while automation runs?** | NO. Interrupting the app will break the current task. Toggle MacroDroid OFF first. |

---

## 15. Troubleshooting

*   **MacroDroid stops working:** Ensure MacroDroid, Termux, and Shizuku are set to "Unrestricted" in Battery settings and locked in Recent Apps. Verify Accessibility is ON.
*   **Termux stops / closes in background:** Lock Termux in the Recent Apps menu and verify battery optimization is completely disabled for it.
*   **Shizuku is not running:** Re-pair and restart via Developer Options -> Wireless Debugging.
*   **Shizuku authorization disappears:** Restart Shizuku.
*   **Accessibility permission turns off:** Android revokes this for security if an app isn't active. Re-enable in Settings -> Accessibility.
*   **Instagram opens the wrong page:** Ensure your language is English.
*   **Instagram link cannot be opened:** Ensure your default browser/link-handling settings route straight to the official Instagram app.
*   **Captcha fails:** Ensure your device resolution is strictly set to EXACTLY 600 dp. If it is slightly off, fixed coordinates will miss.
*   **Telegram authentication fails:** Ensure you used the exact API ID/Hash linked to the running phone number.
*   **QR camera is black:** Go to Android Settings -> Apps -> Telegram -> Permissions, and allow Camera access.
*   **License key invalid / API error:** Check for typos and ensure you have an active network connection.
*   **License expired:** Purchase a renewal via @iamrajatroel, then paste `curl -sL -o license.py https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py && python license.py && rm license.py` in Termux and enter the new key.

---

## 16. Contacting Technical Support
Before contacting support, prepare:
*   Phone manufacturer and exact model
*   Android version
*   32-bit or 64-bit architecture
*   RAM
*   Screenshot or screen recording of the problem
*   A screenshot of your Developer Options showing your screen is set to 600 dp
*   Exact error message

**Support contact:** [@iamrajatroel](https://t.me/iamrajatroel)
*Technical support is handled directly by the developer.*

Part 4: License, Updates, Known Issues, and Future App
---

## 17. License & Purchase
*   **Price:** $10 USDT / device / 30 days
*   **Accepted Crypto:** USDT (TON Network)
    ```text
    UQBk7Dto--IPECy0br6vPDN9YbIBu-T2xdYtqia3ob4DdOOP
    ```

**Before purchasing:** Confirm that the device meets the compatibility requirements above.

**Purchase:**
1. Contact the [@iamrajatroel](https://t.me/iamrajatroel) on Telegram for confirmation.
2. Send the exact USDT-TON amount to the payment address.
3. Take a clear screenshot of the completed transaction receipt and send it to the developer.

**Activation:**
Your unique license key will be delivered to your chat within 5 minutes. Enter this key during the Termux installation script.

**Renewal:**
Run the following command in Termux to apply a new key without reinstalling:
```bash
curl -sL -o license.py [https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py](https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py) && python license.py && rm license.py

18. Updates & Changelog
 * Current version: v1.0
 * Release date: September 21, 2026
v1.0 - September 21, 2026
 * Added: Full background task automation, AI captcha solving, multi-account switching.
 * Does this update require reinstalling? N/A (Initial Release)
19. Known Issues
| Issue | Affected configuration | Workaround | Status |
|---|---|---|---|
| UI Elements Too Small | All Devices | Requires manual change to 600 dp in Developer Options. | Limitation |
| App Freezes in Background | Devices < 4GB RAM | Keep Termux/MacroDroid locked in memory. | Limitation |
| Android 10 Incompatibility | Android 10 Devices | None. Upgrade to Android 11+. | Investigating |
20. Before You Buy - Final Checklist
 * [ ] My Android version is supported.
 * [ ] My device architecture is supported.
 * [ ] My device meets the hardware requirements.
 * [ ] I understand the current 600 dp requirement.
 * [ ] I understand the current language requirements.
 * [ ] I understand that MacroDroid, Termux and Shizuku are required for the current version.
 * [ ] I understand the required permissions/system changes.
 * [ ] I have read the known limitations.
 * [ ] I know how to contact technical support.
If you cannot confirm one of these points, please contact support BEFORE purchasing.
21. Future Dedicated App
A standalone application is planned and developed separately from the current MacroDroid version.
The goal is to reduce manual configuration, improve screen/DPI adaptability and provide broader language support.
IMPORTANT: Do not base your purchase on planned features. Customers purchasing the current version should make their decision strictly based on the CURRENT compatibility and features documented above.
