from user_profile import UserProfile
from shopping_cart import ShoppingCart
from restaurant import Restaurant
import unittest


#helper functions: to view the list of available restaurants
def view_restaurants(restaurants):
    restaurant_list = [restaurant.name for restaurant in restaurants]
    return restaurant_list



class TestApp(unittest.TestCase):
    def setUp(self):
        # Initialize any necessary objects or data before each test
        self.user = UserProfile("Test Address", "1234567890", "Test User", "test@test.com", "password123")
        self.cart = ShoppingCart()
        self.restaurant = Restaurant("1", "Test Restaurant", "Test Address", "Test Category", "$$", "10:00 AM", "9:00 PM", {})
        self.restaurants = [
            Restaurant("1", "Restaurant A", "Address A", "Category A", "$$", "10:00 AM", "9:00 PM", {}),
            Restaurant("2", "Restaurant B", "Address B", "Category B", "$$", "11:00 AM", "8:00 PM", {}),
            Restaurant("3", "Restaurant C", "Address C", "Category C", "$", "9:00 AM", "10:00 PM", {})
        ]

    def test_add_payment(self):
        # Test adding payment method
        payment_info = {
            "credit_card": "1111222233334444",
            "cvv": "111",
            "billing_address": "1 Queen St",
            "first_name": "John",
            "last_name": "Doe"
        }
        message = self.user.add_payment(payment_info)
        self.assertEqual(message, "Payment method added.")

    def test_remove_payment(self):
        # Test removing a payment method
        self.user.add_payment({
            "credit_card": "1111222233334444",
            "cvv": "111",
            "billing_address": "1 Queen St",
            "first_name": "John",
            "last_name": "Doe"
        })
        message = self.user.remove_payment(0)
        self.assertEqual(message, "Payment method removed.")

    def test_modify_payment(self):
        # Add a payment method
        self.user.add_payment({
            "credit_card": "1111222233334444",
            "cvv": "111",
            "billing_address": "1 Queen St",
            "first_name": "John",
            "last_name": "Doe"
        })

        # Modify the payment method
        modified_payment_info = {
            "credit_card": "5555666677778888",
            "cvv": "222",
            "billing_address": "2 King St",
            "first_name": "Jane",
            "last_name": "Smith"
        }

        message = self.user.modify_payment(0, modified_payment_info)
        self.assertEqual(message, "Payment method modified.")

    def test_check_out(self):
        # Set the current user profile to the test user
        cur_profile = self.user

        # Add items to the shopping cart
        item1 = {"name": "Item1", "price": 10.0, "quantity": 2}
        item2 = {"name": "Item2", "price": 5.0, "quantity": 3}

        self.cart.add_item(item1, self.restaurant)
        self.cart.add_item(item2, self.restaurant)

        # Perform the checkout
        user_cart_total = self.cart.cart_total_price()
        card_number = self.user.payment_methods[0]["credit_card"]
        payment_message = self.cart.check_out(user_cart_total, card_number)

        # Assertions
        self.assertEqual(payment_message, "Payment successful. Order has been placed.")
        self.assertEqual(len(self.cart.cart), 0)  # Cart should be cleared after a successful order

    def test_modify_profile(self):
        # Initialize a test user profile
        test_user = UserProfile("Test Address", "1234567890", "Test User", "test@test.com", "password123")
        
        # Modify the profile information
        new_phone_number = "9876543210"
        new_email = "newemail@test.com"
        new_address = "New Address"
        old_password = "password123"
        new_password = "newpassword123"
        
        test_user.modify_profile(new_phone_number, new_email, new_address, old_password, new_password)
        
        # Check if the profile information is modified
        self.assertEqual(test_user.phone_number, new_phone_number)
        self.assertEqual(test_user.email, new_email)
        self.assertEqual(test_user.address, new_address)
        self.assertEqual(test_user.password, new_password)


    def test_user_registration(self):
        # Initialize a test user profile
        test_user = UserProfile("", "", "", "", "")
        
        # Test valid user registration
        valid_name = "Test User"
        valid_phone_number = "1234567890"
        valid_email = "test@test.com"
        valid_address = "Test Address"
        valid_password = "password123"
        
        registration_result = test_user.register(valid_name, valid_phone_number, valid_email, valid_address, valid_password)
        
        # Check if the registration was successful
        self.assertEqual(registration_result, "Account created for Test User. Please login.")

        # Test invalid user registration (e.g., invalid phone number)
        invalid_name = "Invalid User"
        invalid_phone_number = "invalid"
        invalid_email = "invalid_email.com"
        invalid_address = "Invalid Address"
        invalid_password = "short"
        
        registration_result = test_user.register(invalid_name, invalid_phone_number, invalid_email, invalid_address, invalid_password)
        
        # Check if the registration fails with invalid inputs
        self.assertEqual(registration_result, "Invalid phone number. Please try again.")


    def test_user_login_valid(self):
        # Initialize a test user profile
        test_user = UserProfile("Test Address", "1234567890", "Test User", "test@test.com", "password123")
        
        # Test valid user login
        valid_email = "test@test.com"
        valid_password = "password123"
        
        login_result = test_user.login(valid_email, valid_password)
        
        # Check if the login is successful
        self.assertEqual(login_result, "You have logged in successfully.")

    def test_user_login_invalid(self):
        # Initialize a test user profile
        test_user = UserProfile("Test Address", "1234567890", "Test User", "test@test.com", "password123")
        
        # Test invalid user login with incorrect email
        invalid_email = "invalid_email@test.com"
        valid_password = "password123"
        
        login_result = test_user.login(invalid_email, valid_password)
        
        # Check if the login fails with incorrect email
        self.assertEqual(login_result, "Invalid email or password. Please try again.")

        # Test invalid user login with incorrect password
        valid_email = "test@test.com"
        invalid_password = "incorrect_password"
        
        login_result = test_user.login(valid_email, invalid_password)
        
        # Check if the login fails with incorrect password
        self.assertEqual(login_result, "Invalid email or password. Please try again.")


    def test_view_restaurants(self):
        # Call the view_restaurants function with the test restaurants list
        restaurant_names = view_restaurants(self.restaurants)

        # Check if the list of restaurant names matches the expected result
        expected_names = ["Restaurant A", "Restaurant B", "Restaurant C"]
        self.assertEqual(restaurant_names, expected_names)
    # Set the current user profile to the test user
        cur_profile = self.user

        # Add a test restaurant to the list of restaurants
        test_restaurant = Restaurant("4", "Test Restaurant", "Test Address", "Test Category", "$$", "10:00 AM", "9:00 PM", {
            "Item1": {"name": "Item1", "price": 10.0},
            "Item2": {"name": "Item2", "price": 5.0},
        })
        self.restaurants.append(test_restaurant)

        # Call the view_menu function with the test restaurant name
        restaurant_name = "Test Restaurant"
        expected_menu = {
            "Item1": {"name": "Item1", "price": 10.0},
            "Item2": {"name": "Item2", "price": 5.0},
        }
        menu = cur_profile.view_menu(restaurant_name, self.restaurants)

        # Check if the menu matches the expected result
        self.assertEqual(menu, expected_menu)
    
    def test_add_to_cart(self):
        # Set the current user profile to the test user
        cur_profile = self.user

        # Call the add_to_cart function to add an item
        restaurant_name = "Test Restaurant"
        item_name = "Item1"
        quantity = 2
        expected_message = "Item added to the cart."

        message = cur_profile.add_to_cart(restaurant_name, item_name, quantity, self.restaurants)

        # Check if the message matches the expected result
        self.assertEqual(message, expected_message)

    def test_remove_from_cart(self):
        # Set the current user profile to the test user
        cur_profile = self.user

        # Add an item to the cart
        cur_profile.add_to_cart("Test Restaurant", "Item1", 2, self.restaurants)

        # Call the remove_from_cart function to remove an item
        restaurant_name = "Test Restaurant"
        item_name = "Item1"
        expected_message = "Item removed from the cart."

        message = cur_profile.remove_from_cart(restaurant_name, item_name)

        # Check if the message matches the expected result
        self.assertEqual(message, expected_message)

    # def test_cancel_order(self):
    #     # Your test code for canceling an order

    def test_cart_total_price(self):
        # Set the current user profile to the test user
        cur_profile = self.user

        # Add a test restaurant to the list of restaurants
        test_restaurant = Restaurant("4", "Test Restaurant", "Test Address", "Test Category", "$$", "10:00 AM", "9:00 PM", {
            "Item1": {"name": "Item1", "price": 10.0},
            "Item2": {"name": "Item2", "price": 5.0},})

        # Add items to the cart
        cur_profile.add_to_cart("Test Restaurant", "Item1", 2, self.restaurants)
        cur_profile.add_to_cart("Test Restaurant", "Item2", 3, self.restaurants)

        # Calculate the total price using the cart_total_price function
        total_price = cur_profile.cart_total_price()

        # Calculate the expected total price based on the added items
        expected_total_price = (2 * 10) + (3 * 5)

        # Check if the calculated total price matches the expected total price
        self.assertEqual(total_price, expected_total_price)

    def test_valid_item_quantity(self):
        # Create a test user profile and a shopping cart
        cur_profile = self.user
        cart = self.cart

        # Define a valid item quantity
        valid_quantity = 5

        # Check if the item quantity is valid using the function
        is_valid = cart.valid_item_quantity(valid_quantity)

        # Assert that the item quantity is valid
        self.assertTrue(is_valid)


    def test_invalid_item_quantity(self):
        # Create a test user profile and a shopping cart
        cur_profile = self.user
        cart = self.cart

        # Define an invalid item quantity (e.g., a negative quantity)
        invalid_quantity = -1

        # Check if the item quantity is invalid using the function
        is_valid = cart.valid_item_quantity(invalid_quantity)

        # Assert that the item quantity is invalid
        self.assertFalse(is_valid)



if __name__ == '__main__':
    unittest.main()