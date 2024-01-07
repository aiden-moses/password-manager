import functions
import time

while True:
    # Login Loop
    while True:
        selection = functions.login_menu_function()
        if selection == "1":
            funct = functions.login_function()
            if funct == "error":
                functions.clear_function()
                print("Error: You have not registered yet.")
                time.sleep(2)
            else:
                username = funct
                break
        elif selection == "2":
            funct = functions.register_function()
            if funct == "error":
                functions.clear_function()
                print("Error: Username already registered.")
                time.sleep(2)
            else:
                pass
        elif selection == "3":
            functions.exit_function()
    # Main Menu Loop
    while True:
        selection = functions.main_menu_function()
        cipher = functions.security_init_function(username)
        if selection == "1":
            functions.view_logins_function(username, cipher)
        elif selection == "2":
            functions.new_login_function(cipher, username)
        elif selection == "3":
            functions.exit_function()
