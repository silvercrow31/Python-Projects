import os

# En el múdlo debe ir:

# La lista que sera la Base de Datos
# Funciones de validación
# Funciones de transacción (agregar, listar, etc...)

# --------------------MODULO---------------------------------

autosList = []


# ----------------------------------------------funciones validadoras
def validarTextoVacio(texto):
    if len(texto) > 0:
        return True  # texto validado
    else:
        print("ERROR, no puede ser un texto vacío!! ")
        return False  # texto no validado!!!


def validarAnno(anno):
    if anno > 1970:
        return True
    else:
        print("ERROR, el año debe ser mayor a 1970")
        return False


def validarPrecio(precio):
    if precio > 0:
        return True
    else:
        print("ERROR, el precio debe ser un número positivo!! ")
        return False


def validarSN(usadoSN):
    if usadoSN in ["S", "N"]:
        return True  # se valida
    else:
        print("ERROR, solo se acepta S o N como respuesta!!")
        return False  # no se valida

def validarPatente(patente):
    if(len(patente.strip()) != 6):
        print("Error, la patente debe tener 6 carácteres. ")
        return False
    
    
    parte1=patente[:4] #primeros 4 caracteres
    parte2=patente[4:]#ultimos 4 caracteres
    
    if not parte1.isalpha(): #isalpha devuelve true si todos los caracteres son letras
        print("ERROR, no posee las letras!!!")
        return False
    if not parte2.isdigit(): #isdigit devuelve true si todos los caracteres son digitos numericos
        print("ERROR, no posee los números!!!")
        return False
        


# -----------------------------------------------funciones transaccionales


def agregarAuto():

    # 1. Capturamos datos
    patente = str(input("Ingrese patente: ")).strip().upper()
    while not (validarTextoVacio(patente) and validarPatente(patente)):
        patente = str(input("Ingrese patente: ")).strip().upper()

    marca = str(input("Ingrese marca: ")).strip().upper()
    while not validarTextoVacio(marca):
        marca = str(input("Ingrese marca: ")).strip().upper()

    modelo = str(input("Ingrese modelo: ")).strip().upper()
    while not validarTextoVacio(modelo):
        modelo = str(input("Ingrese modelo: ")).strip().upper()

    while True:
        try:
            anno = str(input("Ingrese año: ")).strip()
            while not (validarTextoVacio(anno) and validarAnno(anno)):  # verificar si es asi
                anno = str(input("Ingrese año: ")).strip()
            break
        except:
            print("ERROR, debe ser un N°!!")

    usadoSN = str(input("¿Es usado? S/N: ")).strip().upper()  # "usado" como string
    while not validarTextoVacio(usadoSN):
        usadoSN = str(input("¿Es usado? S/N: ")).strip().upper()  # "usado" como string

    usado = True if usadoSN == "S" else False  # "usado" en booleano

    while True:
        try:
            precio = str(input("Ingrese precio: ")).strip()
            while not validarTextoVacio(precio):
                precio = str(input("Ingrese precio: ")).strip()
            break
        except:
            print("ERROR, debe ser un N°!!! ")

    # 2. Armamos JSON con los datos capturados
    auto = {
        "patente": patente,
        "marca": marca,
        "modelo": modelo,
        "anno": anno,
        "usado": usado,
        "precio": precio,
    }

    # 3. El JSON completado se agrega a la lista
    autosList.append(auto)
    print("Registro almacenado exitosamente!!!")
    os.system("pause")

    # print(f"La base de datos posee: {len(autosList)} autos. \n")

    # print(autosList)


def listarAutos():
    if len(autosList) == 0:
        print("La base de datos no contiene ningún auto para listar. ")
    else:
        for auto in autosList:
            usadoSN="Si" if auto["usado"] == True else "No" #arreglar
            printAuto(auto, usadoSN)


def printAuto(auto, usadoSN):
    print(f"""
          ----------------
          Patente:  {auto["patente"]}
          Marca:    {auto["marca"]}
          Modelo:   {auto["modelo"]}
          Año:      {auto["anno"]}
          Es usado: {usadoSN}
          Precio:   ${auto["precio"]}
          
          """)

def buscarPorMarca():
    marca=str(input("Ingrese marca a buscar: ")).strip().upper()
    while not validarTextoVacio(marca):
        marca=str(input("Ingrese marca a buscar: ")).strip().upper()
    for auto in autosList:
        if marca==auto["marca"]:
            usadoSN="Si" if auto["usado"] == True else "No" #arreglar
            printAuto(auto, usadoSN)    

def cargarDataTesting():
    # crea 3 JSON auto
    auto1 = {
        "patente": "AABB11",
        "marca": "Kia",
        "modelo": "Rio",
        "anno": 2015,
        "usado": False,
        "precio": 4_000_000,
    }
    
    auto2 = {
        "patente": "ZZZZ99",
        "marca": "Toyota",
        "modelo": "Yaris",
        "anno": 2013,
        "usado": True,
        "precio": 8_000_000,
    }
    
    auto3 = {
        "patente": "EEFF33",
        "marca": "Kia",
        "modelo": "Morning",
        "anno": 2026,
        "usado": False,
        "precio": 7_500_000,
    }
    #cargamos JSON a la lista
    
    autosList.append(auto1)
    autosList.append(auto2)
    autosList.append(auto3)
    print("\n<<< data test cargado exitosamente >>>")