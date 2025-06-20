class NegativeQuantityError(Exception):
    """Custom exception for when item quantity drops below zero"""

    def __init__(self, message):
        super().__init__(message)


class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            raise NegativeQuantityError(
                f"Quantity cannot be negative for item: {self.name}"
            )
        self.quantity = new_quantity

    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError(f"Price cannot be negative for item: {self.name}")
        self.price = new_price


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def update_item(self, name, new_quantity=None, new_price=None):
        for item in self.items:
            if item.name == name:
                if new_quantity is not None:
                    item.update_quantity(new_quantity)
                if new_price is not None:
                    item.update_price(new_price)
                return
        print(f"Item '{name}' not found in the inventory.")


# Example usage
inventory = Inventory()

# Add items to the inventory
item1 = Item("Apple", 10, 0.5)
item2 = Item("Banana", 5, 0.75)
inventory.add_item(item1)
inventory.add_item(item2)

# Update item quantities and prices
try:
    inventory.update_item("Apple", new_quantity=-2)
except NegativeQuantityError as e:
    print(e)

try:
    inventory.update_item("Banana", new_price=-1.0)
except ValueError as e:
    print(e)

inventory.update_item("Apple", new_quantity=8, new_price=0.6)
inventory.update_item("Banana", new_quantity=7, new_price=0.8)
