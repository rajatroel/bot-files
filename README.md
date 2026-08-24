## 🤖 Smm Kingdom Tasks Automation Bot

Welcome to the ultimate Instagram automation setup. Please read these basic requirements carefully before starting. If you miss a step, the bot will not work correctly!

### ⚠️ Basic Requirements & Conditions
* **Language:** Your Android system language MUST be set to **English (US or UK)**. Alternatively, you can manually set the language for the **Chrome** and **Instagram** apps to English in your phone's settings. Additionally, your **Telegram bot language** must also be set to English.
* **Permissions:** You MUST allow all requested permissions (Storage, Alarms, Battery, and Accessibility). The bot requires these to run reliably in the background without Android freezing it.
* **Instagram:** Make sure you are already logged into your required VIP accounts on the official Instagram app, and ensure they are available in your SMM Kingdom tasks bot.

### 📝 Prepare Your Data
Before installing, open your phone's **Notes app** and type out all your Instagram usernames correctly. This makes it incredibly easy to just copy and paste them when the initial setup asks for them!

### 🔑 How to get your Telegram API ID
You need your own Telegram API keys to connect the bot safely:
1. Go to [my.telegram.org](https://my.telegram.org) in your web browser.
2. Log in with your Telegram phone number (you will get a login code inside the Telegram app).
3. Tap on **API development tools**.
4. Fill in a random app name and short name, then click Create.
5. Copy your **API ID** (numbers only) and **API Hash** (long mix of letters/numbers) and save them in your Notes app.

---

### 🚀 Installation & Usage Guide

**Step 1: Install the Required Apps**
* **First App (Termux):** **[Click Here to Download Termux](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk)**. Install the downloaded APK file on your phone. *(Strictly download it from this link—do not use the Play Store version!)*
* **Second App (MacroDroid):** **[Click Here to Download MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid)**. Install it from the Google Play Store.

**Step 2: Import the Bot Macro & Start Permissions**
* **[Click Here to Download the Bot Macro]** *(Insert your raw macro link here)*
* Open MacroDroid, navigate to the **Export/Import** tab, and import the `backup.mdr` file you just downloaded.
* Turn the main switch at the top right of MacroDroid to **ON**.
* Follow the on-screen popups to enable the **Alarms**, **Battery**, and **Accessibility** permissions. 
* Once the permissions are granted, MacroDroid will automatically launch Termux for you!

**Step 3: Launch the Setup in Termux**
* Inside Termux, paste the exact command below and press Enter:

  curl -sL https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh | bash

* When the storage permission popup appears, click **Allow**. The setup will automatically detect it and start downloading your files.

**Step 4: Enter Your Details**
* When prompted, type or paste your details in this exact order: your **API ID**, your **API Hash**, and then your **License Key**.
* Next, enter your Instagram account names one by one.
* When you are completely done entering accounts, simply hit **Enter** on a blank line to finish!

**Step 5: The Final Authentication**
* Since this is your very first time running the bot, it will ask for your phone number and an OTP.
* Make sure you enter this exactly as it appears in your Telegram login!

**Step 6: Boom! You're Live**
* Once the screen says *"Automation and bot restarted"*, boom! Your automation has officially started. Let the automation work for you!

**🛑 How to Stop & Restart**
* **To Stop:** Pull down your phone's notification center and tap **Exit** on the Termux notification. This will automatically kill the automation. Then open MacroDroid and manually toggle the main switch to **OFF**.
* **To Restart:** Whenever you want to run the bot again, just open MacroDroid, enable the switch, and let the automation take over!
