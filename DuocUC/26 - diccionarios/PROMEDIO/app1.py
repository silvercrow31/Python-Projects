import moduloPrint as mp  # ALIAS

n1 = float(input("Ingrese nota 1: "))
n2 = float(input("Ingrese nota 2: "))
n3 = float(input("Ingrese nota 3: "))
estado = ""
prom = mp.calcularPromedio(n1, n2, n3)

if prom >= 4:
    estado = "APROBADO"
elif prom < 4:
    estado = "REPROBADO"

mensaje = f"{prom} estás {estado}"
mp.imprimirCaja(mensaje)
