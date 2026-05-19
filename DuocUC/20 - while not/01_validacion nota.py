import os

nota = float(input("Ingrese la nota: "))

while not (1 <= nota <= 7):
    print("ERROR, válido entre 1 y 7")
    nota = float(input("Ingrese la nota: "))

print("Nota cargada exitosamente!!!!!")
