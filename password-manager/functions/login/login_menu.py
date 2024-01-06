from functions import clear_function
from rich.markdown import Markdown
from rich.console import Console
console = Console()

# Menu Text
login_menu_text = """
# Password Manager - Login Menu

Please select an option below.

1. Login
2. Register
3. Exit
"""


def login_menu_function():
    # Clear Screen
    clear_function()

    # Print Login Menu
    md = Markdown(login_menu_text)
    console.print(md)

    # Request Input
    selection = input("\n>> ")

    # If Valid Selection
    if selection == "1" or selection == "2" or selection == "3":
        return selection
    # If Invalid Selection
    else:
        while True:
            # Clear Screen
            clear_function()

            # Print Login Menu With Error Message
            console.print(md)
            print("\nError: Please enter a value between 1 and 3.")
            selection = input("\n>> ")
            # If Valid Selection
            if selection == "1" or selection == "2" or selection == "3":
                return selection
            # If Invalid Selection
            else:
                pass
