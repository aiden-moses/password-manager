import os
import json
import functions


def register_function():
    functions.clear_function()

    while True:
        entered_username = input("\nPlease enter your username.\n>> ")
        entered_password = input("\nPlease enter your password.\n>> ")

        if ' ' in entered_username or ' ' in entered_password:
            functions.clear_function()
            print("Error: Login information cannot contain spaces.")
        else:
            functions.clear_function()

            while True:
                print("Does this information look correct?\n")
                print(f"Username: '{entered_username}'")
                print(f"Password: '{entered_password}'")
                selection = input("\nY/n >> ")

                if selection == "y" or selection == "Y" or not selection:
                    break
                elif selection == "n" or selection == "N":
                    functions.clear_function()
                    print("Error: Please enter a valid input.\n")

            hashed_password = functions.hash_function(entered_password)

            user_directory = f"data/{entered_username}"
            user_data = {'username': entered_username, 'hashed_password': hashed_password} # noqa
            file_name = "user_data.json"
            file_directory = user_directory + "/" + file_name

            if os.path.exists(file_directory):
                functions.clear_function()
                return "error"
            else:
                os.mkdir(user_directory)
                with open(file_directory, 'x') as file:
                    json.dump(user_data, file)
                    return "success"
