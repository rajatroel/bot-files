import json
import os
import sys

# Updated to use the direct internal storage path we set earlier
config_path = '/sdcard/config.json'

if not os.path.exists(config_path):
    print("Error: config.json not found! Please ensure your setup is complete first.")
    sys.exit(1)

try:
    # Load the existing configuration
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    print(f"Current License: {config.get('license_key', 'None')}")
    
    # Prompt the user for the new key
    new_key = input("\nEnter your License Key: ").strip()
    
    if not new_key:
        print("No key entered. Update cancelled.")
        sys.exit(0)
        
    # Update the key and save the file
    config["license_key"] = new_key
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)
        
    print("\nLicense Key successfully updated!")
    
except Exception as e:
    print(f"\nFailed to update config: {e}")
    sys.exit(1)
