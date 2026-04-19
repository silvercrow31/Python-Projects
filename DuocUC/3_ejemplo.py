import os

nombre = str(input("Ingrese nombre: "))
edad = int(input("Ingrese edad: "))

os.system("cls")

print(
    f'''
    ----------------Ticket----------------
    Nombre: {nombre} 
    Edad: {edad}
    --------------------------------------
    '''
)

