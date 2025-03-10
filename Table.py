class Table:
    def __init__(self, inv_filename="Inventory.txt", sold_inventory="Sold_Inventory.txt"):
        self.inventory_file = inv_filename
        self.sold_inventory_file = sold_inventory
        # Stores formatted rows for display
        self.inventory = []  
        self.sold_inventory = []

    def add_item(self, set_code: str, item: str, stock: int, price):
        """Saves raw data to file but shortens text when displayed."""
        if isinstance(price, (float, int)):
            price_str = f"{price:.2f}"
        else:
            price_str = str(price)

        if len(price_str) > 7:
            raise ValueError("Price cannot be more than 7 digits long")

        # Validate stock type
        if not isinstance(stock, int):
            print("Stock must be an integer.")
            return None

        # Validate set length
        if len(set_code) > 3:
            print("Set name cannot be longer than 3 characters.")
            return None

        # Save full data to file (original item name)
        with open(self.inventory_file, "a") as file:
            file.write(f"{set_code.upper()}|{item}|{stock}|{price_str}\n")

        # Also update inventory list for display purposes
        self.load_inventory()

    def load_inventory(self):
        """Loads the inventory from the file into a list for display."""
        self.inventory.clear()
        with open(self.inventory_file, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) != 4:
                    continue
                set_str, item, stock, price = parts
                # Format each field properly
                set_str = set_str.ljust(3)
                # Shorten or pad item name for table display
                if len(item) > 38:
                    item_display = item[:35] + "..."
                else:
                    item_display = item.ljust(38)
                # Format stock and price with proper padding
                stock_display = str(stock).strip().center(8)
                price_display = str(price).strip().rjust(7)
                # Store formatted row
                self.inventory.append((set_str, item_display, stock_display, price_display))

    def check_inventory(self):
        """Reads formatted inventory and displays it in table format."""
        header = "+-----+----------------------------------------+----------+----------+"
        column_header = "| Set | Item                                   | Stock    | Price    |"
        table_str = header + "\n" + column_header + "\n" + header + "\n"
        for set_str, item, stock, price in self.inventory:
            table_str += f"| {set_str} | {item} | {stock} | ${price} |\n"
        table_str += header
        return table_str

    def remove_item(self, index):
        """Removes an item from both the in-memory list and the file."""
        with open(self.inventory_file, "r") as file:
            lines = file.readlines()
        if 0 <= index < len(lines):
            removed_entry = lines[index].strip()
            with open(self.inventory_file, "w") as file:
                for i, line in enumerate(lines):
                    if i != index:
                        file.write(line)
            print(f"Removed: {removed_entry}")
            self.load_inventory()
        else:
            print("Invalid index.")

    def move_item(self, index, quantity):
        """Move a quantity of an item from inventory to sold inventory."""
        with open(self.inventory_file, "r") as file:
            lines = file.readlines()
        if not (0 <= index < len(lines)):
            print("Invalid index.")
            return
        parts = lines[index].strip().split("|")
        if len(parts) != 4:
            print("Invalid data format.")
            return
        set_val, item, stock_str, price_str = parts
        try:
            current_stock = int(stock_str)
            quantity = int(quantity)
        except:
            print("Invalid number.")
            return
        if quantity > current_stock:
            print("Not enough stock to move.")
            return
        new_stock = current_stock - quantity
        # Update inventory file line for that item.
        if new_stock == 0:
            del lines[index]
        else:
            lines[index] = f"{set_val}|{item}|{new_stock}|{price_str}\n"
        with open(self.inventory_file, "w") as file:
            file.writelines(lines)
        # Add an entry to sold inventory
        with open(self.sold_inventory_file, "a") as file:
            file.write(f"{set_val}|{item}|{quantity}|{price_str}\n")
        print(f"Moved {quantity} of {item} to sold inventory.")
        self.load_inventory()
        self.load_sold_inventory()

    def update_item_stock(self, index, number):
        """Update the stock of an item."""
        with open(self.inventory_file, "r") as file:
            lines = file.readlines()
        if not (0 <= index < len(lines)):
            print("Invalid index.")
            return
        parts = lines[index].strip().split("|")
        if len(parts) != 4:
            print("Invalid data format.")
            return
        set_val, item, stock_str, price_str = parts
        try:
            current_stock = int(stock_str)
        except:
            print("Invalid stock number.")
            return
        new_stock = current_stock + number
        if number < 0:
            answer = input("Did you mean to move the removed stock to sold inventory? Y/N: ").upper()
            if answer in ["Y", "YES"]:
                quantity_to_move = abs(number)
                if quantity_to_move > current_stock:
                    print("Not enough stock to move.")
                    return
                self.move_item(index, quantity_to_move)
                return
        if new_stock < 0:
            print("Resulting stock cannot be negative.")
            return
        # Update the line in the file
        lines[index] = f"{set_val}|{item}|{new_stock}|{price_str}\n"
        with open(self.inventory_file, "w") as file:
            file.writelines(lines)
        print(f"Updated stock for item: {item} to {new_stock}")
        self.load_inventory()

    def load_sold_inventory(self):
        self.sold_inventory.clear()
        with open(self.sold_inventory_file, "r") as file:
            for line in file:
                sold_parts = line.strip().split("|")
                if len(sold_parts) != 4:
                    continue
                set_str, item, num_sold, price = sold_parts
                set_str = set_str.ljust(3)
                if len(item) > 38:
                    item_display = item[:35] + "..."
                else:
                    item_display = item.ljust(38)
                num_sold_display = str(num_sold).strip().center(10)
                price_display = str(price).strip().rjust(11)
                self.sold_inventory.append((set_str, item_display, num_sold_display, price_display))

    def check_sold_inventory(self):
        """Display the sold inventory items."""
        header = "+-----+----------------------------------------+------------+--------------+"
        column_header = "| Set | Item                                   | # Sold     | Price Sold @ |"
        sold_table_str = header + "\n" + column_header + "\n" + header + "\n"
        for set_str, item, num_sold, price in self.sold_inventory:
            sold_table_str += f"| {set_str} | {item} | {num_sold} | ${price} |\n"
        sold_table_str += header
        return sold_table_str

# Test Area (for debugging; comment out in production)
if __name__ == "__main__":
    t = Table()
    # Example items for testing:
    # t.add_item("mix", "Legendary Premium Warriors Collection", 4, 100)
    # t.add_item("mix", "Super Ultra Mega Collector's Set Edition", 2, 250.00)
    # t.add_item("abc", "A shorter name", 10, 49.99)
    t.load_inventory()
    t.load_sold_inventory()
    print(t.check_inventory())
    print()
    print(t.check_sold_inventory())
