import os

# 1. Carga de nota con while not()
nota = float(input("Ingrese nota: "))
while not (1 <= nota <= 7):
    print("ERROR: nota debe ser un valor entre 1 y 7.")
    nota = float(input("Ingrese nota: "))

print("Nota cargada exitosamente!!!!")

os.system("pause")

os.system("cls")

# 2. Carga de nota con while True:

nota = float(input("Ingrese nota: "))
while True:
    if 1 <= nota <= 7:
        break
    else:
        print("ERROR: nota debe ser un valor entre 1 y 7.")
        nota = float(input("Ingrese nota: "))

print("Nota cargada exitosamente!!!!")
