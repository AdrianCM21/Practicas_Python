import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='practica'
)
mycursor = mydb.cursor()
sql = 'INSERT INTO pract9i (A, B) VALUES (%s, %s)'
val = ('Juan', 'Perez')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, 'Insertado')