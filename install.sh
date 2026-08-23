#!/bin/bash
set -e

clear
echo "=========================================="
echo "    ⚠️ PERMISSION SETUP REQUIRED ⚠️       "
echo "=========================================="
echo ""
echo "To ensure the bot never crashes in the background,"
echo "you must grant 3 permissions right now:"
echo ""
echo "1. NOTIFICATIONS (For CPU Wake Lock)"
echo "2. STORAGE (To read and send screenshots)"
echo "3. BATTERY OPTIMIZATION (To prevent Android killing the bot)"
echo ""
echo "Please click 'ALLOW' on any popups that appear next."
echo ""
read -p "Press [ENTER] to start granting permissions..."

echo ""
echo "[1/3] Requesting Wake Lock & Notification Permission..."
# This triggers the Android 13+ Notification prompt
termux-wake-lock
sleep 2

echo "[2/3] Requesting Storage Permission..."
# This triggers the Storage access prompt if not already granted
if [ ! -d "~/storage" ]; then
    termux-setup-storage
    sleep 3
fi

echo "[3/3] Opening Battery Optimization Settings..."
echo "👉 PLEASE FIND 'TERMUX' AND SET IT TO 'UNRESTRICTED' OR 'NO RESTRICTIONS'!"
sleep 4
# This forces the phone's Settings app to open to the Battery page
am start -a android.settings.IGNORE_BATTERY_OPTIMIZATION_SETTINGS > /dev/null 2>&1 || true

echo ""
read -p "Press [ENTER] only AFTER you have set the battery to Unrestricted..."

# Permanently inject the wake lock so it activates automatically on future runs
if ! grep -q "termux-wake-lock" ~/.bashrc 2>/dev/null; then
    echo "termux-wake-lock" >> ~/.bashrc
fi

# ==========================================
# BEGIN MAIN INSTALLATION
# ==========================================
clear
echo "=========================================="
echo "    INSTAGRAM BOT - AUTO INSTALLER        "
echo "=========================================="
echo ""

# Prevent any interactive prompts from pausing the script
export DEBIAN_FRONTEND=noninteractive
DPKG_OPTS='-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"'

echo "[1/4] Configuring repositories..."
rm -rf ~/.cache/pip
pkg install x11-repo tur-repo -y $DPKG_OPTS
pkg update -y $DPKG_OPTS
pkg upgrade -y $DPKG_OPTS

echo ""
echo "[2/4] Installing system dependencies & packages (This may take a few minutes)..."
pkg install -y $DPKG_OPTS \
    python \
    android-tools \
    nano \
    rust \
    clang \
    make \
    pkg-config \
    libffi \
    openssl \
    dbus \
    libxml2 \
    libxslt \
    python-numpy \
    python-pillow \
    opencv-python \
    python-lxml \
    termux-api \
    curl

echo ""
echo "[3/4] Installing Python modules..."
export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)"
export CARGO_BUILD_TARGET=aarch64-linux-android
python -m pip install --upgrade pip setuptools wheel maturin
pip install pyrogram tgcrypto aiohttp requests

echo ""
echo "[4/4] Downloading latest bot files..."
curl -sL -o automation.py https://raw.githubusercontent.com/rajatroel/bot-files/main/automation.py
curl -sL -o config.py https://raw.githubusercontent.com/rajatroel/bot-files/main/config.py

echo ""
echo "=========================================="
echo "    INSTALLATION COMPLETE! STARTING SETUP "
echo "=========================================="
sleep 2

# Launch the interactive configuration maker
python config.py
