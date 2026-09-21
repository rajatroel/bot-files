👑 SMM Kingdom Tasks Automation Bot - Official README
Compatibility • Installation • Daily Use • Troubleshooting • Support
IMPORTANT: Please read the Compatibility Requirements and Current Version Limitations BEFORE purchasing a license. Do not purchase until the device has been checked against the verified requirements below.
1. Current Version Information
 * Product version: v1.0
 * Setup type: MacroDroid-based automation
 * Documentation last updated: September 21, 2026
 * Current license price: $10 USDT / device / 30 days
 * Developer / Support contact: @iamrajatroel on Telegram
2. Compatibility Requirements
 * Android 10: Unsupported (Known Incompatible)
 * Android 11: Tested / Supported
 * Android 12: Tested / Supported
 * Android 13: Tested / Supported
 * Android 14: Tested / Supported
 * Android 15: Tested / Supported
 * Android 16: Tested / Supported
 * Tested - physically tested by the developer/test team and confirmed working.
 * Supported - officially supported, although not necessarily tested on every device model.
 * Untested - compatibility has not yet been verified. Untested does NOT mean supported.
 * Unsupported - known not to work reliably with the current version.
3. 32-bit / 64-bit Compatibility
 * 32-bit Android: Tested / Supported
 * 64-bit Android: Tested / Supported
 * How to check device architecture: Download a free device information app from the Google Play Store to verify your architecture.
 * If the user is unsure whether the phone is 32-bit or 64-bit, instruct them to contact support BEFORE purchasing.
4. Hardware Requirements
 * RAM: 4GB Minimum Recommended.
 * Tested devices: Devices running Android 11 to 16 with standard manufacturer UIs are working.
 * Untested configurations: Non-standard custom Android ROMs are untested.
 * Known incompatible configurations: Very low-end hardware configurations (these will experience system instability or background task killing).
5. Important - Current MacroDroid Version Limitations
The current version requires Android system changes. These limitations must be visible BEFORE purchase.
5.1 Screen scaling - 600 dp
 * The current MacroDroid automation uses fixed screen coordinates.
 * For correct operation, set Developer Options -> Smallest width / Minimum width -> 600 dp.
 * IMPORTANT: Changing this setting affects the scale of the ENTIRE Android interface. Text, icons, buttons and other interface elements may become significantly smaller, which may be less comfortable for normal everyday phone use.
 * Before changing the setting, WRITE DOWN OR SCREENSHOT THE ORIGINAL VALUE.
 * If the user stops using the automation, restore the original value.
5.2 Language requirements
 * Android system: English (United States or English UK).
 * Instagram: English (United States or English UK) required.
 * Chrome: English (United States or English UK) required.
 * Telegram / Telegram bot: English required.
 * MacroDroid: English required.
 * The Android system can remain in another language while individual apps (like Chrome and Instagram) use English.
 * The language restrictions described here apply to the CURRENT MacroDroid version. Planned standalone-app capabilities must be described separately.
6. Required Applications
 * MacroDroid: Purchase its pro license from the Play Store.
 * Termux: Download the verified termux.apk from the provided GitHub release source.
 * Shizuku: Download the verified Shizuku.apk from the provided GitHub release source.
 * ZArchiver: Download from the Play Store.
 * Instagram: Official app required.
 * Telegram: Official app required.
 * IMPORTANT: Do not direct customers to random APK files or unknown download sources.
7. Required Android Settings & Permissions
 * MacroDroid: Accessibility must be ON.
 * MacroDroid: Battery optimization must be Unrestricted / No Restrictions.
 * MacroDroid: Display over other apps must be ON.
 * Termux: Battery optimization must be Unrestricted / No Restrictions.
 * Termux: Files & Storage / Media must be ON.
 * Shizuku: Battery optimization must be Unrestricted / No Restrictions.
 * Shizuku: Wireless debugging must be ON.
 * ZArchiver: Files & Storage / Media must be ON.
 * Telegram: Camera access must be ON (required for the Telegram QR scanner).
8. Developer Options Setup
 * Open Settings -> About phone.
 * Enable Developer Options by tapping the build number.
 * Open Developer Options.
 * Smallest width / Minimum width: Set to 600 dp.
 * Wireless debugging: Set to ON.
9. Shizuku Setup
 * Installation: Install the Shizuku application.
 * Start Shizuku: Run it on your device using wireless debugging.
 * Verify Shizuku: Ensure Shizuku is running properly on your device.
 * IMPORTANT: If Shizuku is not running, do NOT continue.
 * After phone restart: Yes, Shizuku needs to be started again via Wireless Debugging after a reboot.
10. Termux Setup
 * Download source: Download via the verified official GitHub release.
 * Commands: Open Termux, paste curl -sSL [https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh](https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh) | bash and press Enter.
 * When the Android storage permission popup appears, tap Allow and return to Termux.
 * When prompted by the setup wizard, input your API ID, API Hash, License Key, and Instagram Usernames line by line, pressing Enter after each.
