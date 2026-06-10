import os

n1, n2, n3, n4, examen = 0, 0, 0, 0, 0

op = ""

while True:
    os.system("cls")
    print("""
          BIENVENIDO A CALCULAPERA

Este programa le ayudará a calcular la nota que necesita para aprobar Fundamentos de Programación.
          
          TABLA DE PONDERACIONES

        |\tNOTA 1\t\tNOTA 2\t\tNOTA 3\t\tNOTA 4\t|\t\tEXAMEN\t\t|
        |\t20%\t\t25%\t\t30%\t\t25%\t|
        |---------------------------------------------------------------|-------------------------------|
        |\t\t\t60%\t\t\t\t\t|\t\t40%\t\t|

          1. Conozco todas mis notas menos el examen
          2. No conozco mi nota 4
          3. Salir
          """)

    op = str(input("\nIngrese una opción: "))

    match op:
        case "1":
            n1 = float(input("\nIngrese nota 1: "))
            n2 = float(input("\nIngrese nota 2: "))
            n3 = float(input("\nIngrese nota 3: "))
            n4 = float(input("\nIngrese nota 4: "))
            ponderado = 0.6 * (0.2 * n1 + 0.25 * n2 + 0.3 * n3 + 0.25 * n4)
            examenMinimo = (4 - ponderado) / 0.4

            print(f"""
                    ----------RESULTADOS----------
                    Necesita como mínimo un {examenMinimo} en el exámen para aprobar.
                    """)
            os.system("pause")

        case "2":
            os.system("cls")
            n1 = float(input("\nIngrese nota 1: "))
            n2 = float(input("\nIngrese nota 2: "))
            n3 = float(input("\nIngrese nota 3: "))
            n4inventada = float(input("\nIngrese una posible nota 4: "))
            ponderado = 0.6 * (0.2 * n1 + 0.25 * n2 + 0.3 * n3 + 0.25 * n4inventada)
            examenMinimo = (4 - ponderado) / 0.4

            print(f"""
                  ----------RESULTADOS----------
                  Con una n4={n4inventada} necesita como mínimo un {examenMinimo} en el examen para aprobar.
                  """)
            os.system("pause")
        case "3":
            break
        case _:
            print("\nERROR, opción ingresada no es válida. ")
            os.system("pause")
