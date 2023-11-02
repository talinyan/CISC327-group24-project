# Import necessary modules and classes
from shopping_cart import ShoppingCart
from restaurant import Restaurant
from user_profile import UserProfile
import pymongo

# Function to validate user credentials
def valid_credentials(phone_number, email, password):
        # phone number must be of length 10 and all digits
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Invalid phone number. Please try again.\n")
            return False
        
        # password must be 8 characters
        if len(password) < 8:
            print("Password too short. Please try again.\n")
            return False
        
        if "@" not in email:
            print("Invalid email. Please try again.\n")
            return False
        
        return True

# Function to register a new user
def register():
    while True:
        name = input("Enter your name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        password = input("Choose a password (must be at least 8 characters): ")
        if valid_credentials(phone_number, email, password):
            user_data = { # arrange data into row format
                "name": name,
                "phone_number": phone_number,
                "email": email,
                "address": address,
                "password": password,
                "payment_methods": []    
            }
            users_table.insert_one(user_data) # add row to table
            users.append(UserProfile(address, phone_number, name, password, email))
            print("Account created for Bob. Please login.\n")
            break
        else: # allow user to exit to main menu after incorrect registration attempt
            exit_check = input("Enter 'r' to retry registration, anything else to exit: ")
            if exit_check != 'r':
                break

# Function to log in a user
def login():
    if len(users) == 0: # empty users table
        return print("Please register first.")
        
    while True:
        # allow user to exit to main menu after incorrect login attempt
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        for user in users:
            if user.email == email and user.password == password:
                print(f"You have logged in successfully.\n")
                return user
        else:
            print("Invalid email or password. Please try again.\n")
        
        # allow user to exit to main menu after incorrect login attempt
        exit_check = input("Enter 'r' to retry login, anything else to exit: ")
        if exit_check != 'r':
            break

# Function to modify the user's profile
def modify_profile():
    while True:
        phone_number = input("Enter your new phone number: ")
        email = input("Enter your new email: ")
        address = input("Enter your new address: ")
        old_password = input("Enter your old password: ")
        new_password = input("Choose a new password (must be at least 8 characters): ")

        if valid_credentials(phone_number, email, new_password) and old_password == cur_profile['password']:
            cur_profile['phone_number'] = phone_number
            cur_profile['email'] = email
            cur_profile['address'] = address
            cur_profile['password'] = new_password

            # update profile in database with modified profile info
            users_table.update_one(
                {"_id": cur_profile["_id"]},
                {"$set": cur_profile}
            )
            print("Profile information changed successfully.\n")
            break
        else:
            print("Invalid password. Please try again.")
            # allow user to exit to main menu after incorrect password attempt
            exit_check = input("Enter 'r' to retry password, anything else to exit: ")
            if exit_check != 'r':
                break

def show_profile():
    print(f"Name: {cur_profile['name']}       Email: {cur_profile['email']}        Address: {cur_profile['address']}     Phone Number: {cur_profile['phone_number']}\n")

# Function to add a payment method to the current user's profile
def add_payment():
    cc = input("Enter your credit card information: ")
    name = input("Enter the name on the card: ")
    address = input("Enter the address on the card: ")
    payment_data = {
        "credit_card": cc,
        "card_name": name,
        "billing_address": address
    }
    cur_profile['payment_methods'].append(payment_data)

    # update profile in database with new payment info
    update_payment_db()
    print("Payment method added.\n")

# Function to modify an existing payment method
def modify_payment():
    while True:
        id = int(input("Enter the id of the payment method to modify: "))
        if id >= len(cur_profile['payment_methods']) or id < 0:
            print("Invalid id. Please try again.")
            # allow user to exit to main menu after incorrect id attempt
            exit_check = input("Enter 'r' to retry id, anything else to exit: ")
            if exit_check != 'r':
                break
        else:
            cc = input("Enter your credit card numbers: ")
            name = input("Enter the name on the card: ")
            address = input("Enter the address on the card: ")
            payment_data = {
                "credit_card": cc,
                "card_name": name,
                "billing_address": address
            }
            cur_profile['payment_methods'][id] = payment_data

            # update profile in database with modified payment info
            update_payment_db()
            print("Payment method modified.\n")
            break

# Function to remove payment method
def remove_payment():
    while True:
        id = int(input("Enter the id of the payment method to remove: "))
        if id >= len(cur_profile['payment_methods']) or id < 0:
            print("Invalid id. Please try again.")
            # allow user to exit to main menu after incorrect id attempt
            exit_check = input("Enter 'r' to retry id, anything else to exit: ")
            if exit_check != 'r':
                break
        else:
            cur_profile['payment_methods'].pop(id)
            # update profile in database with removed payment info
            update_payment_db()
            print("Payment method removed.\n")
            break

# Function to update payment methods in backend database (adding, modifying, & removing payments)
def update_payment_db():
    users_table.update_one(
        {"_id": cur_profile["_id"]},
        {"$set": cur_profile}
    )

# Function to show all payment methods for logged in user
def show_payments():
    if len(cur_profile['payment_methods']) == 0:
        print(f"No payment methods found for {cur_profile['name']}.")

    for payment in cur_profile['payment_methods']:
        print(f"Credit card: {payment['credit_card']}      Name on card: {payment['card_name']}       Billing address: {payment['billing_address']}")
    print()

# Function to view the list of available restaurants
def view_restaurants():
    print("\nList of available restaurants:")

    for restaurant in restaurants:
        print(restaurant.name)
    print("")

# Function to view the menu of a specific restaurant
def view_menu():
    restaurant_name = input("Enter the restaurant you wish to see the menu: ")

    for restaurant in restaurants:
        if restaurant_name == restaurant.name:
            restaurant.show_menu()
            return
    print("Restaurant not found.\n")

# Function to add an item to the shopping cart
def add_to_cart():
    restaurant_name = input("Enter the restaurant where you want to add items: ")
    item_name = input("Enter the name of the item to add to the cart: ")
    quantity = int(input("Enter the quantity: "))

    for restaurant in restaurants:
        if restaurant.name == restaurant_name:
            for item in restaurant.menu.keys():
                if item == item_name:
                    user_cart.add_item(restaurant.menu[item], restaurant, quantity)
                    print("Item added to the cart.\n")
                    return
    print("Restaurant or item not found.")

# Function to remove an item from the shopping cart
def remove_from_cart():
    restaurant_name = input("Enter the restaurant where you want to remove an item from the cart: ")
    item_name = input("Enter the name of the item to remove from the cart: ")
    
    result = user_cart.remove_item(restaurant_name, item_name)
    
    if result == "Item removed from the cart.":
        print(result)
    else:
        print("Item not found in the cart.")

# Function to view the contents of the shopping cart
def view_cart():
    user_cart.view_cart()

# Function to check out and complete the order
def check_out():
    user_cart_total = user_cart.cart_total_price()
    print(f"Total price in the cart: ${user_cart_total:.2f}")
    # gets card number of 1st payment method, need logic for checking if payment methods exist & selecting one
    card_number = cur_profile['payment_methods'][0]['card_number']
    print(f"Card on file: {card_number}")

    # Ask the user if they want to pay with the card on file
    choice = input("Do you wish to pay with this card? (yes/no): ")

    if choice.lower() == "yes":
        print("Payment successful. Order has been placed.")
        user_cart.cancel_order()  # Clear the shopping cart after a successful order
    else:
        print("Order not placed. Returning to the main menu to update payment.")

# Function to print the menu options for a logged-in user
def print_options():
    print(f"Hello {cur_profile.name}. Please choose one of the options below.")
    print("1. View restaurants")
    print("2. View restaurant menu")
    print("3. Add item to cart")
    print("4. Remove item from cart")
    print("5. View cart")
    print("6. Check out")
    print("7. Cancel/withdraw current order")
    print("8. Logout")
    print("9. Display profile information")
    print("10. Modify profile information")
    print("11. Modify payment methods")
    print("0. Exit")

# Access MongoDB database
mongo_url = 'mongodb+srv://group24:eyljlgY1EkNeE8AB@group24-project.rv8qyhx.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(mongo_url)
db = client['backend-database'] # database
users_table = db['users'] # users table
restaurants_table = db['restaurants'] # restaurants table
restaurants = []
users = []

# Create a shopping cart for the current user
user_cart = ShoppingCart()

# Initialize the current user profile as None (no user logged in)
cur_profile = None

# Load all users from DB into a list
users_list = list(users_table.find())
for user in users_list:
    users.append(UserProfile(
        user['address'],
        user['phone_number'],
        user['name'],
        user['password'],
        user['email'],
        user['payment_methods']
    ))

# Load all restaurants from DB into a list
restaurant_list = list(restaurants_table.find())
for restaurant in restaurant_list:
    restaurants.append(Restaurant(
        restaurant['id_num'], 
        restaurant['name'],
        restaurant['address'],
        restaurant['category'],
        restaurant['price_range'],
        restaurant['open_time'],
        restaurant['close_time'],
        restaurant['menu']
    ))

# Main application loop
while True:
    if cur_profile is None:  # If no user is logged in
        print("Hello, welcome to our delivery app. Please choose one of the options below.")
        print("0: Register")
        print("1: Login")
        print("2: Exit")
        num = int(input("Enter choice: "))
        if num == 0:
            register()
        elif num == 1:
            cur_profile = login()
        elif num == 2:
            print("Application exited.")
            break
        else:
            print("Invalid input. Please try again.")
    else:
        print_options()
        choice = input("Enter the number of your choice: ")
        # Handle user choices based on the selected option

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
        elif choice == "7":
            user_cart = []
            print("Cart is now empty.")
        elif choice == "8":
            cur_profile = None
            print("You have logged out.\n")
        elif choice == "9":
            show_profile()
        elif choice == "10":
            modify_profile()
        elif choice == "11":
            print(f"\nPlease choose one of the options below.")
            print("0: Add payment method")
            print("1: Modify payment method")
            print("2: Remove payment method")
            print("3: Show all payment methods")
            num = (int)(input("Enter choice: "))
            if num == 0:
                add_payment()
            elif num == 1:
                modify_payment()
            elif num == 2:
                remove_payment()
            elif num == 3:
                show_payments()
            else:
                print("Invalid option return to main menu")
        elif choice == "0":
            print("Thank you for using our app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
