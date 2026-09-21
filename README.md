# 👑 SMM Kingdom Tasks Automation Bot

[![Version](https://img.shields.io/badge/version-v1.0-blue?style=flat-square)](#18-updates--changelog)
[![Android](https://img.shields.io/badge/Android-11%2B-3DDC84?style=flat-square&logo=android&logoColor=white)](#2-compatibility-requirements)
[![Setup](https://img.shields.io/badge/setup-MacroDroid-orange?style=flat-square)](#11-macrodroid-installation)
[![Support](https://img.shields.io/badge/support-Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/iamrajatroel)

An automation for **@SmmKingdomTasksBot** that completes Instagram **Like** and **Comment** tasks, switches between your Instagram accounts, and solves the bot's image captcha with an online AI service. It runs on your Android phone using **MacroDroid**, **Termux** and **Shizuku**.

**[Compatibility](#2-compatibility-requirements)** • **[Installation](#12-complete-installation-sequence)** • **[Daily Use](#14-daily-use)** • **[Troubleshooting](#15-troubleshooting)** • **[Support](#16-contacting-technical-support)**

> [!IMPORTANT]
> Read the [Compatibility Requirements](#2-compatibility-requirements) and the [Current Version Limitations](#5-important---current-macrodroid-version-limitations) **BEFORE** purchasing a license. Do not purchase until your device has been checked against the requirements below, and finish the [Before You Buy checklist](#20-before-you-buy---final-checklist).

## At a Glance

| You need | Details | Read |
| :--- | :--- | :--- |
| Android 11 or newer | Android 10 and below is not supported | [§2](#2-compatibility-requirements) |
| Screen set to exactly **600 dp** | Shrinks your **entire** Android interface | [§5.1](#51-screen-scaling---600-dp) |
| **English** (US/UK) | Chrome, Instagram and @SmmKingdomTasksBot must be in English | [§5.2](#52-language-requirements) |
| Three helper apps | MacroDroid + Termux + Shizuku (plus ZArchiver). Shizuku must be restarted after **every** phone reboot | [§6](#6-required-applications), [§9](#9-shizuku-setup) |
| A **second phone** | Needed once, to scan the Telegram QR login | [§12](#12-complete-installation-sequence) |
| Your own Telegram **API ID + Hash** | Generated at my.telegram.org with the number that will run the bot | [§12](#step-3--generate-your-telegram-api-id--hash) |
| A license | $10 USDT / device / 30 days | [§17](#17-license--purchase) |

## Table of Contents

| # | Section | # | Section |
| :-: | :--- | :-: | :--- |
| 1 | [Current Version Information](#1-current-version-information) | 12 | [Complete Installation Sequence](#12-complete-installation-sequence) |
| 2 | [Compatibility Requirements](#2-compatibility-requirements) | 13 | [First Run](#13-first-run) |
| 3 | [32-bit / 64-bit Compatibility](#3-32-bit--64-bit-compatibility) | 14 | [Daily Use](#14-daily-use) |
| 4 | [Hardware Requirements](#4-hardware-requirements) | 15 | [Troubleshooting](#15-troubleshooting) |
| 5 | [Current MacroDroid Version Limitations](#5-important---current-macrodroid-version-limitations) | 16 | [Contacting Technical Support](#16-contacting-technical-support) |
| 6 | [Required Applications](#6-required-applications) | 17 | [License & Purchase](#17-license--purchase) |
| 7 | [Required Android Settings & Permissions](#7-required-android-settings--permissions) | 18 | [Updates & Changelog](#18-updates--changelog) |
| 8 | [Developer Options Setup](#8-developer-options-setup) | 19 | [Known Issues](#19-known-issues) |
| 9 | [Shizuku Setup](#9-shizuku-setup) | 20 | [Before You Buy - Final Checklist](#20-before-you-buy---final-checklist) |
| 10 | [Termux Setup](#10-termux-setup) | 21 | [Future Dedicated App](#21-future-dedicated-app) |
| 11 | [MacroDroid Installation](#11-macrodroid-installation) | | |

---

## 1. Current Version Information

| Field | Information |
| :--- | :--- |
| **Product version** | v1.0 |
| **Setup type** | MacroDroid-based automation (MacroDroid + Termux + Shizuku) |
| **Documentation last updated** | 21 September 2026 |
| **Current license price** | $10 USDT / device / 30 days |
| **Developer / Support contact** | [@iamrajatroel](https://t.me/iamrajatroel) on Telegram |

---

## 2. Compatibility Requirements

### Android compatibility

| Android version | Status | Notes |
| :--- | :--- | :--- |
| Android 10 and below | ❌ **Unsupported** | Known incompatible. |
| Android 11 | ✅ **Tested** | Minimum supported version. |
| Android 12 | ✅ **Tested** | |
| Android 13 | ✅ **Tested** | |
| Android 14 | ✅ **Tested** | |
| Android 15 | ✅ **Tested** | |
| Android 16 | ✅ **Tested** | |
| Android 17 and newer | ⚠️ **Untested** | Untested does **not** mean supported. |
| Non-standard custom ROMs | ⚠️ **Untested** | Testing covered standard manufacturer UIs only. |

> [!NOTE]
> Android 11 is also the minimum for starting Shizuku directly on the phone via Wireless debugging. On Android 10 and below, Shizuku's official guide requires a computer instead ([Shizuku user manual](https://shizuku.rikka.app/guide/setup/)).

### Status definitions

| Status | Meaning |
| :--- | :--- |
| **Tested** | Physically tested by the developer/test team and confirmed working. |
| **Supported** | Officially supported, although not necessarily tested on every device model. |
| **Untested** | Compatibility has not yet been verified. Untested does **NOT** mean supported. |
| **Unsupported** | Known not to work reliably with the current version. |

---

## 3. 32-bit / 64-bit Compatibility

| Architecture | Status |
| :--- | :--- |
| **32-bit Android** | ✅ **Supported** |
| **64-bit Android** | ✅ **Supported** |

The installer contains a separate environment package for each architecture and picks one automatically ([§10](#10-termux-setup)).

### How to check your device architecture

1. Install **Termux** from the link in [§6](#6-required-applications) and open it.
2. Run:

   ```bash
   uname -m
   ```

3. Read the result (this is the same check the installer performs):

   | Result | Architecture |
   | :--- | :--- |
   | `aarch64` or `x86_64` | **64-bit** |
   | anything else, e.g. `armv7l`, `armv8l` | **32-bit** |

*Alternative:* install a device-information app from Google Play that shows the CPU architecture / supported ABIs.

> [!TIP]
> Not sure whether your phone is 32-bit or 64-bit? **Contact [support](https://t.me/iamrajatroel) BEFORE purchasing.**

---

## 4. Hardware Requirements

| Requirement | Minimum | Recommended |
| :--- | :--- | :--- |
| **RAM** | Not established — devices below 4 GB are untested | **4 GB** |
| **Free storage** | Not specified for v1.0 | Not specified for v1.0 |
| **CPU / hardware limitations** | Very low-end hardware is **known to be incompatible**: it experiences system instability or background task killing | 4 GB RAM or more |

If your phone's storage is nearly full, ask support before purchasing: the installer downloads and unpacks an environment archive, and your configuration and Telegram session are stored in internal storage.

**Also required**

- An **internet connection** at all times (Telegram, license check and captcha solving).
- **Wi-Fi** when starting Shizuku via Wireless debugging ([§9](#9-shizuku-setup)).
- A **second phone** with the official Telegram app, once, for the QR login ([§12](#step-4--one-time-telegram-qr-login)).

### Tested devices

No per-device test list has been published for v1.0. Compatibility is documented per Android version ([§2](#2-compatibility-requirements)) and architecture ([§3](#3-32-bit--64-bit-compatibility)). To confirm your exact model before buying, ask support.

<!-- Maintainer: when device results exist, add a table here with columns: Brand / Model | Android | 32/64-bit | Result (Working / Limited / Failed). -->

### Known incompatible or problematic configurations

- Android 10 and below.
- Very low-end hardware (system instability or background task killing).
- Any phone that cannot be set to exactly **600 dp** ([§5.1](#51-screen-scaling---600-dp)).
- Non-standard custom ROMs are **untested**, not supported.

---

## 5. Important - Current MacroDroid Version Limitations

> [!WARNING]
> The current version requires changes to your Android system. These limitations apply to the **current MacroDroid version** and must be understood **BEFORE** purchase.

### 5.1 Screen scaling - 600 dp

The current MacroDroid automation uses **fixed screen coordinates**. For correct operation you must set:

```text
Developer Options -> Drawing -> Smallest width / Minimum width -> 600 dp
```

> [!IMPORTANT]
> Changing this setting affects the scale of the **ENTIRE** Android interface. Text, icons, buttons and all other interface elements become significantly smaller, which may be less comfortable for everyday phone use.

- **Before changing it, WRITE DOWN OR SCREENSHOT THE ORIGINAL VALUE.** Phones ship with different defaults (for example 360-420 dp).

  Original value: `__________ dp`

- The value must be **exactly 600**. Even a slightly different value makes the fixed coordinates miss their targets.
- If you change the standard *Display size / Screen zoom* slider afterwards, re-check that the value still reads 600.
- If you stop using the automation, restore the original value in the same setting.

### 5.2 Language requirements

| Application | Required language / status |
| :--- | :--- |
| **Android system** | English (United States or United Kingdom) — **or** another system language, as long as Chrome and Instagram are each set to English individually (see below) |
| **Instagram** | English (United States or United Kingdom) |
| **Chrome** | English (United States or United Kingdom) |
| **Telegram bot (@SmmKingdomTasksBot)** | English (set inside the bot) |
| **Telegram app** | Not verified — ask support if it matters for your setup |
| **MacroDroid** | Not verified — if your MacroDroid is not in English, ask support before purchasing |

**Can the system stay in another language (for example Ukrainian)?** Yes, but only if Chrome and Instagram each use English on their own.

- **Android 13 and newer:** *Settings → System → Languages & input → App languages* → choose the app → English (United States or United Kingdom). Menu names vary slightly by brand, and an app only appears in that list if it supports multiple languages.
- **Android 11 and 12:** the system has no per-app language setting (an app can only change language if it has its own picker). The reliable option is to set the **whole system language** to English (US/UK).

The language restrictions above apply to the **current MacroDroid version** only. Planned standalone-app capabilities are described separately in [§21](#21-future-dedicated-app).

---

## 6. Required Applications

> [!IMPORTANT]
> Only use the download sources listed here. Do **not** install this setup from random APK files or unknown websites.

| Application | Purpose | Verified source | Version / APK |
| :--- | :--- | :--- | :--- |
| **MacroDroid** | Runs the on-screen automation | [Google Play](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) | Current Play Store version. **Pro recommended** — the free version is limited to 5 macros and shows ads; Pro is a one-time upgrade. |
| **Termux** | Runs the automation script | [Developer-provided `termux.apk`](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk) (release v1.0) | Use **this APK** — other Termux builds are not covered by this guide. |
| **Shizuku** | Required helper service | [Developer-provided `Shizuku.apk`](https://github.com/rajatroel/bot-files/releases/download/v1.0/Shizuku.apk) (release v1.0) | Use **this APK**. Official guide: [shizuku.rikka.app](https://shizuku.rikka.app/guide/setup/) |
| **ZArchiver** | Displays the one-time login QR code | [Google Play](https://play.google.com/store/apps/details?id=ru.zdevs.zarchiver) | Current Play Store version. Open it once, allow its permissions, then close it. |
| **Instagram** | The app the automation controls | Official Instagram app ([Google Play](https://play.google.com/store/apps/details?id=com.instagram.android)) | Official app required. |
| **Telegram** | Your account and the second phone's QR scanner | Official Telegram app ([Google Play](https://play.google.com/store/apps/details?id=org.telegram.messenger)) | Official app required. |
| **Chrome** | Used by the current automation; must be in English | Pre-installed on most phones / [Google Play](https://play.google.com/store/apps/details?id=com.android.chrome) | Any current version, English UI. |

---

## 7. Required Android Settings & Permissions

Every permission the current version needs is listed here. **Do not skip any**, or the automation will fail. If an app asks for a permission that is **not** in this table, contact support before continuing.

| Application | Permission / setting | Required value |
| :--- | :--- | :--- |
| MacroDroid | Accessibility | **ON** (lets MacroDroid interact with the screen) |
| MacroDroid | Display over other apps | **ON** (automation overlays) |
| MacroDroid | Files & storage / media | **Allowed** |
| MacroDroid | Battery optimization | **Unrestricted** / *Don't optimize* |
| Termux | Files & storage / media | **Allowed** (the installer shows the popup, [§10](#10-termux-setup)) |
| Termux | Battery optimization | **Unrestricted** / *Don't optimize* |
| Shizuku | Battery optimization | **Unrestricted** / *Don't optimize* |
| Shizuku | Notifications | **Allowed** (the pairing code is entered through a Shizuku notification) |
| Shizuku | Wireless debugging (Developer options) | **ON** and paired ([§9](#9-shizuku-setup)) |
| Shizuku | Authorization of other apps | Not documented by the developer yet — see [§9](#9-shizuku-setup) |
| ZArchiver | Files & storage / media | **Allowed** |
| Telegram (**second phone**) | Camera | **Allowed** (for scanning the QR code) |
| Instagram | Account login | **All** accounts you want to use are logged in |
| Termux, MacroDroid, Shizuku | Recent Apps lock | **Locked** — after setup is complete ([§12](#12-complete-installation-sequence)) |

> Battery setting names vary: Android 12+ usually says **Unrestricted**; Android 11 and some brands say **Don't optimize** / **No restrictions** (often under *Settings → Apps → Special app access → Battery optimization*).

### Manufacturer-specific settings

No brand-specific requirements have been confirmed by the developer, and the settings above apply to every brand. Some manufacturers are known to restrict background apps more aggressively than stock Android. Third-party notes (**not tested with this automation**):

| Brand | Note |
| :--- | :--- |
| **Xiaomi / Redmi / POCO** | Shizuku's manual lists a known issue where ADB permission is limited on some systems (mainly MIUI-based). Some Xiaomi builds have an extra **USB debugging (Security settings)** toggle in Developer options. |
| **Samsung** | No additional requirement confirmed. |
| **Realme / Oppo** | No additional requirement confirmed. |
| **OnePlus** | Reported to revert battery-optimization settings on its own. Re-check them after updates and keep the apps locked in Recent Apps ([source](https://dontkillmyapp.com/oneplus)). |
| **Motorola** | No additional requirement confirmed. |

General reference for background-app restrictions by brand: [dontkillmyapp.com](https://dontkillmyapp.com).

---

## 8. Developer Options Setup

1. Open **Settings → About phone**.
2. Tap the **Build number** **7 times** (enter your PIN/pattern if asked) until you see that Developer options are enabled. The exact path depends on your brand:

   | Brand | Where to tap 7 times |
   | :--- | :--- |
   | Stock Android / Pixel | Settings → About phone → Build number |
   | Samsung | Settings → About phone → Software information → Build number |
   | Xiaomi / Redmi / POCO | Settings → About phone (My device) → All specs → **OS version** (**MIUI version** on MIUI) |
   | Realme | Settings → About phone → Version → Build number |
   | Oppo | Settings → About device → Version → Version number |
   | OnePlus | Settings → About phone → Build number |
   | Motorola | Settings → About phone → (Software information →) Build number |

3. Open **Developer options**. Its location varies: often *Settings → System → Developer options*, or at the bottom of the main Settings menu on Samsung. You can also search Settings for "Developer options".
4. Set the following:

   | Setting | Value |
   | :--- | :--- |
   | Smallest width / Minimum width (in the *Drawing* section) | **600 dp** — set at the step shown in [§12](#12-complete-installation-sequence); note your original value first ([§5.1](#51-screen-scaling---600-dp)) |
   | Wireless debugging | **ON** (needed to start Shizuku; your phone must be on Wi-Fi) |
   | USB debugging | **ON** (listed in Shizuku's official setup guide) |
   | Other | No other Developer options are required by the developer |

---

## 9. Shizuku Setup

> [!IMPORTANT]
> Shizuku is part of the current setup. **If Shizuku is not running, do NOT continue.**

Official reference: [Shizuku user manual](https://shizuku.rikka.app/guide/setup/).

### Installation

1. Download **`Shizuku.apk`** from the link in [§6](#6-required-applications) and install it (allow installs from your browser/file manager if Android asks).
2. Open Shizuku once and allow notifications when asked.

### Start Shizuku using Wireless Debugging

Works on Android 11 and newer, with no computer.

1. Connect the phone to **Wi-Fi**.
2. Enable **Developer options** and switch **Wireless debugging** ON ([§8](#8-developer-options-setup)).
3. **Pair once:** in Shizuku, under *Start via Wireless debugging*, tap **Pairing**. In Developer options → Wireless debugging, tap **Pair device with pairing code**. A 6-digit code appears.
4. Pull down the notification shade, open the **Shizuku** notification, tap **Enter pairing code**, type the code and send it. You should see a *pairing successful* message.
5. Go back to Shizuku and tap **Start**. A command window opens for a few seconds and closes by itself.

### Verify Shizuku

The Shizuku app's main screen shows **"Shizuku is running"**.

If it shows that Shizuku is **not** running, stop here and fix it before continuing ([Shizuku is not running](#shizuku-is-not-running)).

### After phone restart

**Yes — Shizuku must be started again after every phone restart.** This is a system limitation stated in Shizuku's manual. You do **not** normally need to pair again:

1. Connect to Wi-Fi and make sure **Wireless debugging** is ON.
2. Open Shizuku and tap **Start**.
3. If it will not start, switch Wireless debugging **OFF and ON**, then tap **Start** again. If Shizuku asks to pair again, repeat steps 3-4 above.

> [!NOTE]
> Which apps must be authorized inside Shizuku is not documented by the developer yet. If Shizuku shows an authorization request during setup, keep the request visible and contact support before dismissing it.

---

## 10. Termux Setup

**Download source:** [developer-provided `termux.apk`](https://github.com/rajatroel/bot-files/releases/download/v1.0/termux.apk) (release v1.0).
**Required version:** use this APK. Other Termux builds (Play Store, F-Droid) are not covered by this guide.

> [!WARNING]
> The installer unpacks a pre-built Termux environment into Termux's data folder and may overwrite existing Termux files. **Use a fresh Termux installation** and do not run it on a Termux setup that holds data you need.

### Commands

Open **Termux**, paste the command and press **Enter**:

```bash
curl -sSL https://raw.githubusercontent.com/rajatroel/bot-files/main/install.sh | bash
```

This downloads and runs the developer's installer script. You can read it first: [`install.sh`](https://github.com/rajatroel/bot-files/blob/main/install.sh).

### What you should see

The screen clears between stages.

**1. Storage permission** — an Android popup appears. Tap **Allow**, then return to Termux.

```text
SETTING UP PERMISSIONS
Storage permission is required
to install the automation.
Waiting for you to click 'Allow'.....
Storage permission granted!
```

**2. Architecture detection** — the installer picks the 32-bit or 64-bit package.

```text
DETECTING DEVICE ARCHITECTURE
Detected architecture: aarch64
Selecting 64-bit installation...
```

**3. Download and extraction** — wait until it finishes; do not close Termux.

```text
Downloading environment : 100.0% Done!
Extracting system files
(Please wait)...
```

**4. Setup wizard** — screen title `CREATE YOUR CONFIG`. Enter your details line by line, pressing **Enter** after each:

| Prompt | What to enter |
| :--- | :--- |
| `Enter your Telegram API ID :` | Your numeric **API ID** (digits only) |
| `Enter your Telegram API HASH :` | Your alphanumeric **API Hash** |
| `Enter your Automation License Key :` | Your license key, e.g. `SMMK-1D-XXXX-XXXX-XXXX` |
| `Account 1:`, `Account 2:` ... | One **Instagram username** per line (the leading `@` is optional). Check the spelling carefully. |
| *(empty line)* | Press **Enter** on an empty line when you have entered all accounts |

Success message: `CONFIGURATION SAVED`. Your details are stored in `/sdcard/config.json`. Next, prepare your second phone for the QR login ([§12, Step 4](#step-4--one-time-telegram-qr-login)).

### Common errors

| Message | Meaning | What to do |
| :--- | :--- | :--- |
| `Storage permission not detected! If you clicked 'Deny', we must try again.` | The storage popup was denied or dismissed. | Tap **Allow** when the popup returns. If it does not, open Android Settings → Apps → Termux → Permissions and allow files/media. |
| `Error: API ID must contain numbers only. Please run the setup again.` | The API ID contains something other than digits (for example you pasted the Hash). | Run the install command again and enter the numeric API ID. |
| `Error: API HASH cannot be empty.` / `Error: License Key cannot be empty.` | Nothing was entered. | Run the install command again. |
| `Error: You must enter at least one account. Try again.` | The account list was finished while empty. | Enter at least one Instagram username. |
| `Setup cancelled by user. No files were saved.` | Setup was interrupted. | Run the install command again. |
| Command stops during download or extraction | Usually an interrupted connection (the installer stops at the first failure). | Check your internet connection and run the same command again. |

> [!NOTE]
> Running the install command again repeats the **whole** installation and asks for all details again. To change only your license key, use the update command in [§17](#17-license--purchase).

---

## 11. MacroDroid Installation

**Verified source:** [Google Play](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid)
**Required/current version:** the current Play Store version. Pro is recommended (the free version is limited to 5 macros and shows ads).

### Import automation

**Download:** [`Replica.mdr`](https://github.com/rajatroel/bot-files/releases/download/v1.0/Replica.mdr) to your phone's **Download** folder.

> [!WARNING]
> **Clear existing and import all** removes the macros already in your MacroDroid. If you use MacroDroid for anything else, back them up first.

1. Open **MacroDroid**.
2. Tap the **Export/Import** tile on the home screen.
3. Under Import, tick **Reset variables on import**.
4. Tap **Storage**, select the downloaded **`Replica.mdr`** file from your Download folder.
5. Tap **Clear existing and import all**.

### Verify import

The imported macros appear in MacroDroid's macro list. If the import fails or nothing appears, contact support with a screenshot.

---

## 12. Complete Installation Sequence

This section covers the entire setup from a clean phone to a working automation. Follow the steps **in order**. The 600 dp change comes late on purpose, so you complete the fiddly steps at your normal interface size.

| Step | Do this | Details |
| :-: | :--- | :--- |
| 1 | **Check compatibility** — Android version, architecture, RAM, required apps, current limitations | [§2](#2-compatibility-requirements)-[§5](#5-important---current-macrodroid-version-limitations), [§20](#20-before-you-buy---final-checklist) |
| 2 | **Prepare Android and accounts** | below |
| 3 | **Generate your Telegram API ID and Hash** | below |
| 4 | **Install the required apps** | [§6](#6-required-applications) |
| 5 | **Enable Developer options, then install and start Shizuku** | [§8](#8-developer-options-setup), [§9](#9-shizuku-setup) |
| 6 | **Grant ALL required permissions** and battery settings | [§7](#7-required-android-settings--permissions) |
| 7 | **Install and configure Termux** — run the installer; enter API ID, API Hash, **license key** and **Instagram accounts** | [§10](#10-termux-setup) |
| 8 | **Complete Telegram authentication** (one-time QR login with a second phone) | below |
| 9 | **Install MacroDroid and import the current automation** | [§11](#11-macrodroid-installation) |
| 10 | **Set 600 dp** | [§5.1](#51-screen-scaling---600-dp) |
| 11 | **Configure required language settings** (English) | [§5.2](#52-language-requirements) |
| 12 | **Apply any further MacroDroid adjustments** shown in the [video tutorial](https://t.me/+2QbpNDGSQc05YjQ1) | tutorial |
| 13 | **Lock Termux, MacroDroid and Shizuku** in Recent Apps | [§7](#7-required-android-settings--permissions) |
| 14 | **Final verification, then first run** | below, [§13](#13-first-run) |

### Step 2 — Prepare Android and accounts

1. Log in to **all** the Instagram accounts you want to use, inside the official Instagram app.
2. Make sure those accounts are added to **@SmmKingdomTasksBot**, and that the bot's language is set to **English**.
3. Note your original *Smallest width* value now ([§5.1](#51-screen-scaling---600-dp)).
4. Put Chrome and Instagram (or the whole system) into **English (US/UK)** ([§5.2](#52-language-requirements)).

### Step 3 — Generate your Telegram API ID & Hash

The bot connects directly to the Telegram network using your own API credentials.

> [!IMPORTANT]
> Generate your API ID and Hash with the **exact Telegram phone number** you will use to run the automation. The license check also uses your API Hash, so keep using the same credentials ([§17](#17-license--purchase)).

1. Open your browser and go to **[my.telegram.org](https://my.telegram.org)**.
2. Enter your Telegram phone number in international format (e.g. `+1234567890` or `+919876543210`) and click **Next**.
3. Telegram sends a login code to your official Telegram app. Copy it into the website and click **Sign In**.
4. Click **API development tools**.
5. Fill in **App title** (e.g. `Runner`) and **Short name** (e.g. `runner1`). URL and Platform can stay default/empty.
6. Click **Create application**.
7. Copy your **`api_id`** (numbers) and **`api_hash`** (letters and numbers) and store them securely in your Notes app. Never share your API Hash publicly.

### Step 4 — One-time Telegram QR login

You need a **second phone** with the official Telegram app logged in to your target number.

1. **Prepare the scanner (second phone):** open Telegram → **Settings → Devices → Link Desktop Device**. If the camera is black, allow Camera for Telegram ([QR camera is black](#qr-camera-is-black)).
2. **Generate the QR code (main phone):** in Termux, press **Enter** to start the script and generate the QR code.
3. **Open and scan:** when asked how to open the image, choose **ZArchiver** and **immediately** scan it with the second phone. A QR code is valid for about 30 seconds and refreshes automatically (`QR code expired. Refreshing on screen...`) — always scan the newest one. If ZArchiver is not installed, Android's default "Open with" chooser is used.
4. **2FA password:** if Two-Step Verification is enabled, Termux asks `2FA Cloud Password detected. Enter your password:`. Type it (it is visible while typing) and press **Enter**.
5. **Success:** Termux prints `Logged in successfully!`, the temporary QR image is deleted, and your session file stays in internal storage (`/sdcard/userbot.session`). A new device appears in your Telegram app.
6. **Safe exit:** press the back button to close the image. To close Termux cleanly, swipe it away from Recent Apps, reopen Termux, pull down the notification panel and tap **Exit**.

> [!WARNING]
> Never send anyone your session file (`userbot.session`) or your Telegram login codes. The session file gives access to your Telegram account.

### Final verification checklist

Before the first run, confirm every item:

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

---

## 13. First Run

### Start the automation

1. Confirm **Shizuku is running** ([§9](#9-shizuku-setup)).
2. Open **MacroDroid**.
3. Toggle the **MacroDroid switch** to **ON**.

Keep Termux, MacroDroid and Shizuku running in the background ([§14](#14-daily-use)).

### How do I know it is working?

The Termux window shows status messages (as of v1.0). A healthy start looks like this:

```text
Checking license...
License validated!

AUTOMATION STARTED SUCCESSFULLY

Bot restarted
Clicking : 📝Tasks📝
```

> [!NOTE]
> On every start the automation **clears your chat history with @SmmKingdomTasksBot**, sends `/start` and opens the Tasks menu.

Then, as tasks arrive, you will see lines such as:

| Message in Termux | What it means |
| :--- | :--- |
| `Like task detected` / `Comment task detected` | A task was received and is being performed on screen |
| `Switching to: <username>` | The automation is changing Instagram account |
| `Clicking : ✅Completed (Attempt 1/2)` | Task finished and reported to the bot |
| `Captcha detected` → `Solving captcha...` → `Captcha answer : ...` | The bot's security check is being solved |
| `Verification successful` | The captcha was accepted |
| `No task detected` | The bot has no tasks right now — this is normal, it keeps checking |
| `Clicking : ❌Skip` | The task was skipped (see below) |

On your screen you will see Instagram open the task link and perform the action, and switch accounts when needed.

**What the current version skips:** follow-type tasks, and comment tasks whose text contains an `@` mention.

### First-run test

- [ ] Instagram opens correctly
- [ ] Correct account is used
- [ ] Link opens correctly
- [ ] Automation performs the expected action
- [ ] Telegram communication works
- [ ] No permission errors appear

### Online services used (v1.0)

- **Telegram** — your account logs in directly, using your API ID and Hash.
- **Developer's license server** — receives your license key and API Hash (used as the device identifier) when the automation starts and when captchas are solved.
- **Developer's captcha-solving service** — receives the processed captcha images.

---

## 14. Daily Use

| Question / action | Verified instruction |
| :--- | :--- |
| **Start automation** | Make sure Shizuku is running, then toggle the **MacroDroid switch ON** ([§13](#13-first-run)). |
| **Stop automation** | Turn the MacroDroid switch **OFF**, then close Termux cleanly (swipe it away from Recent Apps, reopen Termux, pull down the notification panel, tap **Exit**). The script also stops **by itself** after a license error, a failed captcha verification, or when the bot stops responding — the script does **not** restart itself. |
| **Restart automation** | Stop it as above, fix the cause if there was an error message, then start it again. |
| **Can I lock the screen?** | ⚠️ Not confirmed by the developer. The current version taps the screen at fixed coordinates, so do not assume it keeps working with the screen off or locked. Ask support before relying on it. |
| **Can I use the phone while automation is running?** | ⚠️ Not confirmed by the developer. On-screen actions happen at fixed coordinates, so using the phone at the same time may interfere. Ask support before relying on it. |
| **Must Termux stay open?** | Yes. The script runs inside Termux and stops if Termux is closed or killed. Keep it running and locked in Recent Apps. |
| **Must MacroDroid stay open?** | Yes. It performs the on-screen actions, so it must stay enabled and locked in Recent Apps. |
| **Must Shizuku remain running?** | Yes. If it stops, restart it ([§9](#9-shizuku-setup)). |
| **What happens after restarting the phone?** | Shizuku stops and must be restarted. Follow the sequence below. |
| **Can I use Instagram manually while automation runs?** | **Do not switch Instagram accounts yourself.** The script remembers which account it last opened and will not know you changed it, so later tasks could run on the wrong account. Other manual use is not confirmed — ask support. |

### After a phone restart

1. Connect to **Wi-Fi**.
2. **Start Shizuku** again ([§9, After phone restart](#after-phone-restart)) and confirm it says "Shizuku is running".
3. Open **MacroDroid** and confirm its switch is ON and Accessibility is still enabled.
4. Re-check the battery settings and re-lock Termux, MacroDroid and Shizuku in Recent Apps.
5. Start the automation ([§13](#13-first-run)).

---

## 15. Troubleshooting

Check the last message in the Termux window first: most stops print a clear reason. If the problem persists, [contact support](#16-contacting-technical-support).

### MacroDroid stops working

1. Confirm the **MacroDroid switch** is ON.
2. Check **Accessibility** is still ON for MacroDroid (*Settings → Accessibility*).
3. Set MacroDroid **and Shizuku** to **Unrestricted** in battery settings and lock them in Recent Apps.
4. Confirm **Shizuku is running**.
5. Restart the automation ([§14](#14-daily-use)).

### Termux stops / closes in background

- **Symptom:** the Termux window is gone or the script stopped without an error.
- **Check:** battery optimization for Termux is **Unrestricted**, and Termux is **locked in Recent Apps**. Do not swipe it away.
- **Fix:** reopen Termux and restart the automation. Very low-end hardware is known to kill background tasks ([§4](#4-hardware-requirements)).

### Shizuku is not running

1. Connect to **Wi-Fi** and make sure **Wireless debugging** is ON.
2. Open Shizuku and tap **Start**.
3. If it will not start (or says "Searching for wireless debugging service"), switch Wireless debugging **OFF and ON**, then tap **Start** again.
4. If it asks to pair again, repeat the pairing steps in [§9](#9-shizuku-setup).
5. Still failing? See the [Shizuku manual's FAQ](https://shizuku.rikka.app/guide/setup/), then contact support.

### Shizuku authorization disappears

1. Restart Shizuku ([§9](#9-shizuku-setup)) — authorization requests only work while Shizuku is running.
2. Re-allow any Shizuku request that appears.
3. If it keeps happening, contact support with your phone model and Android version. Shizuku's manual notes that some manufacturers modify Android in ways that stop Shizuku from working properly.

### Accessibility permission turns off

Android occasionally revokes Accessibility permission for security, especially if an app is not actively opened. Re-enable it in **Settings → Accessibility → MacroDroid**, then restart the automation.

### Instagram opens the wrong page

Check the documented requirements, in this order:

1. **600 dp exactly** — fixed coordinates tap the wrong place if it is even slightly off ([§5.1](#51-screen-scaling---600-dp)).
2. **Instagram and Chrome are in English** ([§5.2](#52-language-requirements)).
3. Links open in the **Instagram app** (see the next item).
4. The correct account is active (do not switch accounts manually while it runs).

Still wrong? Send a screen recording to support.

### Instagram link cannot be opened

- Make sure your default browser / link-handling settings route Instagram links straight into the **Instagram app** (usually *Settings → Apps → Instagram → Open by default*).
- Confirm the account is logged in and you have an internet connection.
- Confirm Chrome is in English.

### Captcha fails

| Situation | Behavior in v1.0 |
| :--- | :--- |
| Captcha-solving service unreachable | The request is retried up to **3 times**, 3 seconds apart (`Server error (Attempt n/3)`). |
| The bot answers **"verification failed"** | Termux prints `Verification Failed!` and the script **stops immediately**. There is **no** built-in retry or cooldown. |
| License rejected while solving | The license error is printed and the script stops. |

**What to do:**

1. **Restart** the automation ([§14](#14-daily-use)).
2. Check **600 dp is exactly right** — the most common cause of repeated failures — and that the language settings are correct.
3. Check your internet connection.
4. If it keeps failing, contact support with a **screen recording** and a screenshot of your Developer Options showing 600 dp.

### Telegram authentication fails

1. Use the **exact API ID and Hash** generated for the phone number on this device ([§12, Step 3](#step-3--generate-your-telegram-api-id--hash)).
2. Scan the **newest** QR code — it refreshes about every 30 seconds.
3. If Termux asks for your **2FA password**, enter your Telegram Two-Step Verification password.
4. On the second phone use **Settings → Devices → Link Desktop Device**.
5. Re-scan the QR code if the session has expired.
6. Check your internet connection on both phones.

### QR camera is black

On the **second phone**: *Android Settings → Apps → Telegram → Permissions → Camera → Allow*. Then open Telegram and verify the camera works before scanning.

### API ID / API Hash error

- The API ID must be **digits only**. If you see `Error: API ID must contain numbers only`, you probably pasted the Hash or an extra character. Run the install command again ([§10](#10-termux-setup)).
- Both values must come from [my.telegram.org](https://my.telegram.org) for the **same phone number** that logs in.
- If you changed your API credentials after activating your license, contact support (the license check uses your API Hash).

### License key invalid

Termux prints `License Error:` followed by a message (the default is "Invalid or Expired License").

1. Copy your key **exactly** from the chat with the developer — no extra spaces.
2. Update it with the command in [§17](#17-license--purchase).
3. Make sure you use the same API ID/Hash as during setup.
4. Still rejected? Contact support with a screenshot (hide most of the key).

### License expired

Licenses last **30 days**. Once expired, the next start prints `License Error:`; a license that expires mid-run stops the script at its next check. Renew and update your key as described in [§17](#renewal).

### Automation is running but nothing happens

Work through this checklist:

1. Does Termux show `License validated!` and `AUTOMATION STARTED SUCCESSFULLY`? If it shows an error or has exited, fix that first.
2. Does it show `No task detected`? Then the bot simply has no tasks — the script keeps checking.
3. Is the **MacroDroid switch ON**, **Accessibility ON**, and **Shizuku running**?
4. Is the phone online?
5. Is the screen at **exactly 600 dp**, with **English** in Instagram/Chrome?
6. Is every Instagram username spelled **exactly** as entered in the account list? A wrong name prints `Account switching failed (Not found / Banned)` and the task is skipped.
7. Are the tasks of a type the script skips (follow tasks, comments containing `@`)? They show `Clicking : ❌Skip`.

### Automation freezes

- Some steps wait for MacroDroid: **up to 3 minutes** for an account switch, 60 seconds for a like and 90 seconds for a comment. Wait before deciding it froze.
- `Bot didn't reply in 60s! Trying ONE more time...` means the bot is not answering. After a second failure the script prints `UNKNOWN ERROR: Bot server stopped responding after 2 attempts.` and stops.
- If it is truly stuck, stop and restart the automation ([§14](#14-daily-use)). If it repeats, send support your Termux screenshot.

### Phone restarted

Follow [After a phone restart](#after-a-phone-restart): Wi-Fi → restart **Shizuku** → check MacroDroid and Accessibility → re-lock apps → start the automation.

### Problem started after an update

1. Note what changed (Android, MacroDroid, Instagram, Chrome, Telegram, Termux, Shizuku) and when.
2. Re-check the settings that updates can disturb: **600 dp**, **English** language settings, **Accessibility**, battery settings and Recent Apps locks.
3. Make sure Shizuku is running.
4. If a new version of the automation file was announced, re-download the latest `Replica.mdr` and import it again ([§11](#11-macrodroid-installation)).
5. Still broken? Contact support with the details from step 1 and your current version ([§16](#16-contacting-technical-support)).

---

## 16. Contacting Technical Support

Technical support is handled **directly by the developer**.

**Support contact:** [@iamrajatroel](https://t.me/iamrajatroel) on Telegram.

### Before contacting support, prepare

- Phone manufacturer and exact model
- Android version
- 32-bit or 64-bit architecture ([§3](#3-32-bit--64-bit-compatibility))
- RAM
- Screenshot or screen recording of the problem
- Exact error message
- What happened immediately before the error
- Whether the problem happens every time or occasionally
- MacroDroid log, if requested
- Termux log, if requested
- Current automation/app version
- A screenshot of Developer Options showing your screen is set to **600 dp**

Copy this template into your message:

```text
Phone (brand + model):
Android version:
Architecture (32-bit / 64-bit):
RAM:
Automation version: v1.0
What happened (and what happened just before):
Every time or occasionally:
Exact error message:
Attached: screenshot/screen recording + Developer Options screenshot (600 dp)
```

> [!TIP]
> Your license key and API Hash can be visible in Termux screenshots. Hide them if you share a screenshot anywhere public, and never send your session file (`userbot.session`) to anyone.

---

## 17. License & Purchase

**Price:** $10 USDT / device / 30 days

| Package | Validity | Price |
| :--- | :--- | :--- |
| **Pro (1 Device)** | 30 Days | **$10 USDT** |

> [!CAUTION]
> Sharing your license key with another user is prohibited and will result in a **permanent system ban** and loss of access for your devices. Keep your key private. The current version sends your API Hash to the license server as the device identifier, so keep using the same API ID/Hash; if you need to change them, contact support first.

### Before purchasing

Confirm that your device meets the [compatibility requirements](#2-compatibility-requirements) and complete the [Before You Buy checklist](#20-before-you-buy---final-checklist).

### Purchase

**Accepted crypto: USDT on the TON network**

```text
UQBk7Dto--IPECy0br6vPDN9YbIBu-T2xdYtqia3ob4DdOOP
```

Copy the address above and make sure you send **USDT-TON only**. Sending tokens from other networks (such as TRC-20 or ERC-20) to this address will result in the **permanent loss of your funds**.

1. **Before sending any payment, contact [@iamrajatroel](https://t.me/iamrajatroel).** Wait for the developer's confirmation.
2. Send the exact plan amount to the payment address above.
3. Take a clear screenshot of the completed transaction receipt.
4. Send the screenshot to [@iamrajatroel](https://t.me/iamrajatroel) on Telegram.
5. Your unique license key and its information will be delivered to your chat within **5 minutes**.

### Activation

Enter the key when the Termux setup wizard asks for it ([§10](#10-termux-setup)). The license is verified online every time the automation starts.

### Renewal

To renew an expired license or apply a new key, you do **not** need to reinstall:

1. Contact the developer to renew and receive your new key.
2. Copy this command into Termux and press **Enter**:

   ```bash
   curl -sL -o license.py https://raw.githubusercontent.com/rajatroel/bot-files/main/license.py && python license.py && rm license.py
   ```

3. It shows your current key. Paste your **new license key** at `Enter your License Key:` and press **Enter**.
4. You should see `License Key successfully updated!` — then restart the automation.

If it prints `Error: config.json not found! Please ensure your setup is complete first.`, the initial setup ([§10](#10-termux-setup)) was not completed.

---

## 18. Updates & Changelog

**Current version:** v1.0

### v1.0

- **Added:** Instagram Like and Comment task automation for @SmmKingdomTasksBot; switching between multiple Instagram accounts; AI-assisted captcha solving; online license verification; one-time Telegram QR login.
- **Changed:** Not applicable (first release).
- **Fixed:** Not applicable (first release).
- **Known issues:** See [§19](#19-known-issues).
- **Does this update require reinstalling?** Not applicable (first release).
- **Do existing users need to change settings?** Not applicable (first release).

---

## 19. Known Issues

| Issue | Affected configuration | Workaround | Status |
| :--- | :--- | :--- | :--- |
| Requires exactly 600 dp (fixed coordinates); shrinks the whole interface | All devices | Set 600 dp ([§5.1](#51-screen-scaling---600-dp)); restore your original value when not using the automation | Limitation |
| English required in Chrome, Instagram and the bot | All devices | Set the languages ([§5.2](#52-language-requirements)) | Limitation |
| Android 10 and below not supported | Android 10 and below | None | Limitation |
| Non-standard custom ROMs untested | Custom ROMs | None | Untested |
| Very low-end hardware: instability / background task killing | Low-end devices | None | Limitation |
| Shizuku must be restarted after every phone restart | All non-rooted devices | Restart it ([§9](#after-phone-restart)) | Limitation (Android / Shizuku) |
| Script stops on license error, failed captcha verification or an unresponsive bot, and does not restart itself | All devices | Fix the cause and restart ([§14](#14-daily-use)) | Limitation |
| Follow tasks and comments containing `@` are skipped | All devices | None | Limitation |

---

## 20. Before You Buy - Final Checklist

- [ ] My Android version is supported.
- [ ] My device architecture is supported.
- [ ] My device meets the hardware requirements.
- [ ] I understand the current **600 dp** requirement.
- [ ] I understand the current **language requirements**.
- [ ] I understand that **MacroDroid, Termux and Shizuku** are required for the current version.
- [ ] I understand the required permissions/system changes.
- [ ] I have read the known limitations.
- [ ] I know how to contact technical support.

> [!WARNING]
> If you cannot confirm **every** point, contact [support](https://t.me/iamrajatroel) **BEFORE purchasing**.

---

## 21. Future Dedicated App

A standalone application is planned and would be developed separately from the current MacroDroid version. Its goal is to reduce manual configuration, improve screen/DPI adaptability and provide broader language support.

> [!IMPORTANT]
> The standalone app is **not part of v1.0**, and this guide does not promise a release date or feature list. Base your purchase decision on the **CURRENT** compatibility and features documented above.
