# recibe peso en Kg y estatura en metros
def calcularIMC(peso, estatura):
    imc = round((peso / estatura**2), 1)  # REVISAR; NO CALCULA IMC
    return imc


def determinarClasificacion(imc):
    clasificacion = ""
    if imc < 18.5:
        clasificacion = "BAJO PESO"
    elif 18.5 <= imc <= 24.9:
        clasificacion = "SALUDABLE"
    elif 24.9 < imc:
        clasificacion = "SOBREPESO"
    return clasificacion


def imprimirTicket(nombre, peso, estatura, imc, clasificacion):
    print(f"""
===============TICKET===============
Nombre:             {nombre}
Peso:               {peso}
Estatura:           {estatura}
IMC:                {imc}
Clasificación:      {clasificacion}
====================================
""")
