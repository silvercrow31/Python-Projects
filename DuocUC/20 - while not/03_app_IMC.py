import os
import time

op = ""
clasificacion = ""
sexo = ""
nombre, estatura, peso = 0, 0, 0
imc, promedioHombres, promedioMujeres = 0, 0, 0
hombresSobrepeso, mujeresBajoPeso = 0, 0

while True:
    os.system("cls")
    # Se muestra el menu de forma ciclica
    print("""
                 ---------- MENU ----------
                 1. Calcular IMC y clasificación
                 2. Ver estadísticas
                 3. Salir\n  
                 """)
    op = str(input("Elija opción: "))

    if op == "1":
        # 1. Calcular IMC y clasificación
        os.system("cls")
        print("----- Calculo IMC -----")

        # input nombre y validacion
        nombre = str(input("Ingrese su nombre: ")).strip().upper()
        while not (len(nombre) > 0):
            print("ERROR: el nombre no puede estar vacio")
            nombre = str(input("Ingrese su nombre: ")).strip().upper()

        # input sexo y validacion
        sexo = str(input("Ingrese su sexo: ")).strip().upper()
        while not (sexo == "M" or sexo == "F"):
            print("ERROR: sexo debe ser F o M")
            sexo = str(input("Ingrese su sexo: ")).strip().upper()

        # input peso y validacion
        peso = float(input("Ingrese su peso en kilogramos: "))
        while not (peso >= 1):
            print("ERROR: el peso debe ser mayor o igual a 1")
            peso = float(input("Ingrese su peso: "))

        # input estatura y validacion
        estatura = float(input("Ingrese su estatura en metros: "))
        while not (estatura >= 1):
            print("ERROR: la estatura debe ser mayor o igual a 1")
            estatura = float(input("Ingrese su estatura: "))

        imc = peso / (estatura**2)

        if imc < 18.5:
            clasificacion = "BAJO PESO"
        elif 18.5 <= imc <= 24.9:
            clasificacion = "NORMAL"
        elif 25 <= imc <= 29.9:
            clasificacion = "SOBREPESO"
        elif imc > 30:
            clasificacion = "OBESIDAD"

        # Para las estadísticas
        if clasificacion == "SOBREPESO" and sexo == "M":
            hombresSobrepeso += 1
        if clasificacion == "BAJO PESO" and sexo == "F":
            mujeresBajoPeso += 1

        os.system("cls")

        print(f"""
              --------------- TICKET ---------------
              Nombre:               {nombre}
              Sexo:                 {sexo}
              Estatura:             {estatura}
              Peso:                 {peso}
              
              IMC:                  {imc}
              Clasificación:        {clasificacion}
              """)
        os.system("pause")
    if op == "2":
        # 2. Estadísticas
        os.system("cls")
        print("----- Estadísticas -----")
        os.system("pause")

    if op == "3":
        # 3. Salir
        os.system("cls")
        print("...cerrando app")
        time.sleep(1)
        break
