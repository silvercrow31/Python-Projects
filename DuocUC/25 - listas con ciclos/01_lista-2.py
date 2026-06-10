# Crear una lista de 5 nombres
# la regla es que ningún nombre se repita!!!
import os

os.system("cls")

nombresList = []

# V1
# i = 0

# while i < 5:
#     nombre = str(input(f"Ingrese nombre {i+1}:    ")).strip()
#     if nombre in nombresList:
#         print("ERROR: el nombre no se puede repetir")
#     elif nombre not in nombresList:
#         i += 1
#         nombresList.append(nombre)
#         i = len(nombresList)


# print(f"Lista de nombres:   {nombresList}")
# print(f"N° de nombres ingresados:   {i}")

# V2
while True:
    if len(nombresList) == 5:
        break
    nombre = str(input("Ingrese nombre: "))
    if nombre in nombresList:
        print("ERROR: el nombre ya existe. ")
    else:
        nombresList.append(nombre)

nombresList.sort()
print(nombresList)
