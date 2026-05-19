import os

op = ""
nota1, nota2, nota3 = 0, 0, 0

promedio = 0
estado = ""

atendidos, aprobados, reprobados = 0, 0, 0

os.system("cls")

while True:
    print("""
          ----- MENU -----
          1.- Calcular promedio
          2.- Ver Resultados estadísticos
          3.- Salir
          \n
          """)

    op = str(input("Selecione una opción: "))

    match op:
        # 1. CALCULAR PROMEDIO
        case "1":
            os.system("cls")
            print("----- CALCULAR PROMEDIO -----")

            # NOTA 1
            while True:
                os.system("cls")
                try:

                    nota1 = float(input("Ingrese nota 1: "))

                    if 1 <= nota1 <= 7:
                        break
                except:
                    print("Debe estar entre el 1 y el 7")

                # NOTA 2
            while True:
                os.system("cls")
                try:

                    nota2 = float(input("Ingrese nota 2: "))

                    if 1 <= nota1 <= 7:
                        break
                except:
                    print("Debe estar entre el 1 y el 7")

            # NOTA 3
            while True:
                os.system("cls")
                try:

                    nota3 = float(input("Ingrese nota 3: "))

                    if 1 <= nota1 <= 7:
                        break
                except:
                    print("Debe estar entre el 1 y el 7")

            # CALCULO PROMEDIO Y ESTADO
            promedio = (nota1 + nota2 + nota3) / 3
            estado = "APROBADO" if promedio >= 4 else "REPROBADO"

            # ESTADISTICAS
            atendidos += 1
            match estado:
                case "APROBADO":
                    aprobados += 1
                case "REPROBADO":
                    reprobados += 1

            # TICKET
            print(f"""
                    ----- TICKET -----
                        nota 1: {nota1}
                        nota 2: {nota2}
                        nota 3: {nota3}
                        estado: {estado}
                    

                  """)
            os.system("pause")

        case "2":
            os.system("cls")
            print(f"""
                  ----- ESTADISTICAS -----
                    atendidos:  {atendidos}
                    aprobados:  {aprobados}
                    reprobados: {reprobados}
                   """)
            os.system("pause")

        case "3":
            salir = str(input("Seguro que quiere salir? (S/N)  ")).strip().upper()
            if salir == "S":
                break

        case _:
            print("Error")