11. MacroDroid Installation
 * Verified source: Play Store.
 * Import automation Download: Replica.mdr file.
 * Open MacroDroid: Tap the Export/Import tile.
 * Check the box for "Reset variables on import".
 * Tap Storage, select the backup.mdr file from your Download folder, and tap "Clear existing and import all".
 * Verify import: The automation rules will be successfully loaded into MacroDroid.
12. Complete Installation Sequence
 * Check compatibility: Confirm Android version, architecture, RAM, required apps and current limitations.
 * Prepare Android: Log in to all your working VIP Instagram accounts inside the official Instagram app.
 * Set 600 dp: Configure the minimum width/dpi of your device.
 * Install and configure Shizuku: Verify it is running.
 * Install and configure Termux: Run the installation script.
 * Install MacroDroid: Import the current automation.
 * Grant ALL required permissions: You must manually grant permissions; do not skip any, or the bot will fail.
 * Configure required language settings: Set to English.
 * Configure API ID / API Hash: Generate from my.telegram.org and input during Termux setup.
 * Enter license key: Paste during the Termux wizard.
 * Add Instagram accounts: Enter during the Termux wizard.
 * Complete Telegram authentication: Use your second phone to scan the QR code generated in Termux.
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
13. First Run
 * Start the automation: Toggle the MacroDroid switch.
 * How do I know it is working? The bot will automate Instagram Likes, Comments, account switching, and captcha solving in the background.
First-run test:
 * [ ] Instagram opens correctly
 * [ ] Correct account is used
 * [ ] Link opens correctly
 * [ ] Automation performs expected action
 * [ ] Telegram communication works
 * [ ] No permission errors appear
14. Daily Use
 * Start automation: Toggle the MacroDroid switch.
 * Can I lock the screen? No, the screen must remain active for UI interactions.
 * Can I use the phone while automation is running? Manual interference will disrupt the automation coordinates.
 * Must Termux stay open? Yes, lock it in your phone's Recent Apps screen so Android's memory manager never kills it.
 * Must MacroDroid stay open? Yes, lock it in your phone's Recent Apps screen.
 * Must Shizuku remain running? Yes.
15. Troubleshooting
 * MacroDroid stops working: Ensure both MacroDroid and Shizuku are set to "Unrestricted" in your Android Battery settings and are locked in the Recent Apps menu.
 * Termux stops / closes in background: Lock Termux in the Recent Apps menu and verify battery optimization is disabled for it.
 * Accessibility permission turns off: Android occasionally revokes Accessibility permissions for security if an app isn't actively opened; re-enable them in Settings → Accessibility.
 * Instagram link cannot be opened: Ensure your default browser or link-handling settings are correctly routing straight to the Instagram app.
 * Captcha fails: Ensure your device resolution is strictly set to exactly 600 dp in Developer Options. If it is even slightly off, fixed coordinates will miss the target.
 * Telegram authentication fails: Ensure you used the exact API ID and Hash linked to the phone number on the device.
 * QR camera is black: Go to your Android Settings → Apps → Telegram → Permissions, and allow Camera access.
16. Contacting Technical Support
 * Before contacting support, prepare: Phone manufacturer and exact model, Android version, 32-bit or 64-bit architecture, RAM, Screenshot or screen recording of the problem, Exact error message, What happened immediately before the error, and Whether the problem happens every time or occasionally.
 * Include a screenshot of your Developer Options showing your screen is set to 600 dp.
 * Support contact: Contact @iamrajatroel on Telegram.
 * Technical support is handled directly by the developer.
17. License & Purchase
 * Price: $10 USDT / device / 30 days
 * Before purchasing: Confirm that the device meets the compatibility requirements above.
 * Purchase: Send the exact plan amount to the USDT (TON Network) address UQBk7Dto--IPECy0br6vPDN9YbIBu-T2xdYtqia3ob4DdOOP, take a clear screenshot of the completed transaction receipt, and send it to @iamrajatroel.
 * Activation: Your unique license key and its information will be delivered to your chat within 5 minutes.
 * Renewal: Paste the command curl -sL -o license.py [https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py](https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py) && python license.py && rm license.py in Termux, press Enter, and paste your new license key when prompted.
18. Updates & Changelog
 * Current version: v1.0
 * Release date: September 21, 2026
 * Added: Initial release of the fully automated, background task-completion engine with intelligent AI-powered vision captcha solving.
19. Known Issues
 * No confirmed known issues beyond the documented 600 dp resolution requirement and the Android 10 and below incompatibility at this time.
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
 * If the customer cannot confirm one of these points, instruct them to contact support BEFORE purchasing.
21. Future Dedicated App
 * A standalone application is planned/developed separately from the current MacroDroid version.
 * The goal is to reduce manual configuration, improve screen/DPI adaptability and provide broader language support.
 * IMPORTANT: Do not describe planned features as currently available. Customers purchasing the current version should make their decision based on the CURRENT compatibility and features documented above.
