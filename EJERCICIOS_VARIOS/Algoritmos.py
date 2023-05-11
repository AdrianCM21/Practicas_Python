# 1. Lee 6 pares de palabras e informa cuantos de estos pares son palabras iguales.
# a. Comparación de cadenas – 1pto
# b. Uso de contadores – 1pto

# cont=0
# for item in range(6):
#     palabra1=input('ingrese variable 1')
#     palabra2=input('ingrese variable 2') 
#     if palabra1==palabra2:
#         cont=cont+1
#         print('hay una considencia')
#     else: 
#      print('No hay una considencia')
# print('Hay un total ',cont)
    


# 2. Lee un numero e imprime el valor siguiente a este
# a. Lectura. 1pto
# b. Calculo. 1pto
# c. Impresión de variables. 1pto

# numsig=int(input('Ingrese numero'))
# print('El numero siguiente es ',numsig+1)


# 3. Lee dos números por teclado e imprime el resultado de la resta de dichos números,
# informe si la resta es o no menor a 10.
# a. Cálculo de dos variables. 1pto
# b. Uso de condicionales simples. 1pto


# var1=int(input('Ingrese variable 1: '))
# var2=int(input('Ingrese variable 2: '))
# print(f'La resta de {var1} - {var2} = ',var1-var2)

# 4. Crea un bucle que imprima los números del 1 al 35
# a. Impresión por medio de bucles. 1pto
# b. Definición de un bucle. 1pto3


# for item in range(35):
#     print(item+1)
    


# 5. Resuelve el siguiente planteo:
# a. Cree una matriz de 3x3 elementos. 1pto
# b. Cargue la misma con 9 valores utilizando un bucle. 2ptos
# c. Imprima el valor más alto del arreglo. 1pto

# vari=[[0,0,0],[0,0,0],[0,0,0]]
# for a in range(3):
#     for b in range(3):
#         vari[a][b] = int(input('Ingress numero1'))
        


# 6. Cree un vector de diez elementos por medio del método burbuja ordene los mismos,
# imprima el vector ordenado.
# a. Aplicación del Método burbuja. 1pto
# b. Uso de variables auxiliares. 1pto
# c. Impresión del vector ordenado. 1pto


# 1


# 7. Por medio de una variable auxiliar y un bucle, lea diez números y halle el mayor de
# estos, imprima el mismo.
# a. Uso de variables auxiliares y condicionales. 2ptos


# auxMayor=0
# numeros=[]
# for item in range(10):
#     numeros.append(int(input()))
#     if numeros[item]>auxMayor:
#         auxMayor=numeros[item]
# print('el numero mayor es:',auxMayor)
        


    


# 8. Lea números mientras estos no sean cero, cuente la cantidad de negativos, así como la
# cantidad de positivos, sume todos los valores positivos. Finalmente imprima los
# contadores, así como el sumador.
# a. Ciclo – 1pto
# b. Acumuladores y contadores – 1pto
# c. Condicionales – 1pto

# negativo=0
# positivo=0
# numero=int(input)
# while numero != 0:
#     if numero>0:
#         positivo=numero
#     else:
#         negativo=numero
#     numero=int(input)
# print(f'suma de negativo {negativo} y positivo {positivo}')

        
        




# 9. Se desea totalizar los pagos a empleados por sección y sucursal para esto escriba un
# programa que permita:
# a. Ingresar la sucursal.
# i. E –Encarnación
# ii. A – Asunción
# iii. C – Ciudad del Este
# b. Ingresar la sección
# iv. I- Informática
# v. A- Atención al publico
# vi. C – Contabilidad
# vii. T- Transporte
# c. Importe del sueldo
# d. Antigüedad
# Para empleados con una antigüedad mayor a 5 años se debe sumar un 10% del
# importe del sueldo.
# Al finalizar se deberá imprimir el siguiente resumen, se cuenta con 20 empleados




for item in range(20):  
    suc=input('Ingrese sucursa [E,A,C]: ')
    sec=input('Ingrese SECTOR[I,A,C,T]: ')
    inp=int(input('Ingrese: '))
    ant=int(input('Ingrese: '))
        
    if suc=='E':
        if sec=='I':
            EI='Informática'
        elif sec=='A':
            seccion='Atención al publico'
        elif sec=='C':
            seccion='Ciudad del este'
        elif sec=='T':
            seccion='Transporte'
    elif suc=='A':
        if sec=='I':
            seccion='Informática'
        elif sec=='A':
            seccion='Atención al publico'
        elif sec=='C':
            seccion='Ciudad del este'
        elif sec=='T':
            seccion='Transporte'
    elif suc=='C':
        if sec=='I':
            seccion='Informática'
        elif sec=='A':
            seccion='Atención al publico'
        elif sec=='C':
            seccion='Ciudad del este'
        elif sec=='T':
            seccion='Transporte'


    if sec=='I':
        seccion='Informática'
    elif sec=='A':
        seccion='Atención al publico'
    elif sec=='C':
        seccion='Ciudad del este'
    elif sec=='T':
        seccion='Transporte'



