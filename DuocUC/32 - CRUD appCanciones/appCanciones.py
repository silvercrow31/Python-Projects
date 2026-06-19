import moduloCanciones as mc
import os

while True:
    os.system("cls")
    op = ""
    print("""
                   SISTEMA DE GESTION DE CANCIONES
          
                ========== MENÚ PRINCIPAL ==========
                        1. Agregar canción
                        2. Buscar canción
                        3. Eliminar canción
                        4. Marcar como favorita
                        5. Mostrar canciones
                        6. Salir
                ====================================
        """)
    op = str(input("Seleccione una opción: "))

    match op:
        case "1":
            os.system("cls")
            print("AGREGAR CANCION\n")
            mc.agregarCancion()
            os.system("pause")
        case "2":
            os.system("cls")
            print("BUSCAR CANCION\n")
            tituloABuscar = mc.pedirTitulo()
            busqueda = mc.buscarCancion(tituloABuscar)
            if busqueda == -1:
                print("Canción no encontrada. ")
            else:
                mc.imprimirCancion(busqueda)
            os.system("pause")
        case "3":
            os.system("cls")
            print("ELIMINAR CANCION\n")
            tituloAEliminar = mc.pedirTitulo()
            mc.eliminarCancion(tituloAEliminar)
            os.system("pause")
        case "4":
            os.system("cls")
            print("MARCAR COMO FAVORITA\n")
            tituloFavorita = mc.pedirTitulo()
            mc.hacerFavorita(tituloFavorita)
            os.system("pause")

        case "5":
            os.system("cls")
            print("MOSTRAR CANCIONES\n")
            mc.mostrarLista()
            os.system("pause")
        case "6":
            os.system("cls")
            print(
                "Gracias por utilizar el sistema de gestión de canciones. Hasta pronto. "
            )
            break
        case _:
            os.system("cls")
            print("ERROR, opción inválida. ")
