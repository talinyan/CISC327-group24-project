import csv
menu_file = 'restaurant-menus2.csv'

class Item:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price


class RestaurantMenu:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu = None
        self.load_menu(menu_file)

    def load_menu(self, menu_file):
        menu = []
        with open(menu_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == self.restaurant_name:
                    price_str = row[4].replace(' USD', '')  # Remove "USD" and any leading/trailing spaces
                    price = float(price_str)
                    item = Item(row[2], row[1], row[3], price)
                    menu.append(item)
        self.menu = menu
    
    def show_menu(self):
        categories_list = set()
        for item in self.menu:
            categories_list.add(item.category)

        for category in categories_list:
            print(f"Category: {category}") 
            for item in self.menu:
                if item.category == category:
                    print(f"{item.name} - ${item.price}")


# if __name__ == "__main__":
#     menu_file = 'restaurant-menus2.csv'
#     restaurant_name = '1'
#     restaurant_menu = RestaurantMenu(restaurant_name)
#     print(f"Menu for {restaurant_name}:")
#     restaurant_menu.show_menu()

#     # Test to view an item's price
#     while True:
#         item_name = input("Enter the name of the item to view its price (or type 'exit' to quit): ")
#         if item_name.lower() == 'exit':
#             break

#         found = False
#         for item in restaurant_menu.menu:
#             if item.name == item_name:
#                 print(f"{item.name} - ${item.price}")
#                 found = True
#                 break

#         if not found:
#             print(f"Item '{item_name}' not found in the menu.")
    