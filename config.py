import json
import os
import sys

def clear_screen():
    # Clears the terminal screen for a clean setup UI
    os.system('clear' if os.name == 'posix' else 'cls')

clear_screen()
print("\n" + "-"*42)
print("AUTO-CONFIG MAKER")
print("-"*42)
print("Let's set up your bot configuration.")
print("Please enter your details carefully.")
print("-"*42)

try:
    # 1. Get API Credentials & License Key
    api_id_input = input("\nEnter your Telegram API ID : \n").strip()
    if not api_id_input.isdigit():
        print("\nError: API ID must contain numbers only. Please run the setup again.")
        sys.exit(1)
    api_id = int(api_id_input)
    
    api_hash = input("\nEnter your Telegram API HASH : \n").strip()
    if not api_hash:
        print("\nError: API HASH cannot be empty.")
        sys.exit(1)

    license_key = input("\nEnter your Automation License Key : \n").strip()
    if not license_key:
        print("\nError: License Key cannot be empty.")
        sys.exit(1)

    # 2. Get Accounts Dynamically
    accounts = []
    print("\n" + "-"*42)
    print("ACCOUNT SETUP")
    print("-"*42)
    print("Enter your Instagram usernames one by one.")
    print("Press ENTER after each name.")
    print("When you are done, just press ENTER on an empty line to finish.\n")
    print("NOTE : Check your all account name spelling carefully before submitting!")
    print("-"*42)
    count = 1
    while True:
        raw_username = input(f"\nAccount {count}: ").strip()
        
        # If the user just presses Enter, break the loop and finish
        if not raw_username:
            if len(accounts) == 0:
                print("Error: You must enter at least one account. Try again.")
                continue
            break
            
        # STRIP LOGIC: Remove the '@' if the user included it
        clean_username = raw_username[1:] if raw_username.startswith("@") else raw_username
            
        # Set both username and display_name to be exactly the same
        accounts.append({
            "username": clean_username,
            "display_name": clean_username
        })
        count += 1

    # 3. Build the final JSON structure
    config_data = {
        "api_id": api_id,
        "api_hash": api_hash,
        "license_key": license_key,
        "accounts": accounts
    }

    # 4. Save to the main Termux directory
    config_path = os.path.expanduser('~/config.json')
    with open(config_path, 'w') as f:
        json.dump(config_data, f, indent=4)

    print("\n" + "-"*42)
    print("CONFIGURATION SAVED SUCCESSFULLY!")
    print("-"*42 + "\n")
    print("You can now run 'python bot.py' to start the automation.\n")

except KeyboardInterrupt:
    print("\n\nSetup cancelled by user. No files were saved.")
    sys.exit(1)
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    sys.exit(1)
    print("\n" + "-"*42)
    print("CONFIGURATION SAVED SUCCESSFULLY!")
    print("-"*42 + "\n")
    print("You can now run the main bot installation command.\n")

except KeyboardInterrupt:
    print("\n\nSetup cancelled by user. No files were saved.")
    sys.exit(1)
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
    sys.exit(1)
