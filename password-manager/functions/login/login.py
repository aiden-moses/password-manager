import json
import functions


def login_function():
    functions.clear_function()
    try:
        while True:
            entered_username = input("Enter your username:\n>> ")
            entered_password = input("Enter your password:\n>> ")

            user_directory = f"data/{entered_username}"
            file_name = "user_data.json"
            file_directory = user_directory + "/" + file_name

            with open(file_directory, 'r') as file:
                user_data = json.load(file)

            stored_username = user_data.get('username')
            stored_password_hash = user_data.get('hashed_password')
            entered_password_hash = functions.hash_function(entered_password)

            if entered_username == stored_username and entered_password_hash == stored_password_hash: # noqa
                return entered_username
            else:
                functions.clear_function()
                print("Error: Invalid login credentials.\n")

    except Exception:
        return "error"
