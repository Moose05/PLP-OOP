# Base class
class McDonalds:
    def __init__(self, location, menu):
        self.location = location
        self.menu = menu  # Dictionary: item -> price

    def show_menu(self):
        print(f"\nWelcome to McDonald's at {self.location}!")
        print("Menu:")
        for item, price in self.menu.items():
            print(f"- {item}: R{price:.2f}")

    def pick_item(self):
        choice = input("\nEnter the item you want to order: ").strip()
        if choice in self.menu:
            print(f"{choice} costs R{self.menu[choice]:.2f}")
        else:
            print("Sorry, that item is not on the menu.")


# Child class inheriting from McDonalds
class BreakfastMenu(McDonalds):
    def __init__(self, location, menu, extra_lunch_items):
        # Merge breakfast menu with selected lunch items
        full_menu = {**menu, **extra_lunch_items}
        super().__init__(location, full_menu)


# Define menus
lunch_items = {
    "Big Mac": 60.00,
    "McChicken": 65.00,
    "Fries": 30.00,
    "Coke": 20.00
}

breakfast_items = {
    "Egg McMuffin": 25.00,
    "Hotcakes": 15.00,
    "Coffee": 20.00
}

# Select lunch items to include in breakfast
shared_items = {
    "Fries": lunch_items["Fries"],
    "Coke": lunch_items["Coke"]
}

# Create objects
lunch_branch = McDonalds("Downtown", lunch_items)
breakfast_branch = BreakfastMenu("Airport", breakfast_items, shared_items)

# Show and pick from breakfast menu
breakfast_branch.show_menu()
breakfast_branch.pick_item()
