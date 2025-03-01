import os
from datetime import datetime

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_first_time():
    file = "Name.txt"
    if os.path.exists(file):
        return True
    else:
        prompt = input("Looks like it is your first time opening this program. What is your name?\n")
        with open(file, "w") as file:
            file.write(prompt)

def check_inventory():
    pass

def check_sold_items():
    pass

def add_item():
    pass

def remove_item():
    pass

def update_item_stock():
    pass

def clear_inventory():
    pass

def make_file():
    """
    Logic: it needs to check if the file is there or not, if its not there it will create two files: inventory_file and sold_file
    Check if it exists by using an if statement.
    """
    folder_directory = os.getcwd()
    files = ["Inventory.txt", "Outbound.txt"]
    # files = ["Inventory.txt", "Outbound.txt", "Name.txt"]
    
    file_paths = {name: os.path.join(folder_directory, name) for name in files}

    if not all(os.path.exists(file_paths[file]) for file in files):
        for file in files:
            with open(file, "w") as file:
                pass

def change_name(input):
    pass

def main(): # Menu
    clear_console()
    check_first_time()
    name_file = open('Name.txt', 'r')
    name = name_file.read()
    
    while True:
        # Precondiiton and check text file
        make_file()
        
        # Greet the user
        print(f"Welcome back, {name}!")
        print("What would you like to do?")
        print(f"{'1. Check Inventory':<20} {'2. Add Item'}\n{'3. Remove Item':<20} {'4. Update Item'}\n{'5. Clear Inventory':<20} {'6. Change Name'}\n{'7. Add/Edit note':<20} {'8. Check Notes'}\n9. Terminate Program\n")
        option = input()
        # option = input("Welcome to the Inventory Management System!\n1. Check Inventory\n2. Add Item\n3. Remove Item\n4. Update Item\n5. Clear Inventory\n6. Check Items Sold\n7. Exit\n\n") # Currently this is a lot of options I might do a page thing
        match option:
            case "1":
                print("Option 1")
                clear_console()
            case "2":
                clear_console()
                break
            case "3":
                clear_console()
                break
            case "4":
                clear_console()
                break
            case "5":
                clear_console()
                break
            case "6":
                clear_console()
                break
            case "7":
                clear_console()
                break
            case "8":
                clear_console()
                break
            case "9":
                print(f"See you next time, {name}!")
                break
            case _:
                print("Invalid option.\n")
                clear_console()
                # break
            
if __name__ == "__main__":
    main()