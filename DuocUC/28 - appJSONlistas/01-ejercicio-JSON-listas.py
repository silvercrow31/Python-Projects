import os

op = ""
rut = ""
nombre = ""
edad = 0
usuariosList = []

os.system("cls")
while True:
    os.system("cls")

    print("""
            MENU PRINCIPAL
            1. Agregar usuario
            2. Listar usuarios
            3. Eliminar por RUT
            4. Buscar por RUT
            5. Listar por rango de edad
            6. Salir
        """)

    op = str(input("\nSeleccione una opción: "))

    match op:
        case "1":
            os.system("cls")
            print("Agregar usuario: ")
            nombre = str(input("Ingrese nombre del usuario: "))
            rut = str(input("Ingrese el RUT del usuario: "))
            edad = int(input("Ingrese edad del usuario: "))
            usuario = {"rut": rut, "nombre": nombre, "edad": edad}
            usuariosList.append(usuario)
            print("Registro almacenado correctamente!!!")
            os.system("pause")
        case "2":
            os.system("cls")
            print("Listar usuarios: ")
            if len(usuariosList) == 0:
                print("No hay usuarios registrados!")
            elif len(usuariosList) > 0:
                for u in usuariosList:
                    print(f"""
                        -----------------------------
                        Rut:        {u["rut"]}
                        Nombre:     {u["nombre"]}
                        Edad:       {u["edad"]} años
                        -----------------------------
                          """)
            os.system("pause")
        case "3":
            os.system("cls")
            rut = str(input("Ingrese el RUT del usuario a eliminar: ")).strip().upper()
            encontrado = False
            for u in usuariosList:
                if u["rut"] == rut:
                    encontrado = True
                    usuariosList.remove(u)
                    print("Registro Eliminado!!!")
                    os.system("pause")
            if encontrado == False:
                print("El RUT ingresado no se encuentra en el sistema. ")
                os.system("pause")

        case "4":
            os.system("cls")
            print("Buscar por RUT: ")
            rut = str(input("Ingrese el RUT del usuario a buscar: ")).strip().upper()
            encontrado = False
            for u in usuariosList:
                if u["rut"] == rut:
                    encontrado == True
                    print(f"""
                        -----------------------------
                        Rut:        {u["rut"]}
                        Nombre:     {u["nombre"]}
                        Edad:       {u["edad"]} años
                        -----------------------------
                        """)
                    os.system("pause")
            if encontrado == False:
                print("El RUT ingresado no se encuentra en el sistema. ")
                os.system("pause")
            pass
        case "5":
            os.system("cls")
            pass
        case "6":
            os.system("cls")
            print("Saliendo de la aplicación...")
            os.system("pause")
            break
        case _:
            os.system("cls")
            print("ERROR: opción no válida. Intente de nuevo. ")
            os.system("pause")
