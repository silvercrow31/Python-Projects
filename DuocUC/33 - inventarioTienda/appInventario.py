import moduloInventario as mi
import os

while True:
    os.system("cls")
    mi.mostrarMenu()
    op = mi.leerOpcion()
    match op:
        case 0:
            print("")
            pass
        case 1:
            os.system("cls")
            print(">>> REGISTRAR PRODUCTO <<<\n")
            mi.registrarProducto(mi.productosList)
            os.system("pause")
        case 2:
            os.system("cls")
            print(">>> BUSCAR PRODUCTO <<<\n")
            nombre = mi.pedirInput("nombre")
            posicion = mi.buscarProducto(mi.productosList, nombre)
            if not posicion == -1:
                mi.mostrarProducto(posicion, mi.productosList)
            elif posicion == -1:
                print(f"ERROR: el producto {nombre} no existe en el inventario. ")
            os.system("pause")
        case 3:
            os.system("cls")
            print(">>> ELIMINAR PRODUCTO <<<\n")
            mi.eliminarProducto()
            os.system("pause")
        case 4:
            os.system("cls")
            mi.actualizarDisponibilidad()
            print(">>> ACTUALIZACION FINALIZADA <<<")
            os.system("pause")
        case 5:
            os.system("cls")
            print(">>> INVENTARIO ACTUAL <<<\n")
            mi.verInventario()
            os.system("pause")
        case 6:
            print("SALIENDO DE LA APLICACION...")
            break
        case _:
            print("ERROR: OPCION NO VALIDA")
