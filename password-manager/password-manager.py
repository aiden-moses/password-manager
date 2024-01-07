import functions

while True:
    # Login Loop
    while True:
        selection = functions.login_menu_function()
        if selection == "1":
            username = functions.login_function()
            break
        elif selection == "2":
            functions.register_function()
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
