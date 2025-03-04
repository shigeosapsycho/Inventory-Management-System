class Table:
    def __init__(self, inv_filename="Inventory.txt", sold_inventory="Sold_Inventory.txt"):
        self.inventory_file, self.sold_inventory_file = inv_filename, sold_inventory
        # Stores formatted rows for display
        self.inventory = []  
        self.sold_inventory = []

    def add_item(self, set: str, item: str, stock: int, price):
        """ Saves raw data to file but shortens text when displayed. """
        if isinstance(price, (float, int)):
            price = f"{price:.2f}"
        else:
            price = str(price)

        if len(price) > 7:
            raise ValueError("Price cannot be more than 7 digits long")

        # Validate stock type
        if not isinstance(stock, int):
            print("Stock must be an integer.")
            return None

        # Validate set length
        if len(set) > 3:
            print("Set name cannot be longer than 3 characters.")
            return None

        # Save full data to file (original item name)
        with open(self.inventory_file, "a") as file:
            file.write(f"{set.upper()}|{item}|{stock}|{price}\n")

        # Also update inventory list for display purposes
        self.load_inventory()

    def load_inventory(self):
        """Loads the inventory from the file into a list for display."""
        self.inventory.clear()
        try:
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
                        item = item[:35] + "..."
                    else:
                        item = item.ljust(38)
                    
                    # Format stock and price with proper padding
                    stock = stock.strip().center(8)
                    price = price.strip().rjust(7)

                    # Store formatted row
                    self.inventory.append((set_str, item, stock, price))
        except FileNotFoundError:
            print("No inventory file found. Starting fresh.")

    def check_inventory(self):
        """ Reads formatted inventory and displays it in table format. """
        header = "+-----+----------------------------------------+----------+----------+"
        column_header = "| Set | Item                                   | Stock    | Price    |"
        
        table_str = header + "\n" + column_header + "\n" + header + "\n"
        
        for set_str, item, stock, price in self.inventory:
            table_str += f"| {set_str} | {item} | {stock} | ${price} |\n"
        table_str += header
        
        return table_str

    def remove_item(self, index):
        """ Removes an item from both the in-memory list and the file. """
        if 0 <= index < len(self.inventory):
            removed_entry = self.inventory[index]
            
            # Reload full data, remove the corresponding entry, and rewrite file
            with open(self.inventory_file, "r") as file:
                lines = file.readlines()
            
            with open(self.inventory_file, "w") as file:
                for i, line in enumerate(lines):
                    if i != index:
                        file.write(line)
            
            print(f"Removed: {removed_entry}")
            self.load_inventory()
        else:
            print("Invalid index.")

    def move_item(self, index, stock):
        """ Move the row from inventory to sold inventory """
        pass

    def update_item_stock(self):
        """ Update the stock of an item """
        pass
    
    def check_sold_inventory(self):
        """ Display the sold inventory items (Items user has sold)"""
        header = "+-----+----------------------------------------+------------+--------------+"
        column_header = "| Set | Item                                   | # Sold     | Price Sold   |"

        sold_table_str = header + "\n" + column_header + "\n" + header + "\n"
        
        for set_str, item, stock, price in self.sold_inventory:
            sold_table_str += f"| {set_str} | {item} | {stock} | ${price} |"
        
        sold_table_str += header
        
        return sold_table_str

# Test Area
t = Table()
# t.add_item("mix", "Legendary Premium Warriors Collection", 4, 100)
# t.add_item("mix", "Super Ultra Mega Collector's Set Edition", 2, 250.00)
# t.add_item("abc", "A shorter name", 10, 49.99)

print(t.check_inventory())