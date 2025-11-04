import mysql.connector 

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enter your password",
        database="bank_system"
    )

