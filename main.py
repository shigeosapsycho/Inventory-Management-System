import os, time
from datetime import datetime as dt
import Table

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
        print(f"Welcome back, {name}!\nIt is {dt.now().strftime("%B %d, %Y")}.")
        print(f"{'1. Check Inventory':<20} {'2. Add Item'}\n{'3. Remove Item':<20} {'4. Update Item'}\n{'5. Clear Inventory':<20} {'6. Change Name'}\n{'7. Add/Edit Note(s)':<20} {'8. Check Note(s)'}\n9. Terminate Program\n")
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
            case "6":
                clear_console() # Change Name
                break
            case "7": # Add/Edit Note(s)
                clear_console()
                break
            case "8": # Check Note(s)
                clear_console()
                break
            case "9": # Terminate Program
                print(f"See you next time, {name}!")
                break
            case _:
                clear_console()
                print("Invalid option.")
                time.sleep(1)
            
if __name__ == "__main__":
    main()