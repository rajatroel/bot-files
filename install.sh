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
# BEGIN MAIN INSTALLATION & REPAIR FIX
# ==========================================
clear
echo "=========================================="
echo "    SETTING UP PACKAGES & DEPENDENCIES    "
echo "=========================================="
echo ""

# Prevent any interactive prompts from pausing the script
export DEBIAN_FRONTEND=noninteractive
DPKG_OPTS='-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"'

# FIX: Repair broken links or mismatched package symbols for curl/openssl first
echo "[0/4] Synchronizing package states..."
apt update -y
apt install -y openssl libngtcp2 libcurl curl ca-certificates --reinstall || true

# 1. Clean cache and update package lists safely
echo "[1/4] Updating package lists..."
rm -rf ~/.cache/pip
pkg install x11-repo tur-repo -y $DPKG_OPTS
pkg update -y $DPKG_OPTS

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
