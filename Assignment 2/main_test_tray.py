from profile_manager import UserProfile

# validate credentials
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

def main():
    def register():
        while True:
            name = input("Enter your name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Choose a password (must be at least 8 characters): ")
            if valid_credentials(phone_number, email, password):
                profiles.append(UserProfile(address, phone_number, name, email, password))
                break
    
    def login():
        while True:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            for p in profiles:
                if p.login(email, password):
                    print(f"You have logged in successfully.\n")
                    return p
                else:
                    print("Invalid email or password. Please try again.\n")
    
    def modify_profile():
        while True:
            phone_number = input("Enter your new phone number: ")
            email = input("Enter your new email: ")
            address = input("Enter your new address: ")
            old_password = input("Enter your old password: ")
            new_password = input("Choose a new password (must be at least 8 characters): ")
            if valid_credentials(phone_number, email, new_password):
                cur_profile.modify_profile(address, phone_number, email, old_password, new_password)
                break
    
    def add_payment():
        cc = input("Enter your credit card information: ")
        name = input("Enter the name on the card: ")
        address = input("Enter the address on the card: ")
        cur_profile.payment_manager.add_payment(cc, name, address)
    
    def modify_payment():
        id = int(input("Enter the id of the payment method to modify: "))
        cc = input("Enter your credit card information: ")
        name = input("Enter the name on the card: ")
        address = input("Enter the address on the card: ")
        cur_profile.payment_manager.modify_payment(id, cc, name, address)

    profiles = []
    cur_profile = None

    while True:
        if cur_profile == None: # If not logged in
            print("Hello, welcome to our delivery app. Please choose one of the options below.")
            print("0: Register")
            print("1: Login")
            print("2: Exit")
            num = (int)(input("Enter choice: "))
            if num == 0:
                register()
            elif num == 1:
                cur_profile = login()
            elif num == 2:
                print("Application exited.")
                break
            else:
                print("Invalid input. Please try again.")
        else: # If logged in, show different options
            print(f"Hello {cur_profile.name}. Please choose one of the options below.")
            print("0: Logout")
            print("1: Display profile information")
            print("2: Modify profile information")
            print("3: Modify payment methods")
            num = (int)(input("Enter choice: "))
            if num == 0:
                cur_profile = None
                print("You have logged out.\n")
            elif num == 1:
                cur_profile.show_profile()
            elif num == 2:
                modify_profile()
            elif num == 3:
                print(f"\nPlease choose one of the options below.")
                print("0: Add payment method")
                print("1: Remove payment method")
                print("2: Modify payment method")
                print("3: Show all payment methods")
                num = (int)(input("Enter choice: "))
                if num == 0:
                    add_payment()
                elif num == 1:
                    modify_payment()
                elif num == 2:
                    id = int(input("Enter the id of the payment method to remove:"))
                    cur_profile.payment_manager.remove_payment(id)
                elif num == 3:
                    cur_profile.payment_manager.show_payments()

if __name__ == "__main__":
    main()