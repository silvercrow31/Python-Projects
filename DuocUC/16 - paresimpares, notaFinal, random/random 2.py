import random
import os

primero=0
segundo=0
tercero=0
pares=0
impares=0

#------------------------------------------------------- INPUTS

primero=random.randint(1,100)

segundo=random.randint(1,100)

tercero=random.randint(1,100)

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

print(f'''
      Sus numeros random fueron generados:
      
      Primero: {primero}
      Segundo: {segundo}
      Tercero: {tercero}
      ''')

if (suma>100):
    print(f"La suma de los tres numeros es {suma}, y es mayor a 100")
    if ((suma%2) != 0):
        print("La suma es impar")
    elif ((suma%2) == 0):
        print("L0a suma es par")