import os
import time
import sys
from datetime import datetime as dt
from Table import Table

def clear_console():
    """Clear console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_first_time():
    """Check if it's the user's first time ever opening the program."""
    file = "Name.txt"
    if os.path.exists(file):
        return
    else:
        prompt = input("Looks like it is your first time opening this program. What is your name?\n")
        with open(file, "w") as f:
            f.write(prompt)

def clear_inventory():
    """Clear the inventory; prompts the user if they are sure with their choice."""
    clear_console()
    while True:
        confirmation = input("Are you sure you want to clear your inventory?\nYou can NOT revert this change Y/N\n\n").upper()
        if confirmation in ["YES", "Y"]:
            print("Inventory Cleared.")
            with open("Inventory.txt", "w") as file:
                file.write("")
            time.sleep(1)
            clear_console()
            break
        elif confirmation in ["NO", "N"]:
            print("Inventory deletion voided. Returning back to the menu.")
            time.sleep(1)
            clear_console()
            break
        else:
            print("Not a valid option.")
            time.sleep(1)
            clear_console()

def make_file():
    """Makes the files Inventory.txt and Sold_Inventory.txt for the program."""
    folder_directory = os.getcwd()
    files = ["Inventory.txt", "Sold_Inventory.txt"]
    file_paths = {name: os.path.join(folder_directory, name) for name in files}

    for name in files:
        if not os.path.exists(file_paths[name]):
            with open(name, "w") as f:
                pass

def sort_inventory():
    clear_console()
    # Read inventory file
    with open("Inventory.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        print("Your file has nothing to sort.")
        time.sleep(1)
        clear_console()
        return

    # Convert lines into a list of tuples (set, item, stock, price)
    data = []
    for line in lines:
        parts = line.split("|")
        if len(parts) == 4:
            set_val, item, stock, price = parts
            try:
                stock_val = int(stock)
            except:
                stock_val = stock
            try:
                price_val = float(price)
            except:
                price_val = price
            data.append((set_val, item, stock_val, price_val))

    sort_option = input("Sort inventory set by:\n1. Set\n2. Alphabetical Order\n3. Stock\n4. Price\n5. Exit\n")
    if sort_option == "1":
        sorted_data = sorted(data, key=lambda x: x[0].upper())
    elif sort_option == "2":
        sorted_data = sorted(data, key=lambda x: x[1].upper())
    elif sort_option == "3":
        sorted_data = sorted(data, key=lambda x: x[2])
    elif sort_option == "4":
        sorted_data = sorted(data, key=lambda x: x[3])
    elif sort_option == "5":
        clear_console()
        return
    else:
        print("Not a valid option.")
        time.sleep(1)
        clear_console()
        return

    # Write sorted data back to Inventory.txt
    with open("Inventory.txt", "w") as f:
        for item in sorted_data:
            f.write(f"{item[0]}|{item[1]}|{item[2]}|{item[3]}\n")
    print("Inventory sorted.")
    time.sleep(1)
    clear_console()

def change_name():
    clear_console()
    new_name = input("Enter your new name: ")
    with open("Name.txt", "w") as f:
        f.write(new_name)
    print("Name updated.")
    time.sleep(1)
    clear_console()

def search_inventory():
    clear_console()
    search_term = input("Enter search term (set code or item name): ").strip().lower()
    with open("Inventory.txt", "r") as f:
        lines = f.readlines()
    results = []
    for i, line in enumerate(lines):
        if search_term in line.lower():
            results.append((i, line.strip()))
    if results:
        print("Search Results:")
        for index, result in results:
            changed_result = result.replace ("|", " | ")
            print(f"{changed_result}")
    else:
        print("No matching items found.")
    input("Press Enter to return to the menu...")
    clear_console()

def add_item_menu(inventory_table):
    clear_console()
    set_code = input("Enter Set (max 3 characters): ").strip()
    if len(set_code) > 3:
        print("Set name cannot be longer than 3 characters.")
        time.sleep(1)
        return
    item_name = input("Enter Item Name: ").strip()
    try:
        stock = int(input("Enter Stock (integer): "))
    except:
        print("Stock must be an integer.")
        time.sleep(1)
        return
    try:
        price = float(input("Enter Price: "))
    except:
        print("Invalid price format.")
        time.sleep(1)
        return
    inventory_table.add_item(set_code, item_name, stock, price)
    print("Item added.")
    time.sleep(1)

def remove_item_menu(inventory_table):
    clear_console()
    inventory_table.load_inventory()
    print(inventory_table.check_inventory())
    try:
        index = int(input("Enter the index of the item to remove (starting from 0): "))
    except:
        print("Invalid index.")
        time.sleep(1)
        return
    inventory_table.remove_item(index)
    time.sleep(1)

def update_item_menu(inventory_table):
    clear_console()
    inventory_table.load_inventory()
    print(inventory_table.check_inventory())
    try:
        index = int(input("Enter the index of the item to update: "))
        number = int(input("Enter the number to update the stock (positive to add, negative to remove): "))
    except:
        print("Invalid input.")
        time.sleep(1)
        return
    inventory_table.update_item_stock(index, number)
    time.sleep(1)

def check_inventory_menu(inventory_table):
    clear_console()
    inventory_table.load_inventory()
    print(inventory_table.check_inventory())
    input("Press Enter to return to the menu...")
    clear_console()

def check_sold_inventory_menu(inventory_table):
    clear_console()
    inventory_table.load_sold_inventory()
    print(inventory_table.check_sold_inventory())
    input("Press Enter to return to the menu...")
    clear_console()

def main():
    clear_console()
    check_first_time()
    with open('Name.txt', 'r') as name_file:
        name = name_file.read().strip()
    make_file()
    
    # Good afternoon/morning
    current_hour = dt.now().hour
    greeting = "Good morning" if current_hour < 12 else "Good afternoon"
    
    print(f"{greeting}, {name}!")
    time.sleep(1)
    print(f"It is {dt.now().strftime('%B %d, %Y')}.")
    time.sleep(2)
    inventory_table = Table()
    while True:
        clear_console()
        print("What would you like to do?")
        print(f"{'1.  Check Inventory':<30} {'2.  Add Item':<30}")
        print(f"{'3.  Remove Item':<30} {'4.  Update Item':<30}")
        print(f"{'5.  Sort Inventory':<30} {'6.  Search Inventory':<30}")
        print(f"{'7.  Check Sold Inventory':<30} {'8.  Clear Inventory':<30}")
        print(f"{'9.  Change Name':<30} {'10. Terminate Program':<30}")
        option = input("Enter option: ")
        if option == "1":
            # Check inventory
            check_inventory_menu(inventory_table)
        elif option == "2":
            # Add item
            add_item_menu(inventory_table)
        elif option == "3":
            # Remove item
            remove_item_menu(inventory_table)
        elif option == "4":
            # Update item
            update_item_menu(inventory_table)
        elif option == "5":
            # Sort inventory
            sort_inventory()
            check_inventory_menu(inventory_table)
        elif option == "6":
            # Search inventory
            search_inventory()
        elif option == "7":
            # Check sold inventory
            check_sold_inventory_menu(inventory_table)
        elif option == "8":
            # Clear inventory
            clear_inventory()
        elif option == "9":
            change_name()
        elif option == "10":
            print(f"See you next time, {name}!")
            sys.exit()
        else:
            print("Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main()