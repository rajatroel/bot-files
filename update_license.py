import json
import os
import sys

config_path = os.path.expanduser('~/config.json')

if not os.path.exists(config_path):
    print("❌ Error: config.json not found! Please ensure your setup is complete first.")
    sys.exit(1)

try:
    # Load the existing configuration
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    print(f"Current License: {config.get('license_key', 'None')}")
    
    # Prompt the user for the new key
    new_key = input("\nEnter your new License Key: ").strip()
    
    if not new_key:
        print("❌ No key entered. Update cancelled.")
        sys.exit(0)
        
    # Update the key and save the file
    config["license_key"] = new_key
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
        
    print("\n✅ License Key successfully updated! You can now start the bot.")
    
except Exception as e:
    print(f"\n❌ Failed to update config: {e}")
  
