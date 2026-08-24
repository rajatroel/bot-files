#!/bin/bash
clear
echo "Starting Configuration Update..."

# 1. Download only the config maker
cd "$HOME"
curl -sL -o "$HOME/config.py" "https://raw.githubusercontent.com/rajatroel/bot-files/main/config.py"

# 2. Run it to overwrite config.json
python "$HOME/config.py" < /dev/tty

# 3. Clean up
rm -f "$HOME/config.py"

# 4. Ensure auto-start is still in bashrc just in case
if ! grep -q "python automation.py" "$HOME/.bashrc" 2>/dev/null; then
    echo "python automation.py" >> "$HOME/.bashrc"
fi
