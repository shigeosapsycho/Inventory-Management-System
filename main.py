import os, time, sys
from datetime import datetime as dt
import Table as Table

def clear_console():
    """ Clear console """
    os.system('cls' if os.name == 'nt' else 'clear')

def check_first_time():
    """ Check if it's the user's first time ever opening the program """
    file = "Name.txt"
    if os.path.exists(file):
        return True
    else:
        prompt = input("Looks like it is your first time opening this program. What is your name?\n")
        with open(file, "w") as file:
            file.write(prompt)

def clear_inventory():
    """ Clear the inventory, prompts the user if they are sure with their choice. """
    clear_console()
    while True:
        confirmation = input("Are you sure you want to clear your inventory?\nYou can NOT revert this change Y/N\n\n").upper()
        
        if confirmation == "YES" or confirmation == "Y":
            print("Inventory Cleared.")
            with open("Inventory.txt", "w") as file:
                file.write("")
            time.sleep(1)
            clear_console()
            break
        elif confirmation == "NO" or confirmation == "N":
            print("Inventory deletion voided. Returning back to the menu.")
            time.sleep(1)
            clear_console()
            break
        else:
            print("Not a valid option.")
            time.sleep(1)
            clear_console()

def make_file():
    """ Makes the files Inventory.txt and Sold_Inventory.txt for the program"""
    folder_directory = os.getcwd()
    files = ["Inventory.txt", "Sold_Inventory.txt"]
    
    file_paths = {name: os.path.join(folder_directory, name) for name in files}

    if not all(os.path.exists(file_paths[file]) for file in files):
        for file in files:
            with open(file, "w") as file:
                pass

def sort_inventory():
    clear_console()
    while True:
        if os.stat("Inventory.txt").st_size == 0:
            print("Your file has nothing to sort.")
            time.sleep(1)
            clear_console()
        sort_option = input(f"Sort inventory set by:\n{'1. Set':<10} {'2. Alphabetical Order':<10}\n{'3. Stock':<10} {'4. Price':<10}\n{'5. Exit':<10}\n")
        
        match sort_option:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                clear_console()
                break
            case _:
                print("Not a valid option.")
                time.sleep(1)
                clear_console()
        pass

def change_name(input):
    pass

def main(): # Menu
    clear_console()
    check_first_time()
    name_file = open('Name.txt', 'r')
    name = name_file.read()
    
    # Precondiiton and check text file
    make_file()
    
    # Greet the user
    print(f"Welcome back, {name}!")
    time.sleep(1)
    print(f"It is {dt.now().strftime("%B %d, %Y")}.")
    time.sleep(2)
    
    while True:
        clear_console
        print("What would you like to do?")
        print(f"{'1. Check Inventory':<20} {'2. Add Item'}\n{'3. Remove Item':<20} {'4. Update Item'}\n{'5. Clear Inventory':<20} {'6. Change Name'}\n{'7. Sort Inventory':<20} {'8. Search Inventory'}\n9. Terminate Program\n")
        option = input()
        
        match option:
            case "1": # Check Inventory
                print("Option 1")
                clear_console()
            case "2": # Add Item
                clear_console()
                break
            case "3": # Remove Item
                clear_console()
                break
            case "4": # Update Item
                clear_console()
                break
            case "5": # Clear Inventory
                clear_inventory()
            case "6":
                clear_console() # Change Name
                break
            case "7": # Sort Invenotory
                sort_inventory()
            case "8": # Search Inventory
                clear_console()
                break
            case "9": # Terminate Program
                print(f"See you next time, {name}!")
                sys.exit()
            case _:
                clear_console()
                print("Invalid option.")
                time.sleep(1)
            
if __name__ == "__main__":
    main()
    
""" Current plans:
Greet User:
    Greet the user in good morning/good afternoon depending on the time of day
Search Inventory:
    When searching inventory you are dispalyed these options:
        Search by: 1. Set or Item
Sort Inventory:
    When sortiong inventory you are displayed these options:
        Sort by: 1. Set, 2. Alphabetical Order, 3. Stock, 4. Price
Clear Inventory:
    Decide if I want to make it replace everything in the text or to delet the file so they can recover it in the trash can.
"""