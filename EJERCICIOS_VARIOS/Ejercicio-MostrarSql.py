import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='practica'
)
mycursor = mydb.cursor()
sql = 'INSERT INTO sueldos (seccion,sucursal,sueldo) VALUES (%s, %s,%s)'

option=int(input('Ingrese datos, precione 0 para finalizar'))
while option:
    suc=input('Ingrese sucursa [E,A,C]: ')
    sec=input('Ingrese SECTOR[I,A,C,T]: ')
    sueldo=int(input('Ingrese salario: '))
    if sec=='I':
        seccion='Informática'
    elif sec=='A':
        seccion='Atención al publico'
    elif sec=='C':
        seccion='Contabilidad'
    elif sec=='T':
        seccion='Transporte'

    if suc=='E':
        sucursal='Encarnacion'
    elif suc=='A':
        sucursal='Asuncion'
    elif suc=='C':
        sucursal='Ciudad del Este'

    values=(seccion,sucursal,sueldo)
    mycursor.execute(sql, values)
    mydb.commit()
    print(mycursor.rowcount, 'Insertado')
    option=int(input('Para ingrear 0 para finalizar'))


mycursor = mydb.cursor()
mycursor.execute("SELECT SUM(sueldo),sucursal,seccion FROM `sueldos` GROUP BY seccion,sucursal")
myresult = mycursor.fetchall()
encarnacion=[0,0,0,0]
asuncion=[0,0.0,0,0]
CiudadE=[0,0,0,0]
auxSuc=0
auxSec=0
print('\t \t Encarnacion \t Asuncion \t Ciudad del este')
for i in myresult:
    if i[2]=='Informatica':
        auxSec=0
    elif i[2]=='Atención al pub':
        auxSec=1
    elif i[2]=='Transporte':
        auxSec=2
    elif i[2]=='Contabilidad':
        auxSec=3

    if i[1]== 'Encarnacion':
        encarnacion[auxSec]=i[0]
    elif i[1]== 'Asuncion':
        asuncion[auxSec]=i[0]
    elif i[1]=='Ciudad del Este':
        CiudadE[auxSec]=i[0]
    

print(f'Informatica\t\t{encarnacion[0]} \t {asuncion[0]} \t\t {CiudadE[0]}')
print(f'Atencion al C\t\t{encarnacion[1]} \t {asuncion[1]} \t\t {CiudadE[1]}')
print(f'Trasporte \t\t{encarnacion[2]} \t {asuncion[2]} \t\t {CiudadE[2]}')
print(f'Contabilidad\t\t{encarnacion[3]} \t {asuncion[3]} \t\t {CiudadE[3]}')

