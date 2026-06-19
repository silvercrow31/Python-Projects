import os

estudiantesList = []


def validarRun(run):
    if len(run.strip()) > 0:
        return True
    # aplicamos la logica de  los retornos. cuando ocurre un Return termina la ejecución.
    print("ERROR, no puede ser vacío")
    os.system("pause")
    return False


def validarJornada(jornada):
    if jornada in ["D", "V"]:
        return True
    print("Jornada ingresada no es válida. Debe ser D o V")
    return False


def validarTexto(texto):
    if texto.isalpha():
        return True
    else:
        print("ERROR, el texto no debe contener números!")
        return False


def buscarEstudiante(run):
    for estudiante in estudiantesList:
        if estudiante["run"] == run.strip():
            return estudiante  # SE ENCONTRO
    print("No existe el estudiante en el registro. ")
    os.system("pause")


def registrarEstudiante():
    run = str(input("Ingrese RUN: ")).strip().upper()
    while not validarRun(run):
        run = str(input("Ingrese RUN: ")).strip().upper()

    nombre = str(input("Ingrese nombre: ")).strip().upper()
    while not validarTexto(nombre):
        nombre = str(input("Ingrese nombre: ")).strip().upper()

    carrera = str(input("Ingrese carrera: ")).strip().upper()
    while not validarTexto(carrera):
        carrera = str(input("Ingrese carrera: ")).strip().upper()

    jornada = str(input("Ingrese jornada: ")).strip().upper()
    while not validarJornada(jornada):
        jornada = str(input("Ingrese jornada: ")).strip().upper()

    estudiante = {"run": run, "nombre": nombre, "carrera": carrera, "jornada": jornada}
    estudiantesList.append(estudiante)


def listarEstudiantes():
    if len(estudiantesList) == 0:
        print("No hay estudiantes para listar. ")
        os.system("pause")
    else:
        for estudiante in estudiantesList:
            printEstudiante(estudiante)
        os.system("pause")


def printEstudiante(estudiante):
    print(f"""
        ------------------------------
        NOMBRE:       {estudiante["nombre"]}
        RUN:          {estudiante["run"]}
        CARRERA:      {estudiante["carrera"]}
        JORNADA       {estudiante["jornada"]}
        ------------------------------
        """)


def eliminarEstudiante(run):
    if buscarEstudiante(run) != None:
        estudiantesList.remove(buscarEstudiante(run))
        print("registro eliminado!!")
        os.system("pause")
    else:
        print("No existe el run en el registro!!!")
        os.system("pause")


def modificarEstudiante(run):
    while not validarRun(run):
        run = str(input("RUN inválido. Intente nuevamente: "))

    while True:
        os.system("cls")
        op2 = ""
        estudianteAModificar = buscarEstudiante(run)
        printEstudiante(estudianteAModificar)
        print("""
            ¿Qué valor desea modificar?
              
            1. Nombre
            2. RUN
            3. Carrera
            4. Jornada
            5. Salir sin modificar
            """)
        op2 = str(input("\nSeleccione una opción: "))
        match op2:
            case "1":
                estudianteAModificar["nombre"] = (
                    str(input("Ingrese nuevo nombre: ")).strip().upper()
                )
                while not validarTexto(estudianteAModificar["nombre"]):
                    estudianteAModificar["nombre"] = (
                        str(input("Ingreso no válido. Ingrese nuevo nombre: "))
                        .strip()
                        .upper()
                    )
            case "2":
                estudianteAModificar["run"] = (
                    str(input("Ingrese RUN nuevo: ")).strip().upper()
                )
                while not validarRun(estudianteAModificar["run"]):
                    estudianteAModificar["run"] = (
                        str(input("Ingreso inválido. Ingrese RUN nuevo: "))
                        .strip()
                        .upper()
                    )
                run = estudianteAModificar["run"]

            case "3":
                estudianteAModificar["carrera"] = (
                    str(input("Ingrese carrera nueva: ")).strip().upper()
                )
                while not validarTexto(estudianteAModificar["carrera"]):
                    estudianteAModificar["carrera"] = (
                        str(input("Ingreso inválido. Ingrese carrera nueva: "))
                        .strip()
                        .upper()
                    )
            case "4":
                estudianteAModificar["jornada"] = (
                    str(input("Ingrese jornada nueva: ")).strip().upper()
                )
                while not validarJornada(estudianteAModificar["jornada"]):
                    estudianteAModificar["jornada"] = (
                        str(input("Ingreso inválido. Ingrese jornada nueva: "))
                        .strip()
                        .upper()
                    )
            case "5":
                break
            case _:
                print("ERROR, opción no válida. ")
                os.system("pause")
