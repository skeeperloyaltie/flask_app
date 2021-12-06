import sqlite3 as sql
conn = sql.connect('database.db')

conn.execute('UPDATE TABLE product_movement (movementID INTEGER PRIMARY KEY, productName TEXT, Timing timestamp, fromlocation TEXT, tolocation TEXT,QTY INTEGER)')
print ("Table productmovement Done")



conn.execute("INSERT INTO Balance (locationName,productName,QTY)VALUES('Office Suite []','Valary','10')")
print ("Table balance c successfully")