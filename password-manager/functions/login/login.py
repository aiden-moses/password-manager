# Imports
import json
import functions
import time


def login_function():
    # Clear Screen
    functions.clear_function()
    # Request Information
    print("Enter your username:")
    entered_username = input(">> ")
    print("Enter your password: ")
    entered_password = input(">> ")
    # Clear Screen
    functions.clear_function()
    # Define User Information
    user_directory = f"data/{entered_username}"
    file_name = "user_data.json"
    file_directory = user_directory + "/" + file_name
    # Open Files
    try:
        with open(file_directory, 'r') as file:
            user_data = json.load(file)
        stored_username = user_data.get('username')
        stored_password_hash = user_data.get('hashed_password')
        entered_password_hash = functions.hash_function(entered_password)
        if entered_username == stored_username and entered_password_hash == stored_password_hash: # noqa
            return "success"
        else:
            functions.clear_function()
            print("Error: Invalid login credentials invalid.")
            time.sleep(2)
            functions.exit_function()
    except Exception:
        functions.clear_function()
        print("Error: You have not registered yet.")
        time.sleep(2)
        functions.exit_function()
