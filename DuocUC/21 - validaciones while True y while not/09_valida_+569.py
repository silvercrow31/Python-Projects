import os

celu = str(input("Ingrese número de celular: ")).strip()

while not (celu.startswith("+569")):
    print("ERROR: el número de celular debe comenzar con +569")
    celu = str(input("Ingrese número de celular: ")).strip()

print("Número ingresado correctamente!!!!!")


os.system("pause")

os.system("cls")

while True:
    celu = str(input("Ingrese número de celular: ")).strip()
    if celu.startswith("+569"):
        break
    else:
        print("ERROR: el número de celular debe comenzar con +569")

print("Número ingresado correctamente!!!!!")
