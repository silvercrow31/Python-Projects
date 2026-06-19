import os

usuariosList = []

# ==================== funciones de validacion ====================


def validarTextoVacio(texto):  # texto válido returna True, texto vacío retorna False
    if len(texto) == 0:
        print("ERROR, no se acepta texto vacío. ")
        return False
    return True


def nombreExisteEnLista(
    nombre,
):  # nombre existente retorna True, inexistente retorna False
    for u in usuariosList:
        if nombre == u["nombre"]:
            return True
    return False


def validarNumeroPositivo(
    numero,
):  # positivo y cero retorna True, negativo retorna False
    if numero < 0:
        print("ERROR, numero debe ser mayor o igual a cero. ")
        return False
    return True


def ListaEstaVacia():  # lista vacía retorna True
    if len(usuariosList) == 0:
        return True
    else:
        return False


# ==================== funciones de cálculo ====================


def calcularIMC(peso, estatura):  # retorna IMC
    return float(peso / (estatura**2))


def determinarClasificacionIMC(imc):  # retorna la clasificación
    if imc < 18.5:
        return "BAJO PESO"
    elif 18.5 <= imc < 25:
        return "NORMAL"
    elif 25 <= imc < 30:
        return "SOBREPESO"
    elif imc >= 30:
        return "OBESIDAD"


# ==================== funciones de transaccion ====================


def registrarUsuario():  # Captura datos, arma JSON y lo agrega a la lista

    # Captura nombre
    nombre = str(input("Ingrese nombre: ")).strip().upper()
    while not validarTextoVacio(nombre):
        nombre = str(input("Ingrese nombre: ")).strip().upper()

    # Captura edad
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            while not validarNumeroPositivo(edad):
                edad = int(input("Ingrese edad: "))
            break
        except:
            print("ERROR, debe ingresar un número.")
            os.system("pause")

    # Captura peso
    while True:
        try:
            peso = int(input("Ingrese peso: "))
            while not validarNumeroPositivo(peso):
                peso = int(input("Ingrese peso: "))
            break
        except:
            print("ERROR, debe ingresar un número.")
            os.system("pause")

    # Captura estatura
    while True:
        try:
            estatura = float(input("Ingrese estatura: "))
            while not validarNumeroPositivo(estatura):
                estatura = float(input("Ingrese estatura: "))
            break
        except:
            print("ERROR, debe ingresar un número.")
            os.system("pause")

    # Calcula IMC y determina clasificación
    imc = calcularIMC(peso, estatura)
    clasificacion = determinarClasificacionIMC(imc)

    # Construimos JSON y lo agregamos a la lista
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "peso": peso,
        "estatura": estatura,
        "imc": imc,
        "clasificacion": clasificacion,
    }
    usuariosList.append(usuario)
    printUsuario(usuario)  # Se muestra en pantalla el usuario registrado
    print("\nUsuario registrado exitosamente. ")


def printUsuario(usuario):  # Imprime el usuario y su información
    print(f"""
    ----------------
    Nombre:           {usuario["nombre"]}
    Edad:             {usuario["edad"]}
    Peso:             {usuario["peso"]}
    Estatura:         {usuario["estatura"]}
    IMC:              {usuario["imc"]:.0f}
    Clasificación:    {usuario["clasificacion"]}

          """)


def listarUsuarios():  # Muestra en pantalla los usuarios registrados
    # Primero verificar si tengo usuarios en la lista
    if ListaEstaVacia() == True:
        print("ERROR, no se encontraron usuarios en la lista. ")
    else:
        for usuario in usuariosList:
            printUsuario(usuario)
    os.system("pause")


def buscarUsuario():  # Busca usuario en la lista y si existe hace print
    if not ListaEstaVacia():
        nombreABuscar = str(input("Ingrese nombre a buscar: ")).strip().upper()
        while not validarTextoVacio(nombreABuscar):
            nombreABuscar = str(input("Ingrese nombre a buscar: ")).strip().upper()
        printUsuario(consigueUsuario(nombreABuscar))
    else:
        print("ERROR, no hay usuarios en la lista. No se pudo realizar la búsqueda. ")
    os.system("pause")


def consigueUsuario(nombreAConseguir):  # Recibe un nombre, retorna el JSON del usuario
    for u in usuariosList:
        if u["nombre"] == nombreAConseguir:
            return u


def eliminarUsuario():  # Elimina usuario por nombre
    if not ListaEstaVacia():
        nombreAEliminar = str(input("Ingrese nombre a eliminar: ")).strip().upper()
        while not validarTextoVacio(nombreAEliminar):
            nombreAEliminar = str(input("Ingrese nombre a eliminar: ")).strip().upper()

        for u in usuariosList:
            if u["nombre"] == nombreAEliminar:
                usuariosList.remove(u)
                print(f"Usuario eliminado exitosamente. ")
    else:
        print("ERROR, no hay usuarios en la lista. No se pudo realizar la operación. ")
    os.system("pause")


