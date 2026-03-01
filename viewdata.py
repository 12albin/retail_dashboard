import mysql.connector

connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='demo'

)

cursor=connection.cursor()

cursor.execute("Select * from demo.onlineretail limit 5;")
rows=cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()