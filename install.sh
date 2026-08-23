#!/bin/bash
set -e

# 1. Acquire wake lock immediately for the installation process
termux-wake-lock

# 2. Persist wake lock in ~/.bashrc so every future Termux session stays awake
if ! grep -q "termux-wake-lock" ~/.bashrc 2>/dev/null; then
    echo "termux-wake-lock" >> ~/.bashrc
fi

# Clear the screen
clear
echo "=========================================="
echo "    INSTAGRAM BOT - AUTO INSTALLER        "
echo "=========================================="
echo ""

echo "To ensure the bot never crashes in the background,"
echo "please grant the requested permissions on your phone."
echo ""
read -p "Press [ENTER] to start..."

echo ""
echo "[1/2] Requesting Storage Permission..."
if [ ! -d "~/storage" ]; then
    termux-setup-storage
    sleep 2
fi

echo "[2/2] Opening Battery Optimization Settings..."
echo "👉 PLEASE SET TERMUX TO 'UNRESTRICTED' OR 'NO RESTRICTIONS'!"
sleep 3
am start -a android.settings.IGNORE_BATTERY_OPTIMIZATION_SETTINGS > /dev/null 2>&1 || true

echo ""
read -p "Press [ENTER] only AFTER you have set the battery to Unrestricted..."

# ==========================================
# STREAMLINED INSTALLATION (NO REPO PACKAGES)
# ==========================================
clear
echo "=========================================="
echo "    SETTING UP PACKAGES & DEPENDENCIES    "
echo "=========================================="
echo ""

# Update package lists safely
echo "[1/3] Updating package lists..."
rm -rf ~/.cache/pip
pkg update -y

echo ""
echo "[2/3] Installing system dependencies & Python..."
pkg install -y \
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
    termux-api

echo ""
echo "[3/3] Installing Python modules..."
export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)"
export CARGO_BUILD_TARGET=aarch64-linux-android
python -m pip install --upgrade pip setuptools wheel maturin
pip install pyrogram tgcrypto aiohttp requests

echo ""
echo "Downloading latest bot files..."
python3 -c "
import urllib.request
base = 'https://raw.githubusercontent.com/rajatroel/bot-files/main/'
for f in ['automation.py', 'config.py']:
    print(f'Downloading {f}...')
    urllib.request.urlretrieve(base + f, f)
"

echo ""
echo "=========================================="
echo "    INSTALLATION COMPLETE! STARTING SETUP "
echo "=========================================="
sleep 2

# Launch the interactive configuration maker
python config.py
