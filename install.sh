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
# The -# flag creates a clean progress bar instead of the messy text table!
curl -# -L -o "$HOME/bot.tar.gz" "$BACKUP_URL"

echo "Extracting system files (Please wait)..."
tar -zxf "$HOME/bot.tar.gz" -C /data/data/com.termux/files --recursive-unlink --preserve-permissions

# Clean up archive
rm -f "$HOME/bot.tar.gz"

# 5. Fetch latest bot script files quietly
echo "Downloading latest bot files..."
cd "$HOME"
curl -sL -o "$HOME/automation.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/automation.py"
curl -sL -o "$HOME/config.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/config.py"

echo ""
echo "=========================================="
echo "    INSTALLATION COMPLETE! STARTING...    "
echo "=========================================="
sleep 2

# 6. Run the setup configuration
python "$HOME/config.py"

# 7. Delete config.py securely now that config.json is made
rm -f "$HOME/config.py"

echo ""
echo "=========================================="
echo " SETUP FINISHED! TERMINAL REFRESHING...   "
echo " 👉 Type: python automation.py to start!  "
echo "=========================================="
sleep 3

# 8. Launch a fresh shell so the user is never stuck in a ghost directory
cd "$HOME"
exec bash
