import os

os.system("cls")


promedio= float(input("Ingrese promedio: "))

# comentar  bloque: CTRL + CIERRE DE LLAVE (})

# if ternario:


estado = "APROBADO" if promedio >= 4 else "REPROBADO"

print(f"Promedio: {promedio}     Estado: {estado}")