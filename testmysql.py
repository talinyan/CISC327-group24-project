import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Cxf20020425.",
  database="cisc327"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("select item_name, item_price from   restaurant_item left join restaurants on restaurant_item.restaurant_id=restaurants.restaurant_id where restaurants.restaurant_name='restaurant1'"); 

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0],x[1])
