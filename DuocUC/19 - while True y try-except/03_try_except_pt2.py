import os

while True:
    os.system("cls")
    try:
        nota = float(input("Ingrese nota: "))

        if 1 <= nota <= 7:
            break
        else:
            print("Debe estar entre 1 y 7")

    except ValueError:
        print("ERROR: debe ser un número!!!")
    os.system("pause")

print(f"La nota correcta es {nota}")
