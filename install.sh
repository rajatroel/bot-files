#!/bin/bash
set -e

clear
echo "========================================"
echo "SETTING UP PERMISSIONS"
echo "========================================"
echo ""

# 1. Storage Permission Auto-Detect Loop
while [ ! -d "$HOME/storage/shared" ]; do
    echo "Storage permission is required"
    echo "to install the automation."
    
    # Fire the Android permission popup
    termux-setup-storage
    
    echo -n "Waiting for you to click 'Allow'"
    
    # Check automatically every 1 second (up to 15 seconds)
    for i in {1..7}; do
        if [ -d "$HOME/storage/shared" ]; then
            break # Instantly break the timer if granted!
        fi
        echo -n "."
        sleep 1
    done
    
    echo "" # Print a new line after the dots
    
    # If the folder still isn't readable, they likely clicked Deny
    if [ ! -d "$HOME/storage/shared" ]; then
        echo ""
        echo "Storage permission not detected!"
        echo "If you clicked 'Deny', we must try again."
        echo "========================================"
        sleep 2
    fi
done

echo "Storage permission granted!"
sleep 1
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
cd "$HOME"
curl -sL -o "$HOME/automation.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/automation.py"
curl -sL -o "$HOME/config.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/config.py"

# 5. Run the setup configuration
python "$HOME/config.py" </dev/tty

# 6. Delete config.py securely once configured
rm -f "$HOME/config.py"

# 7. Add wake lock and automation.py to .bashrc so they run on every fresh Termux launch
if ! grep -q "termux-wake-lock" "$HOME/.bashrc" 2>/dev/null; then
    echo "termux-wake-lock" >> "$HOME/.bashrc"
fi

if ! grep -q "python automation.py" "$HOME/.bashrc" 2>/dev/null; then
    echo "python automation.py" >> "$HOME/.bashrc"
fi

cd "$HOME"
exec bash
