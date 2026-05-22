import os

disponibles = 100
op = ""
aComprar = 0
aCancelar = 0
compradas = 0

while True:

    os.system("cls")

    print("""
    *** MENU PRINCIPAL ***
    1.- Ver entradas disponibles.
    2.- Comprar entradas.
    3.- Cancelar compra.
    4.- Ver historial de compras.
    5.- Salir\n
        """)

    op = str(input("Seleccione una opción: "))

    match op:
        case "1":
            os.system("cls")
            print(f"Entradas disponibles: {disponibles}")
            os.system("pause")
        case "2":
            os.system("cls")
            print("------COMPRAR ENTRADAS------")

            while True:
                aComprar = int(
                    input("Ingrese la cantidad de entradas que desea comprar: ")
                )
                # nocompra
                if aComprar <= 0:
                    os.system("cls")
                    print(
                        "ERROR: cantidad no válida. Ingrese un número entero positivo. "
                    )
                    os.system("pause")

                elif aComprar > disponibles:
                    os.system("cls")
                    print(f"""ERROR: cantidad ingresada supera nuestro stock disponible
                        Entradas disponibles: {disponibles}
                        """)
                    os.system("pause")

                # compra validada
                elif aComprar > 0 and aComprar <= disponibles:
                    print(f"Su compra de {aComprar} entradas ha sido validada!!!")
                    os.system("pause")
                    disponibles -= aComprar
                    compradas += aComprar
                    break

        case "3":
            os.system("cls")
            print("------CANCELAR COMPRA------")

            while True:
                aCancelar = int(
                    input("Ingrese la cantidad de entradas que desea cancelar: ")
                )
                # noCancela
                if aCancelar <= 0:
                    os.system("cls")
                    print(
                        "ERROR: cantidad no válida. Ingrese un número entero positivo. "
                    )
                    os.system("pause")
                elif aCancelar > compradas:
                    os.system("cls")
                    print(
                        "ERROR: cantidad ingresada supera el máximo de entradas compradas"
                    )
                    os.system("pause")

                # cancelación validada
                elif aCancelar > 0 and aCancelar <= compradas:
                    print(f"Sus {aCancelar} entradas fueron canceladas exitosamente!!!")
                    os.system("pause")

                    disponibles += aCancelar
                    compradas -= aCancelar
                    break
        case "4":
            os.system("cls")
            print(f"""------HISTORIAL DE COMPRAS------
Entradas compradas esta sesión: {compradas}
                """)
            os.system("pause")

        case "5":
            os.system("cls")
            print("Gracias por utilizar el sistema.")
            os.system("pause")
            break
