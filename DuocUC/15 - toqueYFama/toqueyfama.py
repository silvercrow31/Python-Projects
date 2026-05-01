import os
import random

numeroSecreto=0
intentos=5
apuesta=0
distancia=0


os.system("cls")

print('''
      
                        Toque y Fama
        
        Adivine el numero sorteado, tendrá 5 intentos.
        ¡Elija su opción!
      ''')

opDeseaJugar=str(input('''      
                        ¿Desea jugar? 
        1: Si 
        2: No''')).strip()

if opDeseaJugar=="2":               #salida temprana?
    print("Saliendo de la aplicación...")

elif opDeseaJugar=="1":
    
    os.system("cls")

            
    print(f'''
          ----------------- TOQUE Y FAMA -----------------
          Debes adivinar un número entre 1 y 20. Tienes
          {intentos} intentos.
          ''')

    while intentos > 0:
        numeroSecreto=random.randint(1,20)
        apuesta=int(input("Ingresa tu apuesta: "))
        distancia=abs(numeroSecreto-apuesta)
        
        if distancia>2:
            print("LEJOS")
        if distancia==2:
            print("CERCA")
        if distancia==1:
            print("MUY CERCA")
        if distancia==0:
            print("FAMA")
        print(f"Número: {numeroSecreto}")
        
        
        intentos -= 1


