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
                break
        # Register
        elif selection == "2":
            functions.register_function()
        # Exit
        elif selection == "3":
            functions.exit_function()
    # Main Menu Loop
    while True:
        selection = functions.main_menu_function()
        # View Logins
        if selection == "1":
            print("View Logins")
            time.sleep(2)
        # New Login
        elif selection == "2":
            print("New Login")
            time.sleep(2)
            functions.exit_function
        # Exit
        elif selection == "3":
            functions.exit_function()
