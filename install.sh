#!/bin/bash
set -e

# 1. Acquire wake lock immediately
termux-wake-lock

# 2. Persist wake lock in ~/.bashrc
if ! grep -q "termux-wake-lock" ~/.bashrc 2>/dev/null; then
    echo "termux-wake-lock" >> ~/.bashrc
fi

clear
echo "=========================================="
echo "    INSTAGRAM BOT - AUTO INSTALLER        "
echo "=========================================="
echo ""

echo "To ensure the bot never crashes in the background,"
echo "please grant the requested permissions."
echo ""
read -p "Press [ENTER] to start..."

echo ""
echo "[1/2] Requesting Storage Permission..."
if [ ! -d "~/storage" ]; then
    termux-setup-storage
    sleep 2
fi

echo "[2/2] Opening Battery Optimization Settings..."
echo "👉 PLEASE SET TERMUX TO 'UNRESTRICTED'!"
sleep 3
am start -a android.settings.IGNORE_BATTERY_OPTIMIZATION_SETTINGS > /dev/null 2>&1 || true

echo ""
read -p "Press [ENTER] only AFTER you have set battery to Unrestricted..."

# ==========================================
# ROBUST INSTALLATION (FIXED DPKG PARSING)
# ==========================================
clear
echo "=========================================="
echo "    SETTING UP PACKAGES & DEPENDENCIES    "
echo "=========================================="
echo ""

# Set non-interactive environment variables globally to suppress ALL prompts
export DEBIAN_FRONTEND=noninteractive
export APT_LISTCHANGES_FRONTEND=none

# Clean pip cache
rm -rf ~/.cache/pip

# Update repositories safely using apt-get with proper configuration options
apt-get update -y
apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" x11-repo tur-repo || true

apt-get update -y
apt-get upgrade -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" || true

# Install all required system packages cleanly via apt-get to prevent option-splitting bugs
apt-get install -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" \
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

# Setup compilation targets and install Python modules
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
python config.py    print(f'Downloading {f}...')
    urllib.request.urlretrieve(base + f, f)
"

echo ""
echo "=========================================="
echo "    INSTALLATION COMPLETE! STARTING SETUP "
echo "=========================================="
sleep 2

# Launch the interactive configuration maker
python config.py
