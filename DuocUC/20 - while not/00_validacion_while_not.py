import os

sexo = str(input("Ingrese sexo: ")).strip().upper()

while not (sexo == "F" or sexo == "M"):
    print("ERROR, válido F/M")
    sexo = str(input("Ingrese sexo: ")).strip().upper()

print("Dato cargado exitosamente!!!!!")
