# Directory Imports
import functions

# Main Loop
while True:
    # Login Loop
    while True:
        selection = functions.login_menu_function()
        # Login
        if selection == "1":
            print("Login.")
            break
        # Register
        elif selection == "2":
            functions.register_function()
            break
        # Exit
        elif selection == "3":
            functions.exit_function()
    break
