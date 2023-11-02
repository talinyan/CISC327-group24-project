import pymongo
from restaurant import restaurants_all

# When running this file, accesses all restaurants and their menus, and allows
# adding them to DB table, viewing the DB table, or dropping the table.

def main():
    # Access MongoDB database
    mongo_url = 'mongodb+srv://group24:eyljlgY1EkNeE8AB@group24-project.rv8qyhx.mongodb.net/?retryWrites=true&w=majority'
    client = pymongo.MongoClient(mongo_url)
    db = client['backend-database'] # database
    restaurants_table = db['restaurants'] # restaurants table

    while(True):
        print("0: Exit")
        print("1: Add all restaurants to DB")
        print("2: View all restaurants in DB")
        print("3: Drop restaurant table")
        choice = (int)(input("Enter choice: "))
        if choice == 0:
            break
        elif choice == 1:
            restaurants = list(restaurants_table.find())
            if restaurants:
                print("All restaurants already in DB.\n")
            else:
                for r in restaurants_all:
                    restaurant_data = {
                        "id_num": r.id_num,
                        "name": r.name,
                        "address": r.address,
                        "category": r.category,
                        "price_range": r.price_range,
                        "open_time": r.open_time,
                        "close_time": r.close_time,
                        "menu": r.menu
                    }
                    restaurants_table.insert_one(restaurant_data)
                print("Restaurants added.\n")
        elif choice == 2:
            restaurants = list(restaurants_table.find())
            if len(restaurants) == 0:
                print("Table empty. Add restaurants.\n")
            else:
                for r in restaurants:
                    print(r)
        elif choice == 3:
            restaurants_table.drop()
            print("Table dropped.")
        else:
            print("Invalid input. Please try again.\n")

if __name__ == '__main__':
    main()