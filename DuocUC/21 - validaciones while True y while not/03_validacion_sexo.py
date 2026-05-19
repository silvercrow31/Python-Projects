import os

# 1. Carga de sexo con while not()
sexo = str(input("Ingrese sexo: ")).strip().upper()
while not (sexo in ["M", "F"]):
    print("ERROR: sexo debe ser M o F.")
    sexo = str(input("Ingrese sexo: ")).strip().upper()

print("Sexo cargado exitosamente!!!!")

os.system("pause")

os.system("cls")


# 2. Carga de sexo con while True:

sexo = str(input("Ingrese sexo: ")).strip().upper()
while True:
    if sexo in ["M", "F"]:
        break
    else:
        print("ERROR: sexo debe ser M o F.")
        sexo = str(input("Ingrese sexo: ")).strip().upper()

print("Sexo cargado exitosamente!!!!")
