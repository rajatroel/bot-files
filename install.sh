#!/bin/bash
set -e

clear
echo "=========================================="
echo "SETTING UP ENVIRONMENT"
echo "=========================================="
echo ""

# 1. Storage Permission Loop (Waits for Enter, opens popup, waits for Enter again)
while ! ls ~/storage/shared >/dev/null 2>&1; do
    echo "Storage access is required to install the bot."
    read -r -p "Press [ENTER] to open the permission popup..."
    
    termux-setup-storage
    sleep 2
    
    echo ""
    read -r -p "Please press [ENTER] one more time to continue..."
    
    # If it fails to read storage after pressing Enter, ask again
    if ! ls ~/storage/shared >/dev/null 2>&1; then
        echo ""
        echo "Storage permission not detected!"
        echo "You MUST allow storage access to install the bot."
        echo "Let's try again..."
        echo ""
    fi
done
echo "Storage access verified!"
echo ""

# 2. Open Battery Optimization Settings (Matches the same Enter -> Open -> Enter flow)
echo "Opening Battery Settings..."
echo "Set Termux to 'Unrestricted' or 'Don't Optimize'."
read -r -p "Press [ENTER] to open battery settings..."

am start -a android.settings.IGNORE_BATTERY_OPTIMIZATION_SETTINGS > /dev/null 2>&1 || true
sleep 2

echo ""
echo "Have you changed the settings and returned to Termux?"
read -r -p "Please press [ENTER] one more time to continue..."
echo ""

echo "=========================================="
echo "DOWNLOADING REQUIREMENTS"
echo "=========================================="
echo ""

# 3. Download backup with clean percentage display
BACKUP_URL="https://github.com/rajatroel/bot-files/releases/download/v1.0/bot.tar.gz"

curl -# -L -o "$HOME/bot.tar.gz" "$BACKUP_URL" 2>&1 | while IFS= read -r -d $'\r' line; do
    pct="${line##* }"
    if [[ "$pct" == *%* ]]; then
        printf "\rDownloading environment : %-7s" "$pct"
    fi
done
printf "\rDownloading environment: 100.0%% Done!\n"

echo ""
echo "Extracting system files (Please wait)..."
tar -zxf "$HOME/bot.tar.gz" -C /data/data/com.termux/files --recursive-unlink --preserve-permissions

# Clean up archive
rm -f "$HOME/bot.tar.gz"

# 4. Fetch latest bot script files quietly
echo "Fetching latest bot files..."
cd "$HOME"
curl -sL -o "$HOME/automation.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/automation.py"
curl -sL -o "$HOME/config.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/config.py"

echo ""
echo "=========================================="
echo "STARTING...    "
echo "=========================================="
sleep 2

# 5. Run the setup configuration
python "$HOME/config.py"

# 6. Delete config.py securely once configured
rm -f "$HOME/config.py"
sleep 1

# 7. Launch a fresh shell in home directory
cd "$HOME"
exec bash
