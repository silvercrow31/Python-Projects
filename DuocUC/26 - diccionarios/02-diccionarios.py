# Vamos a crear un diccionario con valores por defecto
# los cuales vamos a reemplazar por valores dados por el user

import os

os.system("cls")

empleado = {
    "RUN": "NO INFO",
    "NOMBRE": "NO INFO",
    "EDAD": "0",
    "CARGO": "NO INFO",
    "CASADO": False,
    "SUELDO": 0,
}

empleado["RUN"] = str(input("Ingrese su RUN: ")).strip().upper()
empleado["NOMBRE"] = str(input("Ingrese su nombre: ")).strip().upper()
empleado["EDAD"] = int(input("Ingrese su edad: "))
empleado["CARGO"] = str(input("Ingrese su cargo: ")).strip().upper()
empleado["CASADO"] = bool(input("¿Está casado/a?: "))
empleado["SUELDO"] = int(input("Ingrese su sueldo: "))

print(empleado)
