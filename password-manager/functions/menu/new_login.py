# Imports
import functions
import os
import json


def new_login_function(cipher, username):
    directory = f'data/{username}/'
    file_name = 'data.json'
    file_directory = directory + file_name
    functions.clear_function()
    while True:
        # Get Input
        print("Application/Website:")
        app = input("\n>> ")
        print("\nUsername:")
        user = input("\n>> ")
        print("\nPassword:")
        password = input("\n>> ")
        # Verify Input
        functions.clear_function()
        while True:
            print("Does this information look correct?")
            print(f"Application/Website: '{app}'")
            print(f"Username: '{user}'")
            print(f"Password: {password}")
            selection = input("\nY/n >> ")
            if selection == "y" or selection == "Y" or not selection:
                functions.clear_function()
                break
            elif selection == "n" or selection == "N":
                functions.clear_function()
            else:
                functions.clear_function()
                print("Error: Please enter a valid input.")
        break
    if not os.path.exists(file_directory):
        data = []
    else:
        try:
            with open(file_directory, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []
    encrypted_password = functions.encrypt_function(cipher, password)
    data_entry = {'application': app, 'username': user, 'encrypted_password': encrypted_password} # noqa
    data.append(data_entry)
    try:
        with open(file_directory, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        with open(file_directory, 'x') as file:
            json.dump(data, file, indent=4)
