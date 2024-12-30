import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password123',
)

with connection.cursor() as cursor:
    cursor.execute("CREATE DATABASE IF NOT EXISTS CRM")
    print("Database 'CRM' created successfully!")


