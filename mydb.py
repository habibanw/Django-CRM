import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456789",
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE elderco")

print("Database created successfully")