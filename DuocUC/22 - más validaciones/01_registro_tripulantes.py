import os

cantTripulantes = 0
cantEspecialista = 0
cantJunior = 0
idVueloInterno = ""
horasVueloTripulante = 0
clasificacionTripulante = ""

# 1. Definición del lote de ingreso
while True:
    os.system("cls")
    try:
        cantTripulantes = int(input("Ingrese cantidad total de tripulantes: "))
        if cantTripulantes > 0:
            break
        else:
            print("ERROR: debe ser un número mayor a cero. ")
            os.system("pause")

    except:
        print("ERROR: debe ser un número entero")
        os.system("pause")

# Se empieza a iterar por cada tripulante
for k in range(cantTripulantes):
    os.system("cls")
    print(f"Tripulante: {k+1}")
    idVueloInterno = str(input("Ingrese el Código de vuelo interno: ")).strip().upper()

    # 2. Validación del código de vuelo
    while True:
        os.system("cls")
        idVueloInterno = (
            str(input("Ingrese el Código de vuelo interno: ")).strip().upper()
        )
        if len(idVueloInterno) < 6:
            print("ERROR: debe tener al menos 6 carácteres")
            os.system("pause")

        elif " " in idVueloInterno:
            print("ERROR: el código no debe contener espacios")
            os.system("pause")

        elif (len(idVueloInterno) >= 6) and (" " not in idVueloInterno):
            break

    # 3. Registro de horas de vuelo
    while True:
        try:
            horasVueloTripulante = int(
                input(
                    "Ingrese el histórico de horas de vuelo acumuladas para este tripulante: "
                )
            )
            os.system("cls")
            if horasVueloTripulante < 0:
                print("ERROR: el número ingresado debe ser un entero positivo o cero. ")
                os.system("pause")

            elif horasVueloTripulante >= 0:
                break
        except:
            print(
                "¡Error de bitácora! Ingresa un número entero positivo para las horas de vuelo. "
            )
            os.system("pause")

    # 4. Clasificación jerárquica automatizada
    if horasVueloTripulante > 500:
        clasificacionTripulante = "Especialista Senior"
        cantEspecialista += 1
    elif horasVueloTripulante <= 500:
        clasificacionTripulante = "Residente Junior"
        cantJunior += 1


print(
    f"¡La aerolínea cuenta con {cantEspecialista} Especialistas Senior y {cantJunior} Residentes Junior! ¡Personal listo para despegar!"
)
