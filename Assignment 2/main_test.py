from restaurant import Restaurant
import csv
restaurant_file = 'restaurant2.csv'







restaurants = []
with open(restaurant_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        restaurant = Restaurant(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        restaurants.append(restaurant)

first = restaurants[1]
print (first.load_menu2())
