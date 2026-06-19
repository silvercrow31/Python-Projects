import os

cancionesList = []

# -----------------------validaciones-----------------------


def validarTextoVacio(texto):
    if len(texto) == 0:
        return False
    return True


def validarDuracion(duracion):
    if duracion > 0:
        return True
    return False


def validacionFinal(titulo, artista, duracion):
    if (
        validarTextoVacio(titulo)
        and validarTextoVacio(artista)
        and validarDuracion(duracion)
    ):
        return True
    else:
        if not validarTextoVacio(titulo):
            print("ERROR: el título ingresado no es válido (texto vacío).")
        if not validarTextoVacio(artista):
            print("ERROR: el artista ingresado no es válido (texto vacío).")
        if not validarDuracion:
            print("ERROR: la duración ingresada no es válida (menor a cero).")
        return False


def imprimirCancion(x):
    # por defecto se asume que x es el JSON de la cancion
    # si type(x) es int, significa que x es en realidad el index
    # y por ello se actualiza el valor de cancion
    cancion = x
    if type(x) == int:
        cancion = cancionesList[x]
    esFavorita = "FAVORITA" if cancion["favorita"] == True else "NORMAL"
    print(f"""
        --------------------
        Título:       {cancion["titulo"]}
        Artista:      {cancion["artista"]}
        Duración:     {cancion["duracion"]}
        Estado:       {esFavorita}
""")


def agregarCancion():
    titulo = str(input("Ingrese título de la canción: ")).strip().upper()
    while not validarTextoVacio(titulo):
        titulo = str(input("Ingrese título de la canción: ")).strip().upper()

    artista = str(input("Ingrese nombre del artista: ")).strip().upper()
    while not validarTextoVacio(artista):
        artista = str(input("Ingrese nombre del artista: ")).strip().upper()

    while True:
        try:
            duracion = int(input("Ingrese duración de la canción (segundos): "))
            if not validarDuracion(duracion):
                print("ERROR, la duración debe ser mayor a cero. ")
            break
        except ValueError:
            print("ERROR, debe ingresar un número. ")
    if validacionFinal(titulo, artista, duracion):
        # si todos los datos son validados se crea el JSON y se agrega a lista
        cancion = {
            "titulo": titulo,
            "artista": artista,
            "duracion": duracion,
            "favorita": False,
        }
        cancionesList.append(cancion)
        print("Cancion registrada exitosamente! ")
    else:
        print("Abortando el registro de la canción... ")


def buscarCancion(tituloABuscar):
    for c in cancionesList:
        if c["titulo"] == tituloABuscar:
            return cancionesList.index(c)
    return -1


def eliminarCancion(tituloAELiminar):
    if buscarCancion(tituloAELiminar) == -1:
        print(f"La canción {tituloAELiminar} no se encuentra registrada. ")
    else:
        cancionesList.pop(buscarCancion(tituloAELiminar))
        print(f"La canción {tituloAELiminar} fue eliminada exitosamente. ")


def mostrarLista():
    if len(cancionesList) == 0:
        print("ERROR: no hay canciones en la lista. ")
    elif len(cancionesList) > 0:
        for c in cancionesList:
            imprimirCancion(c)


def pedirTitulo():
    titulo = str(input("Ingrese título: ")).strip().upper()
    while not validarTextoVacio(titulo):
        titulo = str(input("Ingrese título: ")).strip().upper()
    return titulo


def hacerFavorita(titulo):
    if buscarCancion(titulo) == -1:
        print(f"La canción {titulo} no se encuentra registrada")
    else:
        for c in cancionesList:
            if c["titulo"] == titulo and c["favorita"] == False:
                c["favorita"] = True
                print(f"La canción {titulo} ahora es su favorita!")
            elif c["titulo"] == titulo and c["favorita"] == True:
                print("ERROR: la canción ya es favorita")
