#________________________VARIABLES
import os

opMenu=""
producto=""
valorUnitario=0
esMayorista=False
descuento=0
cantidadProducto=0
pagoEfectivo=""
subtotal=0
totalCompra=0


#________________________Menu    

os.system("cls")

opMenu=str(input('''

    Bienvenido a PlasTic.

                
    Producto                Valor Unitario
    ______________________________________
    
    1. Tazon                $500
    2. Llavero              $200
    3. Polera estampada     $3.000
    
    Seleccione una opción del menú: 
                
'''))

if opMenu=="1":
    producto="tazon"
    cantidadProducto=int(input(f"Ingrese cantidad de {producto} a comprar: "))
    
    if cantidadProducto>=100:
        esMayorista=True
        valorUnitario=300
    elif cantidadProducto<100:
        valorUnitario=500
        
    
elif opMenu=="2":
    producto="llavero"
    cantidadProducto=int(input(f"Ingrese cantidad de {producto} a comprar: "))
    if cantidadProducto>=300:
        esMayorista=True
        valorUnitario=150
    elif cantidadProducto<150:
        valorUnitario=200
        
elif opMenu=="3":
    producto="polera estampada"
    cantidadProducto=int(input(f"Ingrese cantidad de {producto} a comprar: "))
    if cantidadProducto>=50:
        esMayorista=True
        valorUnitario=2000
    elif cantidadProducto<50:
        valorUnitario=3000
else:
    print("Error desconocido")

subtotal=cantidadProducto*valorUnitario

if esMayorista==True:
    pagoEfectivo=str(input("¿Paga en efectivo? S/N")).strip().upper()
    if pagoEfectivo=="S":
        descuento=subtotal*0.1

totalCompra=subtotal-descuento

#________________________Print

os.system("cls")
    
print(f'''
        _______________________________________
        
        Producto: {producto.upper()}
        Cantidad: {cantidadProducto}
        Valor unitario: {valorUnitario:.0f}
        ¿Es Mayorista? {esMayorista}
        Descuento 10%: {descuento:.0f}
        
        Total compra: {totalCompra:.0f}
        
        Gracias por su compra
        _______________________________________
        
        ''')

# Problema detectado: cuando se supera la cantidad minima para ser mayorista y el pago es en efectivo el total reportado es cero