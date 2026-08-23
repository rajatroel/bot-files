#!/bin/bash
set -e

# Clear the screen
clear
echo "=========================================="
echo "    INSTAGRAM BOT - AUTO INSTALLER        "
echo "=========================================="
echo ""

# Prevent any interactive prompts from pausing the script
export DEBIAN_FRONTEND=noninteractive
DPKG_OPTS='-o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"'

# 1. Clean cache and update repositories
echo "[1/4] Configuring repositories..."
rm -rf ~/.cache/pip
pkg install x11-repo tur-repo -y $DPKG_OPTS
pkg update -y $DPKG_OPTS
pkg upgrade -y $DPKG_OPTS

# 2. Install all system dependencies and prebuilt binaries
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

# 3. Setup compile environments and install pip modules
echo ""
echo "[3/4] Installing Python modules..."
export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)"
export CARGO_BUILD_TARGET=aarch64-linux-android
python -m pip install --upgrade pip setuptools wheel maturin
pip install pyrogram tgcrypto aiohttp requests

# 4. Download latest automation & config files
echo ""
echo "[4/4] Downloading latest bot files..."
curl -sL -o automation.py https://raw.githubusercontent.com/rajatroel/bot-files/main/automation.py
curl -sL -o config.py https://raw.githubusercontent.com/rajatroel/bot-files/main/config.py

# Request storage permission if not already granted
if [ ! -d "/sdcard" ]; then
    termux-setup-storage
fi

echo ""
echo "=========================================="
echo "    INSTALLATION COMPLETE! STARTING SETUP "
echo "=========================================="
sleep 2

# Launch the interactive configuration maker
python config.py
