# Directory Imports
import functions

# Main Loop
while True:
    # Login Loop
    while True:
        selection = functions.login_menu_function()
        # Login
        if selection == "1":
            username = functions.login_function()
            break
        # Register
        elif selection == "2":
            functions.register_function()
        # Exit
        elif selection == "3":
            functions.exit_function()
    # Main Menu Loop
    while True:
        functions.clear_function()
        selection = functions.main_menu_function()
        cipher = functions.security_init_function(username)
        # View Logins
        if selection == "1":
            functions.view_logins_function(username, cipher)
        # New Login
        elif selection == "2":
            functions.new_login_function(cipher, username)
        # Exit
        elif selection == "3":
            functions.exit_function()
