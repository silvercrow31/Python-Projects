import os
import moduloIMC as imcm

os.system("cls")

nombre = str(input("Ingrese su nombre: "))

peso = float(input("Ingrese su peso (Kg): "))
estatura = float(input("Ingrese su estatura (m): "))

imc = imcm.calcularIMC(peso, estatura)
clasificacion = imcm.determinarClasificacion(imc)

os.system("cls")

imcm.imprimirTicket(nombre, peso, estatura, imc, clasificacion)
