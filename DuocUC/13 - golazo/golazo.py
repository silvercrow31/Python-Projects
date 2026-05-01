import os
import random

#------------------------------variables-------------------------------
direccionBalon=0                            #para donde va el balon
direccionArquero=0                          #para donde va el arquero
intentos=0                                  #cinco intentos de tiro
cantGoles=0
cantAtajadas=0

#------------------------------codigo ppal-----------------------------



while (intentos<10):
    os.system("cls")

    print('''
        ================GOLAZO================
        1. Angulo superior izq
        2. Angulo superior der.
        3. Angulo inferior izq.
        4. Angulo inferior der.
        5. Centro
        
        ''')

    direccionBalon=int(input("Elija dirección: "))

    direccionArquero = random.randint(1,5)
    
    
    
    
    if (direccionArquero==direccionBalon):
        print("ATAJO EL ARQUERO!")
        intentos+=1
        cantAtajadas+=1
        os.system("pause")
        
    elif (direccionArquero!=direccionBalon):
        print("GOLAZO!!!")    
        intentos+=1
        cantGoles+=1
        os.system("pause")
        
    else:
        print("error")
        os.system("pause")

print(f'''
      -------------------MARCADOR FINAL-------------------
                GOLES: {cantGoles}
                ATAJADAS: {cantAtajadas}
                
      ''')

