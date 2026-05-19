import os
import random

num1=0
num2=0
numeroGenerado=0
numeroFinal=0
intentos=3
pista=0
apuesta=0
contadorIntentos=1
diferencia1=0
diferencia2=0

os.system("cls")

while True:                             #input num1
    num1=int(input("Ingrese límite inferior: "))
    if (num1>=0):
        break
    else:
        print("ERROR: El límite inferior debe ser un entero positivo o cero. ")
        os.system("pause")
        
while True:                             #input num2
    num2=int(input("Ingrese límite superior: "))
    if ((num2>0) and (num2>num1)):
        break
    
    elif (num2<=0):
        print("ERROR: El límite superior debe ser un entero positivo. ")
        os.system("pause")
    
    elif (num2<num1):
        print("ERROR: El límite superior debe ser mayor que el primer número. ")
        os.system("pause")
    
    else:
        print("ERROR. ")
        os.system("pause")
        
numeroGenerado = random.randint(num1, num2)

#verifica si es par o impar y ajusta acorde a reglas
if (numeroGenerado%2!=0):
    if ((numeroGenerado+1)<=num2):
        numeroFinal=numeroGenerado+1
    
    elif (numeroGenerado+1)>num2:   ###
        numeroFinal=numeroGenerado-1
elif(numeroGenerado%2==0):
    numeroFinal=numeroGenerado

#JUEGO

while intentos!=0:
    while True:                             #input num1
        apuesta=int(input("Intente adivinar: "))
        if (apuesta>=0):
            break
        else:
            print("ERROR: El número ingresado debe ser un entero positivo o cero. ")
            os.system("pause")    
    
    intentos-=1
    
    if apuesta==numeroFinal:
        print(f"Felicidades, pudiste adivinar. en tu intento n°{contadorIntentos} ")
        break
    #primer intento
    elif (apuesta!=numeroFinal) and (contadorIntentos==1):
        diferencia1=abs(numeroFinal-apuesta)
        if apuesta>numeroFinal:
            print("Su número es MAYOR que el generado. ")
        elif apuesta <numeroFinal:
            print("Su número es MENOR que el generado")
        contadorIntentos+=1
    #segundo intento
    elif (apuesta!=numeroFinal) and (contadorIntentos==2):
        diferencia2=abs(numeroFinal-apuesta)
        if apuesta>numeroFinal:
            print("Su número es MAYOR que el generado. ")
        elif apuesta <numeroFinal:
            print("Su número es MENOR que el generado")
        if diferencia2<diferencia1:
            print("PISTA: El SEGUNDO intento estuvo más cerca. ")
        elif diferencia1<diferencia2:
            print("PISTA: El PRIMER intento estuvo más cerca. ")
        contadorIntentos+=1
    #tercer intento
    elif (apuesta!=numeroFinal) and (contadorIntentos==3):
        contadorIntentos+=1
        print(f"Perdiste. El número era {numeroFinal}")
        
        
print(f'''Debugging:
        diferencia1 {diferencia1}
        diferencia2: {diferencia2}
        numerogenerado {numeroGenerado}
        numerofinal {numeroFinal}''')