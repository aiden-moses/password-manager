# Directory Imports
import functions
import time

# Main Loop
while True:
    # Login Loop
    while True:
        selection = functions.login_menu_function()
        # Login
        if selection == "1":
            if functions.login_function() == "success":
                functions.clear_function()
                print("Logged in.")
                time.sleep(2)
                functions.exit_function()
        # Register
        elif selection == "2":
            functions.register_function()
        # Exit
        elif selection == "3":
            functions.exit_function()
