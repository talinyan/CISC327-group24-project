import mysql.connector
class_order = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Pasta": 6.49,
    "Salad": 3.99,
    "Soda": 1.99
}

class order:
    def __init__(self,order_id):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cxf20020425.",
        database="cisc327"
        )

        print(mydb)

        mycursor = mydb.cursor()

        mycursor.execute("select restaurant_id,stats, total_price from orders where order_id='%s'" % order_id)

        myresult = mycursor.fetchall()

        for x in myresult:        
            self.order_id = order_id
            self.restaurant_id =x[0] 
            self.stats=x[1]
            self.total_price=x[2]
            print(x)

    def place_order(self):
        self.order_stats="placed"

    def change_stats(stats):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cxf20020425.",
        database="cisc327"
        )

        print(mydb)

        mycursor = mydb.cursor()
        

        mycursor.execute(" update orders  set stats = '%s'" %stats %" where order_id='12'")

        print("statts changed to" % stats )

    def order_stats(self):
        return self.order_stats
    
    def withdraw_order(self):
        self.order_stats="withdraw"




# Function to display the menu
#def display_menu():
#    print("Menu:")
#    for item, price in menu.items():
#        print(f"{item}: ${price:.2f}")

# Function to take orders
#def take_order():
#    order = {}
#    while True:
#        display_menu()
#        item = input("Enter the item you want to order (or 'done' to finish): ")
#        if item.lower() == "done":
#            break
#        if item in menu:
#            quantity = int(input(f"How many {item}s would you like to order? "))
#            if item in order:
#                order[item] += quantity
#            else:
#                order[item] = quantity
#        else:
#            print("Item not found in the menu. Please choose from the menu.")

#    return order

# Function to calculate the total cost of the order
#def calculate_total(order):
#    total_cost = 0
#    for item, quantity in order.items():
#        total_cost += menu[item] * quantity
#    return total_cost

# Main function
def main():
    order1=order(12)
    order.change_stats("deliverd")

    #print("Welcome to the restaurant!")
    #order = take_order()
    #if order:
    #    print("\nYour order:")
    #    for item, quantity in order.items():
    #        print(f"{item}: {quantity}")
    #    total_cost = calculate_total(order)
    #    print(f"Total cost: ${total_cost:.2f}")
    #else:
    #    print("No items were ordered. Thank you for visiting!")

if __name__ == "__main__":
    main()


