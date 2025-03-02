class Table:
    def __init__():
        pass
    
    def add_row(set: str, item: str, stock: int, price):
        """ 
        Add row template:
| {set} | {item}} |    {stock}    |   ${price}    |
+-----+----------------------------------------+----------+----------+
        """
        if isinstance(price, (float, int)):
            price = f"{price:.2f}"
        else:
            price = str(price)
        if len(price) > 7:
            raise ValueError("Price can not be more than 7 digits long")
        else:
            price = price.ljust(7)
        
        # Check stock type
        if not isinstance(stock, int):
            print("Stock can only be an integer.")
            return None
        
        # Check set length
        if len(set) > 3:
            print("Set can not be longer than 3 characters long.")
            return None
        
        # Adjust item length
        if len(item) > 38:
            item = item[:38 - 3] + "..."
        else:
            item = item.ljust(38)
        
        return f"| {set.upper()} | {item} |    {stock}    | ${price} |"

# Test area
t = Table
# t.add_row("MIX", "Legendary Warrior Collection", 4, 100.00)
# t.add_row("MIX", "Legendary Warrior Collection", "100")
# print("+-----+----------------------------------------+----------+----------+")
# print(t.add_row("mix", "Legendary Premium Warriors Collection", 4, 100))
# print("+-----+----------------------------------------+----------+----------+")

# print(t.add_row("mix", "Legendary Premium Warriors Collection", 4, 100.00))
# print("+-----+----------------------------------------+----------+----------+")

# print(t.add_row("mix", "Legendary Premium Warriors Collection", 4, 100.0))
# print("+-----+----------------------------------------+----------+----------+")

# print(t.add_row("mix", "Legendary Premium Warriors Collectionhdjbfhbkfdhkgakdsg", 4, 100.0))
# print("+-----+----------------------------------------+----------+----------+")