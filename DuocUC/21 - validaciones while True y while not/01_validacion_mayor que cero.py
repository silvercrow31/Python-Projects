import os

print("\n ---------- while not ----------")

edad = int(input("Ingrese edad: "))
while not (edad > 0):
    print("ERROR: edad debe ser mayor a cero. ")
    edad = int(input("Ingrese edad: "))

print("Edad cargada exitosamente!!!!!")

os.system("pause")

os.system("cls")


print("\n ---------- while True ----------")

while True:
    edad = int(input("Ingrese edad: "))
    if edad > 0:
        break
    elif edad <= 0:
        print("ERROR: edad debe ser mayor a cero. ")
