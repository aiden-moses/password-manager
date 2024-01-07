# Imports
import json
import time
import functions
from rich.console import Console
from rich.table import Table
console = Console()
table = Table(title="Password Manager - Saved Passwords")


def table_function(view, cipher):
    table.add_column("Application / Website", justify='center', no_wrap=True)
    table.add_column("Username", justify='center', no_wrap=True)
    table.add_column("Password", justify='center', no_wrap=True)
    for x in view:
        user = x['username']
        application = x['application']
        encrypted_password = x['encrypted_password']
        decrypted_password = functions.decrypt_function(cipher, encrypted_password) # noqa
        table.add_row(application, user, decrypted_password)
    while True:
        functions.clear_function()
        console.print(table)
        selection = input("\nWould you like to return to the main menu?\nY/n>> ") # noqa
        if selection == "y" or selection == "Y" or not selection:
            break
        else:
            pass


def view_logins_function(username, cipher):
    functions.clear_function()
    file_name = 'data.json'
    directory = f'data/{username}/'
    file_directory = directory + file_name
    try:
        with open(file_directory, 'r') as data:
            view = json.load(data)
            table_function(view, cipher)
    except FileNotFoundError:
        functions.clear_function()
        print("Error: You have not saved any passwords.")
        time.sleep(2)
        functions.exit_function()
