import json
import os
import sys

def clear_screen():
    # Clears the terminal screen for a clean setup UI
    os.system('clear' if os.name == 'posix' else 'cls')

clear_screen()
print("\n" + "="*42)
print("       CREATE YOUR CONFIG")
print("="*42)
print("Let's set up your bot configuration.")
print("Please enter your details carefully.")
print("-"*42)

try:
    # 1. Get License Key
    license_key = input("\nEnter your Automation License Key: \n").strip()
    while not license_key:
        print("\nError: License Key cannot be empty.")
        license_key = input("Enter your Automation License Key: \n").strip()

    # 2. Get Accounts Dynamically
    accounts = []
    print("\n" + "-"*42)
    print("ACCOUNT SETUP")
    print("-"*42)
    print("Enter your Instagram usernames one by one.")
    print("Press ENTER after each name.")
    print("When you are done, just press ENTER on an empty line to finish.\n")
    print("NOTE: Check all account names carefully before submitting!")
    print("-"*42)
    
    count = 1
    while True:
        raw_username = input(f"\nAccount {count}: ").strip()
        
        # If the user presses Enter on an empty prompt, finish input
        if not raw_username:
            if len(accounts) == 0:
                print("Error: You must enter at least one account. Try again.")
                continue
            break
            
        # Strip '@' prefix if entered
        clean_username = raw_username[1:] if raw_username.startswith("@") else raw_username
            
        # Set username and display_name
        accounts.append({
            "username": clean_username,
            "display_name": clean_username
        })
        count += 1

    # 3. Build the final JSON structure (Cleaned of API keys)
    config_data = {
        "license_key": license_key,
        "accounts": accounts
    }

    # 4. Save to ~/config.json
    config_path = os.path.expanduser('~/config.json')
    with open(config_path, 'w') as f:
        json.dump(config_data, f, indent=4)

    print("\n" + "="*42)
    print("     ALL DONE SUCCESSFULLY!")
    print("="*42)
    print(f"Saved {len(accounts)} account(s) to config.json.")
    print("You can now run: python automation_3.py\n")

except KeyboardInterrupt:
    print("\n\nSetup cancelled by user. No files were saved.\n")
    sys.exit(1)
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}\n")
    sys.exit(1)
