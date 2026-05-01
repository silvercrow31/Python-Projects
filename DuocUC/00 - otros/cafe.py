#-----------------------------VARIABLES
import os

op="0"
opAgregado="0"

precioProducto=0
producto=""
cantidad=0

deseaAgregados=""
agregado="n/a"
precioAgregado=0

canceloCon=0
totalCompra=0
vuelto=0

os.system("cls")

#-----------------------------MENU PPAL
print('''
                        MENU
      __________________________________________
      
      1. Espresso       $750
      2. Capuccino      $850
      3. Latte          $800
      4. Mocha          $830
      __________________________________________

''')

op=str(input("Seleccione una opción de nuestro menú: "))

if op=="1":
    producto="Espresso"
    precioProducto=750
    
if op=="2":
    producto="Capuccino"
    precioProducto=850

if op=="3":
    producto="Latte"
    precioProducto=800

if op=="4":
    producto="Mocha"
    precioProducto=830

#-----------------------------MENU AGREGADOS
os.system("cls")
print('''
              NUESTRO MENU DE AGREGADOS
      __________________________________________
      
      1. Leche                  $300
      2. Chocolate              $200
      3. Leche y Chocolate      $500
      __________________________________________

''')

deseaAgregados=str(input("¿Desea agregados? (S/N) ")).strip().upper()

if deseaAgregados=="S":

    opAgregado=str(input("Seleccione una opción de agregado: "))
    if opAgregado=="1":
        agregado="Leche"
        precioAgregado=300
        
    elif opAgregado=="2":
        agregado="Chocolate"
        precioAgregado=200
    
    elif opAgregado=="3":
        agregado="Leche y Chocolate"
        precioAgregado=500

    cantidad=int(input(f"Ingrese la cantidad de {producto.lower()} con {agregado.lower()} que desea comprar: "))


elif deseaAgregados=="N":
    cantidad=int(input(f"Ingrese la cantidad de {producto} que desea comprar: "))
    
if cantidad < 0:
    print("Error: la cantidad debe ser un número positivo. ")

canceloCon=int(input("¿Con cuánto dinero va a cancelar?: "))

totalCompra=cantidad*(precioProducto+precioAgregado)
vuelto=canceloCon-totalCompra

#-----------------------------TICKET
os.system("cls")
print(f'''
______________________________________________
      
                TICKET
      
    Tipo café:          {producto}
    Agregados:          {agregado}
    Cantidad:           {cantidad}
    Total compra:       {totalCompra}
    Canceló con:        {canceloCon}
    Vuelto:             {vuelto}

    Disfrute su café.
_______________________________________________
''')
