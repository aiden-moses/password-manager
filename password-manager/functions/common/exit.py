# Imports
import sys
from .clear import clear_function


def exit_function():
    clear_function()
    print("Exiting now...")
    sys.exit()
