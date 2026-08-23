#!/bin/bash
set -e

# 1. Acquire wake lock immediately & persist it in .bashrc
termux-wake-lock
if ! grep -q "termux-wake-lock" ~/.bashrc 2>/dev/null; then
    echo "termux-wake-lock" >> ~/.bashrc
fi

# 2. Grant permissions setup prompt
clear
echo "=========================================="
echo "    INSTAGRAM BOT - AUTO INSTALLER        "
echo "=========================================="
echo ""
echo "Please grant Storage and Battery permissions if prompted."
echo ""
read -p "Press [ENTER] to begin installation..."

if [ ! -d "~/storage" ]; then
    termux-setup-storage
    sleep 2
fi

am start -a android.settings.IGNORE_BATTERY_OPTIMIZATION_SETTINGS > /dev/null 2>&1 || true

# ==========================================
# 3. COMPLETELY SUPPRESS ALL PROMPTS & RUN EXACT COMMAND
# ==========================================
clear
echo "Running installation..."

# These environment variables force apt/dpkg to automatically choose default answers (Option 'N')
export DEBIAN_FRONTEND=noninteractive
export APT_LISTCHANGES_FRONTEND=none

# Run your exact master command line with automatic default-selection options injected
rm -rf ~/.cache/pip && \
pkg install x11-repo tur-repo -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" && \
pkg update -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" && \
pkg upgrade -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" && \
pkg install python android-tools nano rust clang make pkg-config libffi openssl dbus libxml2 libxslt python-numpy python-pillow opencv-python python-lxml -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" && \
export ANDROID_API_LEVEL="$(getprop ro.build.version.sdk)" && \
export CARGO_BUILD_TARGET=aarch64-linux-android && \
python -m pip install --upgrade pip setuptools wheel maturin && \
pip install pyrogram tgcrypto aiohttp requests

# 4. Download latest bot files and launch configuration
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

python config.py
