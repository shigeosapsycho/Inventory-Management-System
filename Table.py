class Table:
    def __init__():
        pass
    
    def add_row(set: str, item: str, price: int):
        """ 
        Add row template:
| {set} | {item}} |    {stock}    |   ${price}    |
+-----+----------------------------------------+----------+----------+
        """
        
        if type(price) != int:
            print("Price can only be an integer.")
        elif len(set) > 3:
            print("Set can not be longer than 3 characters long.") # Make it ask again but I have not implemented that yet.
        elif len(item) > 40:   
            item = item[:40-3] + "..." # Make it under 40 characters but still keep the full name in the Inventory.txt file
        elif len(item) <= 40:
            item = item.ljust(40) # Make it 40 characters by adding spaces
        elif len(price) > 7:
            raise ValueError("Price can not be more than 7 digits long") # Reprompt the user after
        elif len(price) <= 7:
            price = price.ljust(7) # Fill the price to make it fit the box
        pass

# Test area
t = Table
t.add_row("MIX", "Legendary Warrior Collection", 100)
# t.add_row("MIX", "Legendary Warrior Collection", "100")