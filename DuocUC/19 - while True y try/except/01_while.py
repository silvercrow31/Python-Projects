import os

op = ""


while True:
    os.system("cls")
    print("""
          ---------------- MENU ----------------
          1. Opción A
          2. Opción B
          3. Salir
          \n
          """)

    op = str(input("Elija opción: "))

    match op:
        case "1":
            os.system("cls")
            print("Presionó opción A")
            os.system("pause")
        case "2":
            os.system("cls")
            print("Presionó opción B")
            os.system("pause")
        case "3":
            print("saliendo....bye")
            break
        case _:
            print("NO VALIDO!!!!!!")
            os.system("pause")
