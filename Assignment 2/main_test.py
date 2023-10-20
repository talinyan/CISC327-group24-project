from restaurant import Restaurant, restaurants_all
from shopping_cart import ShoppingCart
from menu import RestaurantMenu, Item


# Create a shopping cart for the current user
user_cart = ShoppingCart()

def view_restaurants():
    print("List of available restaurants:")
    for restaurant in restaurants_all:
        print(restaurant.name)

def view_menu():
    restaurant_name = input("Enter the restaurant you wish to see the menu: ")
    for restaurant in restaurants_all:
        if restaurant.name == restaurant_name:
            restaurant.show_menu()
            return
    print("Restaurant not found.")

def add_to_cart():
    restaurant_name = input("Enter the restaurant where you want to add items: ")
    item_name = input("Enter the name of the item to add to the cart: ")
    quantity = int(input("Enter the quantity: "))
    
    for restaurant in restaurants_all:
        if restaurant.name == restaurant_name:
            for item in restaurant.menu.items:
                if item.name == item_name:
                    user_cart.add_item(item, restaurant, quantity)
                    print("Item added to the cart.")
                    return
    print("Restaurant or item not found.")

def remove_from_cart():
    restaurant_name = input("Enter the restaurant where you want to remove an item from the cart: ")
    item_name = input("Enter the name of the item to remove from the cart: ")
    
    result = user_cart.remove_item(restaurant_name, item_name)
    
    if result == "Item removed from the cart.":
        print(result)
    else:
        print("Item not found in the cart.")

def view_cart():
    user_cart.view_cart()

def check_out():
    user_cart_total = user_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")
    #show card number i will add logic later
    card_number = "**** **** **** 1234"  # Sample card number
    print(f"Card on file: {card_number}")

    # Ask the user if they want to pay with the card on file
    choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() == "yes":
        print("Payment successful. Order has been placed.")
        user_cart.cancel_order()  # Clear the shopping cart after a successful order
    else:
        print("Order not placed. Returning to the main menu to update payment.")


while True:
    print("Welcome to our delivery app!")
    print("Please choose an option:")
    print("1. View restaurants")
    print("2. View restaurant menu")
    print("3. Add item to cart")
    print("4. Remove item from cart")
    print("5. View cart details")
    print("6. Check out")
    # Add more options as needed

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        view_restaurants()
    elif choice == "2":
        view_menu()
    elif choice == "3":
        add_to_cart()
    elif choice == "4":
        remove_from_cart()
    elif choice == "5":
        view_cart()
    elif choice == "6":
        check_out()
    # Implement other menu options

    elif choice == "0":
        print("Thank you for using our app. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
