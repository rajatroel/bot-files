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
# BEGIN MAIN INSTALLATION (NO CURL PACKAGE)
# ==========================================
clear
echo "=========================================="
echo "    SETTING UP PACKAGES & DEPENDENCIES    "
echo "=========================================="
echo ""

# Prevent any interactive prompts from pausing the script
export DEBIAN_FRONTEND=noninteractive
DPKG_OPTS='-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"'

# 1. Clean cache and update package lists safely (Skipping curl package entirely)
echo "[1/4] Updating package lists..."
rm -rf ~/.cache/pip
pkg update -y $DPKG_OPTS

# Install required repositories safely
pkg install x11-repo tur-repo -y $DPKG_OPTS

echo ""
echo "[2/4] Installing system dependencies & packages..."
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
    termux-api

echo ""
echo "[3/4] Installing Python modules..."
export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)"
export CARGO_BUILD_TARGET=aarch64-linux-android
python -m pip install --upgrade pip setuptools wheel maturin
pip install pyrogram tgcrypto aiohttp requests

echo ""
echo "[4/4] Downloading latest bot files using Python..."
# Using Python instead of curl to download files safely, bypassing any apt/curl link errors
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
