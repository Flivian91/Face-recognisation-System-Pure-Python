import mysql.connector

conn = mysql.connector.connect(username='root', password='flivian254',host='localhost',database='mydb')
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()