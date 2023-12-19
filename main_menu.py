import sys
from os import system
from game import start


def display_menu(menu):
    # Display a graphical text-based main menu
    for k, function in menu.items():
        print(k, function.__name__)


def play():
    # print("you have selected menu option one") # Simulate function output.
    system('clear')  # clears console
    start()


def quit():
    # print("quitting") # Simulate function output.
    system('clear')  # clears console
    sys.exit()


def main():
    # Create a menu dictionary where the key is an integer number and the value is a function name.
    functions_names = [play, quit]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(
            input("Please enter your selection number: "))  # Get function key
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function