import moduloIMC as mi
import os

op = ""
while True:
    os.system("cls")

    print("""
        CALCULADORA IMC 
        ======================
        1. Registrar usuario
        2. Mostrar lista de usuarios
        3. Buscar usuario por nombre
        4. Eliminar usuario por nombre
        5. Modificar usuario por nombre
        6. Salir
        """)

    op = str(input("\nSeleccione una opción: "))

    match op:
        case "0":
            os.system("cls")
            mi.loadDataTest()
            # os.system("pause")
        case "1":
            os.system("cls")
            print("REGISTRO DE USUARIO\n")
            mi.registrarUsuario()
            # os.system("pause")
        case "2":
            os.system("cls")
            print("LISTA DE USUARIOS\n")
            mi.listarUsuarios()
            # os.system("pause")
        case "3":
            os.system("cls")
            print("BUSCAR USUARIO\n")
            mi.buscarUsuario()
            # os.system("pause")
        case "4":
            os.system("cls")
            print("ELIMINAR USUARIO\n")
            mi.eliminarUsuario()
            # os.system("pause")
        case "5":
            os.system("cls")
            print("MODIFICAR USUARIO\n")
            mi.modificarUsuario()
            # os.system("pause")
        case "6":
            os.system("cls")
            print("SALIENDO DE LA APLICACION...\n")
            break
        case _:
            print("ERROR, debe ingresar una opción válida.")
