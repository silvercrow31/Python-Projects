import moduloEstudiante as me
import os

op = ""
while True:
    os.system("cls")

    print("""
        SISTEMA DE ESTUDIANTES
        ======================
        1. Registrar estudiante
        2. Listar estudiantes
        3. Modificar estudiante
        4. Eliminar estudiante
        5. Buscar estudiante
        6. Salir
        """)

    op = str(input("\nSeleccione una opción: "))

    match op:
        case "1":
            os.system("cls")
            print("REGISTRAR ESTUDIANTE")
            me.registrarEstudiante()
        case "2":
            os.system("cls")
            print("LISTAR ESTUDIANTES")
            me.listarEstudiantes()
        case "3":
            os.system("cls")
            print("MODIFICAR ESTUDIANTES")
            run = (
                str(input("Ingrese el rut del estudiante a modificar: "))
                .strip()
                .upper()
            )
            me.modificarEstudiante(run)
        case "4":
            os.system("cls")
            print("ELIMINAR ESTUDIANTES")
            run = str(input("Ingrese run a eliminar: ")).strip().upper()
            me.eliminarEstudiante(run)
        case "5":
            os.system("cls")
            print("BUSCAR ESTUDIANTES")
            run = str(input("Ingrese run a buscar: ")).strip().upper()
            me.printEstudiante(me.buscarEstudiante(run))
            os.system("pause")
        case "6":
            os.system("cls")
            print("SALIENDO DE LA APLICACION...")
            break
        case _:
            print("ERROR, debe ingresar una opción válida.")
