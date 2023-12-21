import sys
import time
from os import system
from game import start
from colorama import Fore

print(Fore.LIGHTGREEN_EX) # Setting text color to light green


def display_menu(menu):
    # Display a graphical text-based main menu
    print("*       *             *  ")
    print("   *             *      \n")
    print("// Welcome to Venator //")
    print("------------------------")
    print("The universe awaits you!\n")
    print("*      *           *")
    print("   *           *      *\n")
    print("===================")
    for k, function in menu.items():
        print(k, function.__name__)
    print("=================== \n")

def Play():
    # print("you have selected menu option one") # Simulate function output.
    system('clear')  # clears console
    start()

def Credits():
    # print("you have selected menu option one") # Simulate function output.
    system('clear')  # clears console
    print("\n")
    print("Credits:\n\n")
    print("Everything by Willem Gibson :)\n\n\n")
    time.sleep(3)
    system('clear')
    main()
    

def Quit():
    # print("quitting") # Simulate function output.
    system('clear')  # clears console
    sys.exit()


def main():
    # Create a menu dictionary where the key is an integer number and the value is a function name.
    functions_names = [Play, Credits, Quit]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(
            input("Please enter your selection by number: "))  # Get function key
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function
        break