👑 SMM Kingdom Tasks Automation Bot (Termux)
A fully automated, background-running system designed for @SmmKingdomTasksBot. This setup handles Instagram task execution (Likes, Comments), intelligent account switching, and 24/7 AI-powered math/emoji captcha solving with zero manual intervention.
⚠️ 1. Prerequisites & System Requirements
Before downloading or installing anything, verify these settings on your Android device:
 * System Language: Your phone's system language MUST be set to English (United States or English UK).
   * Alternative: If you must keep your system in another language, navigate to your phone's App Settings and manually set the individual language for Chrome and Instagram to English. Your language inside the Telegram bot must also be set to English.
 * Instagram App Setup: Ensure you are already logged into all your active Instagram accounts inside the official Instagram app, and that these accounts are added to @SmmKingdomTasksBot.
 * Battery & Background Permissions: You must disable battery optimization for both Termux and MacroDroid so Android does not close them in the background.
 * App Pinning: Lock/Pin both Termux and MacroDroid in your phone's Recent Apps (App Switcher) screen.
📝 2. Prepare Your Data
Open your phone's Notes app and prepare the following details so you can quickly paste them during setup:
 * Instagram Account Names: Write down the exact display names / usernames of your Instagram accounts in a clean list.
 * Telegram Credentials: Follow the steps in Section 3 to obtain your unique API ID and API Hash.
🔑 3. Generating Your Telegram API ID & Hash
The bot connects directly to Telegram's core network. You must generate your API credentials using the exact Telegram phone number you intend to run the automation on.
 * Open your mobile browser and go to my.telegram.org.
 * Enter your Telegram phone number in international format (e.g., +1234567890 or +919876543210) and click Next.
 * A confirmation message containing a web login code will be sent to your official Telegram app. Copy this code, paste it into the website, and click Sign In.
 * Tap on API development tools.
 * Fill in the form:
   * App title: Type any name (e.g., SMMRunner)
   * Short name: Type any short alphanumeric word (e.g., runner1)
   * You can leave the URL and platform fields blank or default.
 * Tap Create application.
 * Copy both your api_id (numeric string) and api_hash (alphanumeric string) and save them to your Notes app.
🚀 4. Step-by-Step Installation & Setup
Step 1: Install Required Applications
Download and install the following three tools:
 * Termux (Terminal Environment): Download Termux APK
   (Do not install Termux from Google Play Store; only this release contains the required background utilities).
 * MacroDroid (Macro Automation): Download MacroDroid from Google Play.
 * ZArchiver (Image Viewer for QR Login): Download ZArchiver from Google Play.
Step 2: Import & Configure MacroDroid
 * Download the Latest Macro File (backup.mdr) to your phone's Download folder.
 * Open MacroDroid \rightarrow tap the Export/Import tile on the main home screen.
 * Check the box labeled Reset variables on import.
 * Tap Storage (under the Import section), navigate to your Download folder, and select backup.mdr.
 * When prompted, select Clear existing and import all.
 * Grant all 4 system permissions prompted on screen:
   * Accessibility Service
   * Write System Settings
   * Draw Over Other Apps (Overlay)
   * Usage Access
 * Toggle the main MacroDroid switch at the top right OFF, wait 2 seconds, and toggle it back ON. Grant any remaining system dialog requests.
Step 3: Run the Termux Automated Installer
 * Open the Termux app.
 * Copy and paste the following one-line command and press Enter:
bash <(curl -sL https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh)

 * When the Android storage permission popup appears, tap Allow and return to Termux.
 * The installer will automatically download Python, build OpenCV, and configure all dependencies.
Step 4: Configure Your Bot Credentials
Once dependencies finish installing, the setup wizard will prompt you for your details directly in the terminal:
 * Enter API ID: Paste your numeric API ID \rightarrow Press Enter.
 * Enter API Hash: Paste your alphanumeric API Hash \rightarrow Press Enter.
 * Enter License Key: Paste your purchased license key (e.g., SMMK-1D-XXXX-XXXX-XXXX) \rightarrow Press Enter.
 * Enter Instagram Accounts: Paste your Instagram account display names one by one, pressing Enter after each name.
 * When you have entered all your accounts, press Enter on an empty line to save config.json and initialize the runner.
Step 5: Initial QR Code Login (One-Time Setup)
The bot authenticates using official Telegram QR linking. Your session is saved permanently to /sdcard/userbot.session, so you only need to complete this once.
========================================
       QR CODE OPENED ON SCREEN         
========================================
Scan the image showing on your screen with your other phone!
Waiting for scan (timeout 30s)...

 * The script will automatically generate a QR code and display it on your screen via ZArchiver or your default gallery app.
 * How to Scan:
   * Method A (Two Devices): Open Telegram on your second phone \rightarrow Go to Settings \rightarrow Devices \rightarrow Tap Link Desktop Device \rightarrow Point the camera at your main phone's screen.
   * Method B (Single Device): Take a screenshot of the QR code immediately \rightarrow Send it to a friend's phone or computer screen \rightarrow Open Telegram on your phone \rightarrow Settings \rightarrow Devices \rightarrow Link Desktop Device \rightarrow Point your camera at their screen.
 * 2FA Cloud Password: If your Telegram account has Two-Step Verification enabled, Termux will prompt:
   [!] 2FA Cloud Password detected. Enter your password:

   Type your Telegram password into Termux and press Enter.
 * Upon successful login, the temporary QR file is deleted, and your session is safely stored in internal storage.
Step 6: Live Execution & Monitoring
Once authenticated:
 * The bot will automatically purge old chat history with @SmmKingdomTasksBot.
 * It will send /start and click 📝Tasks📝.
 * When a like or comment task appears, the bot handles it automatically. When a vision captcha is triggered, the AI proxy solves the math problem in the background.
 * Do not touch your screen while MacroDroid is performing actions.
🛑 5. How to Stop & Restart
 * To Stop: Pull down your Android notification drawer and tap Exit on the persistent Termux notification. Then open MacroDroid and toggle the top-right switch to OFF.
 * To Restart: Open MacroDroid and toggle the switch to ON. MacroDroid will automatically wake Termux, load your saved session from storage, and resume automation instantly.
💳 6. License Packages, Pricing & Ordering
All licenses include 24/7 AI-powered captcha solving, automated account switching, and macro updates for the duration of the plan.
| Plan | Devices Supported | Duration | Price | Features Included |
|---|---|---|---|---|
| Single Runner | 1 Phone / HWID | 90 Days | $25 USDT | Auto-Like, Auto-Comment, AI Vision Solver |
| Farm Master | 4 Phones / HWIDs | 90 Days | $50 USDT | Multi-Device Sync, High Volume Farming |
💳 Accepted Payment Methods
 * Binance Pay ID: YOUR_BINANCE_PAY_ID
 * USDT (TON Network): YOUR_TON_WALLET_ADDRESS (Fastest & recommended)
 * Native TON Coin: YOUR_TON_WALLET_ADDRESS
 * USDT (TRC-20 Network): YOUR_TRC20_WALLET_ADDRESS
(Note: TON and USDT-TON transactions do not require a MEMO/Tag when sending to personal self-custody wallets).
📥 How to Order
 * Select your plan and transfer the exact amount to one of the payment addresses above.
 * Take a clear screenshot of the completed transaction receipt.
 * Send the screenshot along with your chosen plan to @iamrajatroel on Telegram.
 * Your custom license key and installation files will be delivered to you within 15 minutes!
 
