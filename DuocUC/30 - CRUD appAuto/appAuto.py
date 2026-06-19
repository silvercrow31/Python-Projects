import moduloAuto as ma
import os

op = ""
while True:
    os.system("cls")

    print("""
        SISTEMA DE ESTUDIANTES
        ======================
        0. Cargar data para testing
        1. Registrar auto
        2. Listar autos
        3. Buscar por marca
        4. Buscar por rango de precio
        5. Eliminar registro de auto
        6. Salir
        """)

    op = str(input("\nSeleccione una opción: "))

    match op:
        case "0":
            os.system("cls")
            print("CARGAR DATA PARA TESTING")
            ma.cargarDataTesting()            
            os.system("pause")
        case "1":
            os.system("cls")
            print("REGISTRAR AUTO")
            ma.agregarAuto()
        case "2":
            os.system("cls")
            print("LISTAR AUTOS")
            ma.listarAutos()
            os.system("pause")
        case "3":
            os.system("cls")
            print("BUSCAR POR MARCA")
            os.system("pause")
        case "4":
            os.system("cls")
            print("BUSCAR POR RANGO DE PRECIO")
            os.system("pause")
        case "5":
            os.system("cls")
            print("ELIMINAR REGISTRO DE AUTO")
            os.system("pause")
        case "6":
            os.system("cls")
            print("SALIENDO DE LA APLICACION...")
            break
        case _:
            print("ERROR, debe ingresar una opción válida.")