import os
primero=0
segundo=0
tercero=0
pares=0
impares=0

#------------------------------------------------------- INPUTS

primero=int(input("Ingrese el valor del primer número: "))

segundo=int(input("Ingrese el valor del segundo número: "))

tercero=int(input("Ingrese el valor del tercer número: "))

#------------------------------------------------------- PAR O IMPAR
#INTENTAR HACER CON WHILE!!!
if ((primero % 2) != 0):
    impares+=1
elif ((primero % 2) == 0): 
    pares+=1
    
if ((segundo % 2) != 0):
    segundo+=1
elif ((segundo % 2) == 0): 
    pares+=1
    
if ((tercero % 2) != 0):
    impares+=1
elif ((tercero % 2) == 0): 
    pares+=1

#------------------------------------------------------- SUMA  
suma=primero+segundo+tercero

os.system("cls")
#-------------------------------------------------------CONDICIONES
if (suma>100):
    print("Suma de los tres numeros es mayor a 100")
    if ((suma%2) != 0):
        print("La suma es impar")
    elif ((suma%2) == 0):
        print("La suma es par")