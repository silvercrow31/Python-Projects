productosList = []
import os


# ====================== FUNCIONES DE MENU Y ACCESORIAS ======================
def mostrarMenu():
    print("""
          SISTEMA DE INVENTARIO\n
          1. REGISTRAR PRODUCTO
          2. BUSCAR PRODUCTO
          3. ELIMINAR PRODUCTO
          4. ACTUALIZAR DISPONIBILIDAD
          5. VER INVENTARIO
          6. SALIR\n
          """)


def leerOpcion():
    while True:
        try:
            op = (
                str(input("Seleccione una opción: ")).strip().upper()
            )  # recibe input como string
            op = int(op)  # transforma string a int
            break
        except ValueError:
            print("ERROR: debe ingresar un número. ")
    if 1 <= op <= 6:
        return op
    else:
        print("ERROR: debe ingresar una opción entre 1 y 6")


def pedirInput(x):
    # en base al valor de x se decide que input se va a pedir
    match x:
        case "nombre":
            nombre = str(input(f"Ingrese nombre: ")).strip().upper()
            while not validacionNombre(nombre):
                nombre = str(input("Ingrese nombre: ")).strip().upper()
            return nombre
        case "precio":
            while True:
                try:
                    precio = float(input("Ingrese precio: "))
                    while not validacionPrecio(precio):
                        precio = float(input("Ingrese precio: "))
                    return precio
                except ValueError:
                    print("ERROR: el precio debe ser un número. ")
        case "cantidad":
            while True:
                try:
                    cantidad = float(input("Ingrese cantidad: "))
                    while not validacionCantidad(cantidad):
                        cantidad = float(input("Ingrese cantidad: "))
                    return cantidad
                except ValueError:
                    print("ERROR: la cantidad debe ser un número. ")


# ====================== VALIDACIONES ======================


def validacionNombre(nombre):
    if len(nombre) > 0:
        return True
    elif len(nombre) == 0:
        return False


def validacionPrecio(precio):
    precio = float(precio)
    if type(precio) == float and precio > 0:
        return True
    else:
        return False


def validacionCantidad(cantidad):
    cantidad = int(cantidad)
    if type(cantidad) == int and cantidad >= 0:
        return True
    else:
        return False


# ====================== FUNCIONES PRINCIPALES ======================


def registrarProducto(lista):
    nombre = pedirInput("nombre")
    precio = pedirInput("precio")
    cantidad = pedirInput("cantidad")
    if not validacionNombre(nombre):
        print("ERROR: nombre ingresado no es válido. Abortando registro... ")
        os.system("pause")
    if not validacionPrecio(precio):
        print("ERROR: precio ingresado no es válido. Abortando registro... ")
        os.system("pause")
    if not validacionCantidad(cantidad):
        print("ERROR: cantidad ingresada no es válida. Abortando registro... ")
        os.system("pause")

    if (
        validacionNombre(nombre)
        and validacionPrecio(precio)
        and validacionCantidad(cantidad)
    ):
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "conStock": False,
        }
        lista.append(producto)
        mostrarProducto(buscarProducto(productosList, nombre), productosList)
        print("¡Producto registrado existoamente!")


def mostrarProducto(index, lista):
    producto = lista[index]
    estado = "DISPONIBLE" if producto["cantidad"] > 0 else "AGOTADO"
    print(f"""
            Producto : {producto["nombre"]}
            Precio   : {producto["precio"]}
            Cantidad : {producto["cantidad"]}
            Estado   : {estado}
            ─────────────────────────────
          """)


def buscarProducto(lista, nombre):
    for i, producto in enumerate(lista):
        if nombre == producto["nombre"]:
            return i
    return -1


def actualizarDisponibilidad():
    for producto in productosList:
        if producto["cantidad"] > 0:
            producto["conStock"] = True
        elif producto["cantidad"] == 0:
            producto["conStock"] = False


def verInventario():
    actualizarDisponibilidad()
    for i, producto in enumerate(productosList):
        mostrarProducto(i, productosList)


def eliminarProducto():
    nombre = pedirInput("nombre")
    posicion = buscarProducto(productosList, nombre)
    if not posicion == -1:
        productosList.pop(posicion)
        print(f"El producto {nombre} fue eliminado del inventario. ")
    else:
        print(f"El producto {nombre} no existe en el inventario. ")
