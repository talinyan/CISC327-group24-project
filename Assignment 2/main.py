class PaymentMethod:
    def __init__(self, id, cc, name, address):
        self.id = id
        self.cc = cc
        self.name = name
        self.address = address
    
class PaymentManager:
    def __init__(self):
        self.payment_methods = []
        self.id = 0

    def add_payment(self, cc, name, address):
        payment_method = PaymentMethod(self.id, cc, name, address)
        self.payment_methods.append(payment_method)
        print(f"Payment method added with id {self.id}.")
        self.id += 1
    
    def remove_payment(self, id):
        self.payment_methods.pop(id)
        print(f"Payment method with id {id} removed.")
    
    def modify_payment(self, id, cc, name, address):
        payment = self.payment_methods[id]
        payment.cc = cc
        payment.name = name
        payment.address = address
        print(f"Payment method with id {id} modified.")
    
    def show_payments(self):
        if len(self.payment_methods) == 0:
            print("No payment methods have been added.")
            return
        
        print("--------------------------------------------------------------------------------------------------------------\nPayment Methods:")
        for payment in self.payment_methods:
            print(f"ID: {payment.id}        CC: {payment.cc}        Name: {payment.name}        Address: {payment.address}")


class UserProfile:
    def __init__(self, address, phone_number, name, email, password):
        self.address = address
        self.phone_number = phone_number
        self.name = name
        self.password = password
        self.email = email
    
    def valid_credentials(self, phone_number, email, password):
        if len(phone_number) != 10 or not phone_number.isdigit():
            print("Invalid phone number. Please try again.")
            return False
        
        # password must be 8 characters
        if len(password) < 8:
            print("Password too short. Please try again.")
            return False
        
        if "@" not in email:
            print("Invalid email. Please try again.")
            return False
        
        return True
    
    def modify_profile(self, address, phone_number, email, old_password, new_password):
        if self.password == old_password:
            if self.valid_credentials(phone_number, email, new_password):
                self.address = address
                self.phone_number = phone_number
                self.email = email
                self.password = new_password
                print(f"Profile information changed for {self.name}.")
        else:
            print("Password does not match old password. Please try again.")
        
    def show_profile(self):
        print(f"Name: {self.name}       Email: {self.email}        Address: {self.address}     Phone Number: {self.phone_number}")
    
    def login(self, email, password):
        if self.password == password and self.email == email:
            print(f"Logged in. Welcome, {self.name}")
        else:
            print("Invalid email or password. Try again.")
            

def main():
    #payments = PaymentManager()
    #payments.add_payment("1111222233334444", "Bob", "999 Bob Street")
    #payments.show_payments()
    #payments.remove_payment(0)
    #payments.show_payments()

    bob = UserProfile("999 Bob Street", "1112223333", "Bob", "bob@gmail.com", "password123")
    bob.show_profile()
    bob.modify_profile("888 Bob Street", "2223334444", "bob2@gmail.com", "password124", "password321")
    bob.show_profile()
    bob.modify_profile("888 Bob Street", "2223334444", "bob2@gmail.com", "password123", "password321")
    bob.show_profile()


if __name__ == "__main__":
    main()