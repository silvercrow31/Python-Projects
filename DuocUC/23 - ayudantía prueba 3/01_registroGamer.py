import os

nombre = ""
cantidad = 0
profesionales = 0
novatos = 0
listaJugadores = []

os.system("cls")

while True:
    try:
        cantidad = int(input("¿Cuántos jugadores desea registrar?: "))
        if cantidad <= 0:
            print(
                "El número ingresado es negativo. Debe ingresar un número entero positivo. "
            )
        else:
            break
    except ValueError:
        print("Debe ingresar un número entero positivo. ")


for i in range(cantidad):
    jugador = []
    jugador.append(i + 1)

    # registrar y validar nombre
    while True:
        os.system("cls")

        nombre = str(input("Ingrese el nombre del jugador: "))
        # valida nombre
        if len(nombre) < 6 or " " in nombre:
            print("Nombre inválido. Debe tener minimo 6 caracteres y sin espacios. ")
            os.system("cls")
        else:
            jugador.append(nombre)
            break

    # registrar y validar nivel
    while True:
        os.system("cls")
        # nivel
        try:
            nivel = int(input("Ingrese el nivel del jugador: "))
            if nivel <= 0:
                print("¡Nivel inválido! Ingresa un entero positivo.")
                os.system("pause")
            elif nivel > 0:
                jugador.append(nivel)
                break

        except ValueError:
            print("¡Nivel inválido! Ingresa un entero positivo.")
            os.system("pause")

    # clasificar jugador
    clasificacion = ""

    if nivel >= 100:
        clasificacion = "Profesional"
        profesionales += 1
    elif nivel < 100:
        clasificacion = "Novato"
        novatos += 1
    jugador.append(clasificacion)
    listaJugadores.append(jugador)
    os.system("cls")
    print(f"\nJugador nº{i+1} Registrado : {nombre}, nivel {nivel}, {clasificacion}")
    os.system("pause")

os.system("cls")

print(f"""\nLista de jugadores registrados: 

{"Nº registro":<16} {"Nombre":<16} {"Nivel":<16} {"Clasificación":<16}
""")
print(64 * "-")
for x in listaJugadores:
    print(f"""
{x[0]:<16} {x[1]:<16} {x[2]:<16} {x[3]:<16}
""")
    print(64 * "-")
