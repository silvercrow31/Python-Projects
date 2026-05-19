import os

nombre = str(input("Ingrese nombre: ")).strip()

while not (len(nombre) > 0):
    print("ERROR: debe ingresar un nombre")
    nombre = str(input("Ingrese nombre: ")).strip()

print("Nombre ingresado correctamente!!!!!")


os.system("pause")

os.system("cls")


while True:
    nombre = str(input("Ingrese nombre: ")).strip()
    if len(nombre) > 0:
        break
    else:
        print("ERROR: debe ingresar un nombre")

print("Nombre ingresado correctamente!!!!!")
