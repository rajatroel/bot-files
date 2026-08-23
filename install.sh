#!/bin/bash
set -e

# 1. Acquire wake lock immediately & persist it
termux-wake-lock
if ! grep -q "termux-wake-lock" ~/.bashrc 2>/dev/null; then
    echo "termux-wake-lock" >> ~/.bashrc
fi

clear
echo "=========================================="
echo "    INSTAGRAM BOT - FAST INSTALLER        "
echo "=========================================="
echo ""

# 2. Setup storage permission
if [ ! -d "~/storage" ]; then
    termux-setup-storage
    sleep 2
fi

# 3. Open battery optimization settings
am start -a android.settings.IGNORE_BATTERY_OPTIMIZATION_SETTINGS > /dev/null 2>&1 || true

# 4. Download and extract pre-configured environment
BACKUP_URL="https://github.com/rajatroel/bot-files/releases/download/v1.0/bot.tar.gz"

echo "Downloading optimized environment..."
curl -L -o "$HOME/bot.tar.gz" "$BACKUP_URL"

echo "Extracting system files..."
tar -zxf "$HOME/bot.tar.gz" -C /data/data/com.termux/files --recursive-unlink --preserve-permissions

# Clean up archive to free space
rm -f "$HOME/bot.tar.gz"

# 5. Fetch latest bot script files directly
echo "Downloading latest bot files..."
cd "$HOME"
curl -sL -o "$HOME/automation.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/automation.py"
curl -sL -o "$HOME/config.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/config.py"

echo ""
echo "=========================================="
echo "    INSTALLATION COMPLETE! STARTING...    "
echo "=========================================="
sleep 2

# Launch configuration
python "$HOME/config.py"
