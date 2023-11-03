class UserProfile:
    def __init__(self, address, phone_number, name, email, password, payment_methods=[]):
        self.register(address, phone_number, name, email, password, payment_methods)
    
    def register(self, address, phone_number, name, email, password, payment_methods=[]):
        if not self.valid_credentials(phone_number, email, password):
            return "Invalid phone number. Please try again."
        self.address = address
        self.phone_number = phone_number
        self.name = name
        self.email = email
        self.password = password
        self.payment_methods = payment_methods
        return "Account created for " + name + ". Please login."

    def valid_credentials(self, phone_number, email, password):
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

    def add_payment(self, payment_info):
        self.payment_methods.append({
            "credit_card": payment_info["credit_card"],
            "cvv": payment_info["cvv"],
            "billing_address": payment_info["billing_address"],
            "card_name": payment_info["first_name"] + payment_info["last_name"]
        })
        return "Payment method added."
    
    def remove_payment(self, id):
        self.payment_methods.pop(id)
        return "Payment method removed."

    def modify_payment(self, id, payment_info):
        self.payment_methods[id] = ({
            "credit_card": payment_info["credit_card"],
            "cvv": payment_info["cvv"],
            "billing_address": payment_info["billing_address"],
            "card_name": payment_info["first_name"] + payment_info["last_name"]
        })
        return "Payment method modified."
    
    def modify_profile(self, address, phone_number, email, old_password, new_password):
        if self.password == old_password:
            if self.valid_credentials(phone_number, email, new_password):
                self.address = address
                self.phone_number = phone_number
                self.email = email
                self.password = new_password
                print(f"Your profile information has been changed.\n")
        else:
            print("Password does not match old password. Please try again.\n")
        
    def show_profile(self):
        print(f"Name: {self.name}       Email: {self.email}        Address: {self.address}     Phone Number: {self.phone_number}\n")
    
    def login(self, email, password):
        if self.password == password and self.email == email:
            return "You have logged in successfully."
        else:
            return "Invalid email or password. Please try again."


test_user = UserProfile("Test Address", "1234567890", "Test User", "test@test.com", "password123")

# Modify the profile information
new_phone_number = "9876543210"
new_email = "newemail@test.com"
new_address = "New Address"
old_password = "password123"
new_password = "newpassword123"

test_user.modify_profile(new_phone_number, new_email, new_address, old_password, new_password)

test_user.show_profile()