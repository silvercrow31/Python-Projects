import os
import funcionesEmpleados as fe

empleadosList = []

while True:
    print("""
MENU
            1. Cargar datos y ver liquidación
            2. Ver estadísticas
            3. Salir
          """)
    opcion = str(input("\nElija opción: ")).strip()

    match (opcion):
        case "1":
            os.system("cls")
            print("Cargar datos y ver liquidación")
            rut = str(input("Ingrese RUT: ")).strip().upper()
            nombre = str(input("Ingrese nombre: ")).strip().upper()
            bruto = int(input("Ingrese sueldo bruto: $"))
            liquido = fe.calcularLiquido(bruto)
            salud = fe.calcularSalud(bruto)
            pension = fe.calcularPension(bruto)
            fe.imprimirLiquidacion(rut, nombre, bruto, salud, pension, liquido)

            empleado = {
                "rut": rut,
                "nombre": nombre,
                "bruto": bruto,
                "salud": salud,
                "pension": pension,
                "liquido": liquido,
            }
            empleadosList.append(empleado)
            print("...empleado grabado!!!")
            os.system("pause")
        case "2":
            os.system("cls")
            print("Los empleados registrados:")
            for emp in empleadosList:
                fe.imprimirEmpleado(emp)
            pass
        case "3":
            break
        case _:
            print("ERROR, opción no válida. ")
