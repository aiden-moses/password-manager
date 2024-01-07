from functions import clear_function
from rich.markdown import Markdown
from rich.console import Console
console = Console()

login_menu_text = """
# Password Manager - Login Menu

Please select an option below.

1. Login
2. Register
3. Exit
"""


def login_menu_function():
    clear_function()

    md = Markdown(login_menu_text)
    console.print(md)
    selection = input("\n>> ")

    if selection == "1" or selection == "2" or selection == "3":
        return selection
    else:
        while True:
            clear_function()

            console.print(md)
            print("\nError: Please enter a value between 1 and 3.")
            selection = input("\n>> ")

            if selection == "1" or selection == "2" or selection == "3":
                return selection
            else:
                pass
