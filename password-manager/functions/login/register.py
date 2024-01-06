# Imports
import os
import json
import time
import functions


def register_function():
    # Clear Screen
    functions.clear_function()

    while True:
        # Request Information
        entered_username = input("\nPlease enter your username.\n>> ")
        entered_password = input("\nPlease enter your password.\n>> ")
        # Check For Spaces
        if ' ' in entered_username or ' ' in entered_password:
            functions.clear_function()
            print("Error: Login information cannot contain spaces.")
        else:
            # Clear Screen:
            functions.clear_function()

            while True:
                # Verify Desired Input
                print("Does this information look correct?\n")
                print(f"Username: '{entered_username}'")
                print(f"Password: '{entered_password}'")
                selection = input("\nY/n >> ")
                if selection == "y" or selection == "Y" or not selection:
                    break
                elif selection == "n" or selection == "N":
                    functions.clear_function()
                    print("Error: Please enter a valid input.")
                    time.sleep(2)
                    functions.exit_function
            # Hash Password
            hashed_password = functions.hash_function(entered_password)
            # Define User Information
            user_directory = f"data/{entered_username}"
            user_data = {'username': entered_username, 'hashed_password': hashed_password} # noqa
            file_name = "user_data.json"
            file_directory = user_directory + "/" + file_name
            # Save User Information
            if os.path.exists(file_directory):
                functions.clear_function()
                print("Error: Username already registered.")
                time.sleep(2)
                functions.exit_function()
            else:
                os.mkdir(user_directory)
                with open(file_directory, 'x') as file:
                    json.dump(user_data, file)
                    return "success"
