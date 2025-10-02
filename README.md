# 📦 Inventory Management System

A simple, effective command-line inventory management system built with Python. Perfect for tracking personal collections, small business stock, or any list of items with quantities and prices.

-----

### ✨ Features

  * **📊 View Inventories**: Check your current stock and sold items in neatly formatted tables.
  * **✏️ Full CRUD Operations**:
      * **Add** new items to your inventory.
      * **Remove** items by selecting them from the list.
      * **Update** the stock count of any item.
  * **💰 Track Sales**: When stock is removed, you can move it to the "Sold Inventory" log to keep a record of sales.
  * **🔍 Sort & Search**:
      * Sort your inventory by Set, Alphabetical Order, Stock, or Price.
      * Search for items by set code or name to find what you need quickly.
  * **🗑️ Clear Inventory**: Start fresh by clearing all items from your inventory after a confirmation prompt.
  * **👋 Personalized Greeting**: The app greets you by name and wishes you a good morning or afternoon.
  * **✅ Simple & Dependency-Free**: Runs with a standard Python installation, no external libraries needed.

-----

### ⚙️ Requirements

  * Python 3.x

-----

### 🚀 Getting Started

1.  **Get the code:**
    Could you clone this repository or download the files into a single directory?
    ```bash
    git clone https://github.com/shigeosapsycho/Inventory-Management-System/tree/main
    ```
2.  **Navigate to the directory:**
    ```bash
    cd Inventory-Management-System-main
    ```
3.  **Run the application:**
    ```bash
    python main.py
    ```
4.  **First-Time Setup**: The first time you run the script, it will ask for your name to personalize the experience. This is saved in `Name.txt`.

-----

### 📂 File Structure

```
.
├── .gitignore          # Specifies files for Git to ignore
├── Inventory.txt       # Database file for current inventory stock
├── Name.txt            # Stores the user's name
[cite_start]├── Sold_Inventory.txt  # Database file for logging sold items
[cite_start]├── Table.py            # Contains the Table class for all data handling
└── main.py             # Main entry point and user interface logic
```

-----

### 🛠️ How It Works

This system operates using a few core components:

  * **`main.py`**: Acts as the user interface (UI). It displays the menu, captures user input, and calls the appropriate methods from the `Table` class.
  * **`Table.py`**: The "engine" of the program. The `Table` class handles all logic for reading from and writing to the `.txt` data files. It formats data for display and contains the methods for adding, removing, updating, and moving inventory items.
  * **`.txt` Files**: Plain text files are used for data persistence. Items are stored in a pipe-separated format: `Set|Item|Stock|Price`. This makes the data easy to view and manually edit if needed.
