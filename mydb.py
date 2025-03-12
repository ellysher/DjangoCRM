import mysql.connector

# Establish connection
dataBase = mysql.connector.connect(
    host='localhost',
    user='elisha',
    password='elisha001'
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database (without spaces in the name)
cursorObject.execute("CREATE DATABASE `quantum db`")

print("Database created successfully!")
