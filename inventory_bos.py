
class Item:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = int(quantity)
        self.price = float(price)
    def __str__(self):
        return f"{self.name:<16} | {self.category:<10} | {self.quantity:<8} | ${self.price:.2f}"

class Inventory:
    def __init__(self):
        self.items = {}
    
    def _find_key(self, name):
        """Find the actual key in items dictionary by case-insensitive comparison."""
        for key in self.items.keys():
            if key.lower() == name.lower():
                return key
        return None
    
    def add_item(self, name, category, quantity, price):
        """Add a new item to the inventory."""
        self.items[name] = Item(name, category, quantity, price)
    
    def remove_item(self, name):
        """Remove an item from inventory."""
        actual_key = self._find_key(name)
        if actual_key:
            del self.items[actual_key]
            print(f"Removed {actual_key} from inventory.")
        else:
            print(f"Item {name} not found.")
    
    def update_item(self, name, category, quantity, price):
        """Update attribute of item."""
        actual_key = self._find_key(name)
        if actual_key:
            item = self.items[actual_key]
            item.category = category
            item.quantity = int(quantity)
            item.price = float(price)
        else:
            print(f"Item '{name}' not found.")

    def get_item(self, name):
        actual_key = self._find_key(name)
        if actual_key:
            return self.items[actual_key]
        return None

    def decrement_item(self, name, amount):
        actual_key = self._find_key(name)
        if actual_key and amount > 0:
            item = self.items[actual_key]
            if item.quantity >= amount:
                item.quantity -= amount
                return True
        return False

    def restore_quantity(self, name, amount):
        actual_key = self._find_key(name)
        if actual_key and amount > 0:
            item = self.items[actual_key]
            item.quantity += amount
            return True
        return False

    def display_inventory(self):
        """Display All Inventory items."""
        if not self.items:
            print("No items in inventory.")
        else:
            print(f"\n{'Item':<16} | {'Category':<10} | {'Quantity':<6} | {'Price'}")
            print("=" * 50)
            for item in self.items.values():
                print(item)
            print("__________________________________________________\n")
    
    def search_item(self, name):
        """Search Inventory"""
        search_que = name.lower()
        found_any = False

        print(f"\n Search results for {name}")
        print(f"{'Item':<16} | {'Category':<10} | {'Quantity':<6} | {'Price'}")

        for item in self.items.values():
            if search_que in item.name.lower():
                print(item)
                found_any = True

        if not found_any:
            print("Search Item not found.")

nosh_inventory = Inventory()

grocery_inventory = {

"Apple": {"category": "Fruit", "Quantity": "50","price":  "0.50"},
"Bacon": {"category": "Meat", "Quantity": "35","price":  "4.50"},
"Banana": {"category": "Fruit", "Quantity": "100","price":  ".30"},
"Bread": {"category": "Bakery", "Quantity": "30","price":  "2.00"},
"Carrots": {"category": "Produce", "Quantity": "60","price":  "1.00"},
"Chicken breast": {"category": "Meat", "Quantity": "50","price":  "5.00"},
"Coffee": {"category": "Beverage", "Quantity": "20","price":  "8.00"},
"Eggs": {"category": "Dairy", "Quantity": "40","price": "2.50"},
"Ground beef": {"category": "Meat", "Quantity": "40","price":  "4.00"},
"Lettuce": {"category": "Produce", "Quantity": "40","price":  "1.50"},
"Milk": {"category": "Dairy", "Quantity": "25","price":  "3.00"},
"Orange Juice": {"category": "Beverage", "Quantity": "30","price":  "4.00"},
"Peanut Butter": {"category": "Pantry", "Quantity": "25","price":  "3.00"},
"Rice": {"category": "Pantry", "Quantity": "100", "price": "1.20"},
"Broccoli": {"category": "Produce", "Quantity": "45", "price": "1.80"},
"Yogurt": {"category": "Dairy", "Quantity": "30", "price": "2.00"},
"Cherry": {"category": "Fruit", "Quantity": "80", "price": "0.60"},
}

for item_name, details in grocery_inventory.items():
    nosh_inventory.add_item(
        name=item_name,
        category=details["category"],
        quantity=details["Quantity"],
        price=details["price"]
    )


while True:
        print("\n___ Nosh & Nibbles Inventory ___")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Item")
        print("5. Search")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == "1":
            nosh_inventory.display_inventory()

        elif choice == "2":
            print("\nAdd New Item")
            name = input("Enter new item name: ")
            category = input("Enter category: ")
            
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                nosh_inventory.add_item(name, category, quantity, price)
            except ValueError:
                print("-> Error: Invalid number format for quantity or price.")

        elif choice == "3":
            print("\nRemove Item")
            name = input("Enter item to remove: ")
            nosh_inventory.remove_item(name)

        elif choice == "4":
            print("\nUpdate Item")
            name = input("Enter Item to Update: ")
            current_item = nosh_inventory.items.get(name)  
            if current_item:
                print(f"Updating '{name}'. Enter to keep current value.")
                new_cat = input(f"Enter Category [{current_item.category}]: ")
                category = new_cat if new_cat != "" else current_item.category
        
                try:
                    new_qty = input(f"Enter Quantity [{current_item.quantity}]: ")
                    quantity = int(new_qty) if new_qty != "" else current_item.quantity

                    new_price = input(f"Enter Price [{current_item.price}]: ")
                    price = float(new_price) if new_price != "" else current_item.price

                    nosh_inventory.update_item(name, category, quantity, price)
                    print(f"{name} updated successfully.")
            
                except ValueError:
                    print("Incorrect number format for quantity or price.")
            else:
                print("Item not found in inventory. Check Spelling and Case Sensitive")

        elif choice == "5":
            print("\nSearch Item")
            name = input("Enter item name to search: ")
            nosh_inventory.search_item(name)

        elif choice == "6":
            nosh_inventory.display_inventory()
            print("Closing inventory values. Thank you for visiting.")
            break
        else:
            print("-> Invalid option. Please select 1 through 6.")