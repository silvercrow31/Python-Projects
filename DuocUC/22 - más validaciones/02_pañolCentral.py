import os

op = 0
disponibles = 150
contadorPrestamosActivos = 0


os.system("cls")

print(
    "¡Bienvenido al sistema de gestión de préstamos del Pañol Central de Herramientas!"
)
os.system("pause")

while True:
    os.system("cls")
    print("""
        === MENÚ PRINCIPAL ===
        1. Herramientas disponibles
        2. Realizar préstamo
        3. Devolver herramienta
        4. Historial de movimientos
        5. Salir\n
          """)
    op = int(input("Seleccione una opción: "))
    match op:
        case 1:
            print(f"Herramientas disponibles: {disponibles}")
            os.system("pause")

        case 2:
            while True:
                egreso = int(input("""
                --- PRESTAMO ---
                Ingrese la cantidad de unidades deseadas: 
                """))
                if egreso <= 0:
                    print("ERROR: la cantidad solicitada debe ser mayor que cero. ")
                    os.system("pause")
                elif egreso > disponibles:
                    print("ERROR: la cantidad solicitada supera el stock disponible. ")
                    os.system("pause")
                elif egreso >= 0 and egreso <= disponibles:
                    print("Préstamo aprobado. ")
                    os.system("pause")
                    contadorPrestamosActivos += 1
                    disponibles -= egreso
                    break

        case 3:
            while True:
                ingreso = int(input("""
                --- DEVOLUCION ---
                    Ingrese la cantidad de unidades deseadas:    
                    """))
                if ingreso <= 0:
                    print("ERROR: el número debe ser mayor a cero")
                    os.system("pause")
                elif ingreso + disponibles > 150:
                    print("ERROR: se ha excedido el límite de herramientas en stock")
                    os.system("pause")
                    break
                elif ingreso > 0 and ingreso + disponibles <= 150:
                    print("Devolución aprobada. ")
                    os.system("pause")
                    if contadorPrestamosActivos > 0:
                        contadorPrestamosActivos -= 1
                    disponibles += ingreso
                    break
        case 4:
            print(f"Cantidad de préstamos activos: {contadorPrestamosActivos}")
            os.system("pause")

        case 5:
            break
os.system("cls")
print("Gracias por utilizar nuestro software de pañol, hasta la próxima. ")
os.system("pause")
