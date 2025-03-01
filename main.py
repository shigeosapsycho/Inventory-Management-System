import os

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
    inventory_file = "Inventory.txt"
    sold_file = "Outbound.txt"
    
    inv_file_path = os.path.join(folder_directory, inventory_file)
    sold_file_path = os.path.join(folder_directory, sold_file)

    if not (os.path.exists(inv_file_path) and os.path.exists(sold_file_path)):
        with open(inv_file_path, "w") as file:
            pass
        with open(sold_file_path, "w") as file:
            pass

def display_options(num):
    match num:
        case 1:
            print("1. Check Inventory\n2. Add Item\n3. Remove Item\n4. Update Item\n5. Clear Inventory")
            print("")
        case 2:
            print("1. Add note\n2. Check notes\n3. Terminate program")

def main(): # Menu
    while True:
        # Precondiiton and check text file
        make_file()
        print("Welcome to the Inventory Management System!", end="")
        display_options(num=1)
        
        option = input()
        # option = input("Welcome to the Inventory Management System!\n1. Check Inventory\n2. Add Item\n3. Remove Item\n4. Update Item\n5. Clear Inventory\n6. Check Items Sold\n7. Exit\n\n") # Currently this is a lot of options I might do a page thing
        
        match option:
            case "1":
                print("Option 1")
                break
            case "2":
                break
            case "3":
                break
            case "4":
                break
            case "5":
                break
            case "6":
                break
            case "7":
                print("Goodbye. All your progress has been saved")
                break
            case _:
                print("Invalid option.\n")
                # break
            
if __name__ == "__main__":
    main()