def modificarUsuario():
    if not ListaEstaVacia():
        nombreAModificar = (
            str(input("Ingrese nombre del usuario que desea modificar: "))
            .strip()
            .upper()
        )
        os.system("cls")
        while not validarTextoVacio(nombreAModificar):
            nombreAModificar = (
                str(input("Ingrese nombre del usuario que desea modificar: "))
                .strip()
                .upper()
            )
        if nombreExisteEnLista(nombreAModificar):
            usuarioAModificar = consigueUsuario(nombreAModificar)
            while True:
                os.system("cls")
                print(f"""
    MODIFICAR USUARIO: {nombreAModificar}  

        1. Modificar nombre
        2. Modificar edad
        3. Modificar peso
        4. Modificar estatura
                    """)
                opModificar = str(input("\nSeleccione una opción: "))
                match opModificar:
                    # Modificar nombre
                    case "1":
                        nuevoNombre = (
                            str(input("\nIngrese nuevo nombre: ")).strip().upper()
                        )
                        while not validarTextoVacio(nuevoNombre):
                            nuevoNombre = (
                                str(input("\nIngrese nuevo nombre: ")).strip().upper()
                            )
                        for u in usuariosList:
                            if u == usuarioAModificar:
                                usuarioAModificar["nombre"] = nuevoNombre
                                os.system("cls")
                                printUsuario(u)
                                print("\nUsuario modificado exitosamente. ")
                                os.system("pause")
                        break
                    # Modificar edad
                    case "2":
                        while True:
                            try:
                                nuevaEdad = int(input("\nIngrese nueva edad: "))
                                while not validarNumeroPositivo(nuevaEdad):
                                    nuevaEdad = int(input("\nIngrese nueva edad: "))
                                for u in usuariosList:
                                    if u == usuarioAModificar:
                                        u["edad"] = nuevaEdad
                                        os.system("cls")
                                        printUsuario(u)
                                        print("\nUsuario modificado exitosamente. ")
                                        os.system("pause")
                                break
                            except:
                                print("ERROR, debe ingresar un número.")
                                os.system("pause")
                        break
                    # Modificar peso
                    case "3":
                        while True:
                            try:
                                nuevoPeso = int(input("\nIngrese nuevo peso: "))
                                while not validarNumeroPositivo(nuevoPeso):
                                    nuevoPeso = int(input("\nIngrese nuevo peso: "))
                                for u in usuariosList:
                                    if u == usuarioAModificar:
                                        u["peso"] = nuevoPeso
                                        # Actualizamos IMC y clasificación
                                        u["imc"] = calcularIMC(u["peso"], u["estatura"])
                                        u["clasificacion"] = determinarClasificacionIMC(
                                            u["imc"]
                                        )
                                        os.system("cls")
                                        printUsuario(u)
                                        print("\nUsuario modificado exitosamente. ")
                                        os.system("pause")
                                break
                            except:
                                print("\nERROR, debe ingresar un número.")
                                os.system("pause")
                        break
                    # Modificar estatura
                    case "4":
                        while True:
                            try:
                                nuevaEstatura = float(
                                    input("\nIngrese nueva estatura: ")
                                )
                                while not validarNumeroPositivo(nuevaEstatura):
                                    nuevaEstatura = float(
                                        input("\nIngrese nueva estatura: ")
                                    )
                                for u in usuariosList:
                                    if u == usuarioAModificar:
                                        u["estatura"] = nuevaEstatura
                                        # Actualizamos IMC y clasificación
                                        u["imc"] = calcularIMC(u["peso"], u["estatura"])
                                        u["clasificacion"] = determinarClasificacionIMC(
                                            u["imc"]
                                        )
                                        os.system("cls")
                                        printUsuario(u)
                                        print("\nUsuario modificado exitosamente. ")
                                        os.system("pause")
                                break
                            except:
                                print("\nERROR, debe ingresar un número.")
                                os.system("pause")
                        break
                    case _:
                        print("Opción inválida. ")
                        os.system("pause")
        elif not nombreExisteEnLista(nombreAModificar):
            os.system("cls")
            print(
                "ERROR, el usuario que desea modificar no se encuentra en la lista. No se pudo realizar la operación. "
            )
            os.system("pause")
    elif ListaEstaVacia():
        os.system("cls")
        print("ERROR, no hay usuarios en la lista. No se pudo realizar la operación. ")
        os.system("pause")


def loadDataTest():  # carga data para testing
    usuariosList.append(
        {
            "nombre": "JOSE PABLO",
            "edad": 26,
            "peso": 72,
            "estatura": 1.7,
            "imc": 0,
            "clasificacion": "",
        }
    )
    usuariosList.append(
        {
            "nombre": "CLAUDIO",
            "edad": 26,
            "peso": 80,
            "estatura": 1.75,
            "imc": 0,
            "clasificacion": "",
        }
    )
    for u in usuariosList:
        u["imc"] = calcularIMC(u["peso"], u["estatura"])
        u["clasificacion"] = determinarClasificacionIMC(u["imc"])
    print("DATA TEST LOADED SUCCESSFULLY")
    os.system("pause")
