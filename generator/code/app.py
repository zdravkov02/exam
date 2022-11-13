import os
import mysql.connector
import random
import time

a = ['Blue', 'Black', 'Yellow', 'White', 'Green', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Red']
b = ['Tigers', 'Lions', 'Crocodiles', 'Horses', 'Donkeys', 'Dogs', 'Cats', 'Bears', 'Pandas', 'Coalas', 'Chameleons', 'Lizards']
c = ['Fat', 'Slim', 'Fast', 'Slow', 'Tall', 'Short', 'Weak', 'Strong']
d = ['Eat', 'Dream', 'Like', 'Adore', 'Trow', 'Love', 'Dislike']
e = ['Oranges', 'Bananas', 'Tomatoes', 'Potatoes', 'Onions', 'Cucumbers', 'Nuts']

print('Started. Looking for new fun facts ...')

while True:
    s = a[random.randrange(10)] + " " + b[random.randrange(11)] + " Are " + c[random.randrange(7)] + " And " + d[random.randrange(6)] + " " + e[random.randrange(6)]

    print("New fun fact discovered: " + s)

    try:
      mydb = mysql.connector.connect(
        host = os.getenv('DB_HOST', "con-storage"),
        user = os.getenv('DB_USER', "root"),
        password = os.getenv('DB_PASS', "ExamPa$$w0rd"),
        database = os.getenv('DB_NAME', "animal_facts")
      )
      cursor = mydb.cursor()
      cursor.execute("INSERT INTO facts (fact) VALUES ('" + s + "')")
      cursor.close()
      mydb.commit()
    except:
      print("ERROR: Database communication error.")

    t = random.randrange(60,90)
    print(f'Sleep for {t} seconds')
    time.sleep(t)
