# validacion 3

import os

nombre = (str(input("Ingrese nombre: "))).strip()

while not (len(nombre) > 0):

    # len() cuenta la cantidad de caracteres de un string

    print("ERROR, no puede ser vacio!!!!!!")
    nombre = (str(input("Ingrese nombre: "))).strip()

print("Nombre cargado exitosamente!!!!!")
