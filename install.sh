#!/bin/bash
set -e

clear
echo "========================================"
echo "SETTING UP PERMISSIONS"
echo "========================================"
echo ""

# 1. Storage Permission Loop 
while ! ls ~/storage/shared >/dev/null 2>&1; do
    echo "Storage permission is required"
    echo "to install the automation."
    echo ""
    echo "Press [ENTER] to open the"
    read -r -p "permission window..."

    clear
    echo "========================================"
    echo "SETTING UP PERMISSIONS"
    echo "========================================"
    echo ""

    termux-setup-storage
    
    sleep 2
    
    echo "Please press [ENTER] one more"
    read -r -p "time to continue..."

    clear
    echo "========================================"
    echo "SETTING UP PERMISSIONS"
    echo "========================================"
    echo ""
    
    # If it fails to read storage after pressing Enter, ask again
    if ! ls ~/storage/shared >/dev/null 2>&1; then
        echo "Storage permission not detected!"
        echo "You MUST allow storage access"
        echo "to install the bot."
        echo "Let's try again..."
        echo ""
    fi
done

clear

echo "========================================"
echo "DOWNLOADING FILES"
echo "========================================"
echo ""

# 3. Download backup with clean percentage display
BACKUP_URL="https://github.com/rajatroel/bot-files/releases/download/v1.0/bot.tar.gz"

curl -# -L -o "$HOME/bot.tar.gz" "$BACKUP_URL" 2>&1 | while IFS= read -r -d $'\r' line; do
    pct="${line##* }"
    if [[ "$pct" == *%* ]]; then
        printf "\rDownloading environment : %-7s" "$pct"
    fi
done
printf "\rDownloading environment : 100.0%% Done!\n"

echo ""
echo "Extracting system files"
echo "(Please wait)..."
echo ""
tar -zxf "$HOME/bot.tar.gz" -C /data/data/com.termux/files --recursive-unlink --preserve-permissions

# Clean up archive
rm -f "$HOME/bot.tar.gz"

# 4. Fetch latest bot script files quietly
echo "Starting initial setup..."
cd "$HOME"
curl -sL -o "$HOME/automation.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/automation.py"
curl -sL -o "$HOME/config.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/config.py"

# 5. Run the setup configuration
python "$HOME/config.py"

# 6. Delete config.py securely once configured
rm -f "$HOME/config.py"

# 7. Acquire wakelock to prevent Android from killing Termux in the background
echo "Acquiring wakelock..."
termux-wake-lock

# 8. Add automation.py to .bashrc so it runs on every fresh Termux launch
echo "Configuring auto-start..."
if ! grep -q "python automation.py" "$HOME/.bashrc" 2>/dev/null; then
    echo "python automation.py" >> "$HOME/.bashrc"
fi

cd "$HOME"
exec bash
