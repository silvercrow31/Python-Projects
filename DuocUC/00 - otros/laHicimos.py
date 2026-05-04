import os

valorEntrada = 0
op=""
descuento=0
subtotal=0
total=0
cantidadEntradas=0
aplicaDescuento=""
totalCLP=""

os.system("cls")

while True:
    op=str(input('''

                Productora LAHICIMOS
      
        Categoría               Precio
      ________________________________________

    1   Galería                 $25.000
    2   Cancha                  $55.000
    3   Tribuna                 $80.000
    4   Cancha VIP              $100.000                 

    Seleccione un tipo de entrada: 
'''))
    if (op=="1" or op=="2" or op=="3" or op=="4"):
         #el dato es correcto
        break
    else:
        #el dato es incorrecto
        print("ERROR: Debe seleccionar una opción válida. ")
        os.system("pause")
        os.system("cls")

match op:
    case "1":
        categoria="Galería"
        valorEntrada=25_000
    case "2":
        categoria="Cancha"
        valorEntrada=55_000
    case "3":
        categoria="Tribuna"
        valorEntrada=80_000
    case "4":
        categoria="Cancha VIP"
        valorEntrada=100_000



while True:
    os.system("cls")
    aplicaDescuento=str(input("¿Las entradas fueron compradas con anticipación? S/N ")).strip().upper()
    if aplicaDescuento=="S" or aplicaDescuento=="N":
        break
    else:
        print("ERROR: Ingrese una respuesta válida (S/N)")
        os.system("pause")


while True:
    os.system("cls")

    cantidadEntradas=int(input(f"¿Cuántas entradas {categoria} desea comprar?"))

    if cantidadEntradas<=0:
        print("ERROR: La cantidad de entradas debe ser un numero positivo")
    
    elif (cantidadEntradas>5) and (aplicaDescuento=="S"):
        print("ERROR: No se pueden comprar más de 5 entradas con anticipación. ")
    
    else:
        break

    os.system("pause")

if aplicaDescuento=="S":
    descuento=valorEntrada*0.1

#____________________________________________CALCULO DE TOTAL

if categoria=="Cancha VIP":
    total=(valorEntrada-descuento)+(valorEntrada*(cantidadEntradas-1))
else:
    total=cantidadEntradas*(valorEntrada-descuento)

#____________________________________________PRINT FINAL TICKET

os.system("cls")
totalCLP=f"{total:,.0f}".replace(",",".")
print(f'''

        TICKET
    Esta venta: {cantidadEntradas} entradas {categoria}

    TOTAL A PAGAR: ${totalCLP}

''')

