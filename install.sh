#!/bin/bash
set -e

# 1. Acquire wake lock immediately & persist it
termux-wake-lock
if ! grep -q "termux-wake-lock" ~/.bashrc 2>/dev/null; then
    echo "termux-wake-lock" >> ~/.bashrc
fi

clear
echo "=========================================="
echo "SETTING UP ENVIRONMENT"
echo "=========================================="
echo ""

# 2. Setup storage permission
if [ ! -d "~/storage" ]; then
    termux-setup-storage
    sleep 2
fi

# 3. Open battery optimization settings
am start -a android.settings.IGNORE_BATTERY_OPTIMIZATION_SETTINGS > /dev/null 2>&1 || true

# 4. Download backup with clean percentage display
BACKUP_URL="https://github.com/rajatroel/bot-files/releases/download/v1.0/bot.tar.gz"

echo "Downloading optimized environment..."
curl -# -L -o "$HOME/bot.tar.gz" "$BACKUP_URL" 2>&1 | while IFS= read -r -d $'\r' line; do
    pct="${line##* }"
    if [[ "$pct" == *%* ]]; then
        printf "\rDownloading: %-7s" "$pct"
    fi
done
printf "\rDownloading: 100.0%% Done!\n"

echo ""
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

# 7. Delete config.py securely once configured
rm -f "$HOME/config.py"

echo ""
echo "=========================================="
echo " SETUP FINISHED! TERMINAL REFRESHING...   "
echo " 👉 Type: python automation.py to start!  "
echo "=========================================="
sleep 3

# 8. Launch a fresh shell in home directory
cd "$HOME"
exec bash
