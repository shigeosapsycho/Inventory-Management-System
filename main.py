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
    files = ["Inventory.txt", "Outbound.txt", "Name.txt"]
    
    file_paths = {name: os.path.join(folder_directory, name) for name in files}

    inv_file_path = file_paths["Inventory.txt"]
    sold_file_path = file_paths["Outbound.txt"]
    name_file_path = file_paths["Name.txt"]

    if not all(os.path.exists(file_paths[file]) for file in files):
        for file in files:
            with open(file, "w") as file:
                pass

def display_options(num):
    match num:
        case 1:
            print("1. Check Inventory\n2. Add Item\n3. Remove Item\n4. Update Item\n5. Clear Inventory")
            print("")
        case 2:
            print("1. Add note\n2. Check notes\nChange name\n3. Terminate program")

def main(): # Menu
    while True:
        # Precondiiton and check text file
        make_file()
        
        # Greet the user
        print("Welcome to the Inventory Management System!")
        num = 1
        display_options(num = num)
        
        option = input()
        # option = input("Welcome to the Inventory Management System!\n1. Check Inventory\n2. Add Item\n3. Remove Item\n4. Update Item\n5. Clear Inventory\n6. Check Items Sold\n7. Exit\n\n") # Currently this is a lot of options I might do a page thing
        
        if num == 1:
            match option:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case _:
                    print("Invalid option.\n")
        else:
            pass
        # match option:
        #     case "1":
        #         print("Option 1")
        #         break
        #     case "2":
        #         break
        #     case "3":
        #         break
        #     case "4":
        #         break
        #     case "5":
        #         break
        #     case "6":
        #         break
        #     case "7":
        #         print("Goodbye. All your progress has been saved")
        #         break
        #     case _:
        #         print("Invalid option.\n")
        #         # break
            
if __name__ == "__main__":
    main()