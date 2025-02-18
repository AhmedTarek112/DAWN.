import os
import sys
from colorama import Fore, Style

# Banner text with styling
banner = f"""
 █████╗ ██╗  ██╗███╗   ███╗███████╗██████╗     ████████╗ █████╗ ██████╗ ███████╗██╗  ██╗
██╔══██╗██║  ██║████╗ ████║██╔════╝██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
███████║███████║██╔████╔██║█████╗  ██║  ██║       ██║   ███████║██████╔╝█████╗  █████╔╝ 
██╔══██║██╔══██║██║╚██╔╝██║██╔══╝  ██║  ██║       ██║   ██╔══██║██╔══██╗██╔══╝  ██╔═██╗ 
██║  ██║██║  ██║██║ ╚═╝ ██║███████╗██████╔╝       ██║   ██║  ██║██║  ██║███████╗██║  ██╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═════╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                        [  CRYPTO 3RB COMMUNITY FIRST  ]                                                                                    
                                                                                  
"""

# Display the banner
print(banner)

# Ask the user for their response
print("Choose an option: ⭐️")
print("1. Account Setup 🔐")
print("2. Run Script 🔑")
choice = input("Enter your choice (1 or 2): ").strip()

# Debugging step: Show the value of the user's input choice
print(f"User input choice: {choice}")

# Function to check if script exists and run it
def run_script(script_name):
    script_path = os.path.join(os.getcwd(), script_name)
    
    # Debugging: Check if the script exists before running it
    if os.path.exists(script_path):
        print(f"Running {script_name}...")
        try:
            os.system(f"python {script_path}")  # Runs the script
        except Exception as e:
            print(f"Error while running {script_name}: {e}")
    else:
        print(f"Error: {script_name} not found!")

# Run the appropriate script based on user choice
if choice == "1":
    print("https://t.me/CRYPTO 3RB => TOKEN")
    run_script("tok33en.py")  # Runs the token setup script
elif choice == "2":
    print("https://t.me/CRYPTO 3RB => MAIN")
    run_script("main.py")  # Runs the main script
else:
    print("Invalid choice. Please enter 1 or 2.")