import mysql.connector

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql2004',
    database='bolt_db'
)

cursor = db_connection.cursor()
cursor = db_connection.cursor(buffered=True)