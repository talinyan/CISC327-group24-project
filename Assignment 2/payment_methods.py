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
        print("--------------------------------------------------------------------------------------------------------------")


# Example usage:
# def main():
#     payments = PaymentManager()
#     payments.add_payment("1111222233334444", "Bob", "999 Bob Street")
#     payments.show_payments()
#     payments.remove_payment(0)
#     payments.show_payments()

# if __name__ == "__main__":
#     main()