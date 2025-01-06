import mysql.connector

database = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = '@Baseball95!',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE Tutorial")

print("All Done!")