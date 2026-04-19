import os

#-----------------------------VARIABLES
op=""
cantidad= 0
happy="N"
producto=""
cantidad=0
total=0
precio=0
descuento=0
subtotal=0

#----------------------------CODIGO PPAL

os.system("cls")

print('''
    ________________________________________
                    MENU
    1. Vodka tónica                    $5500
    2. Ron cola                        $5000
    3. Cerveza                         $2000
    4. Bebida                          $1500
    ________________________________________  

''')




op=str(input("Seleccione una opción: "))

if op=="1":
    producto="vodka tónica"
    precio=5500

elif op=="2":
    producto="ron cola"
    precio=5000

elif op=="3":
    producto="cerveza"
    precio=2000

elif op=="4":
    producto="bebida"
    precio=1500

else:
    print("Error: opción no válida")

cantidad=str(input(f"Ingrese cantidad deseada de {producto}: "))


#----------------------------CALCULO TOTAL
subtotal=precio*int(cantidad)
total=precio*int(cantidad)

happy=str(input("Happy hour? (S/N)")).strip().upper()

if happy == "S":
    descuento=total-(total/2)
    total = total/2

#----------------------------PRINT BOLETA

os.system("cls")

print(f'''
=========================================================      
      
                        ESTA VENTA
      
      Producto: {producto.upper()}
      Valor: {precio}
      Cantidad: {cantidad}
      
      {precio} X {cantidad}
      
      
      
      
      Subtotal:                                 {subtotal:.0f}
''')


if happy=="S":
    print(f'''      
      Dscto 50% (Happy Hour):                   {descuento:.0f}
      ''')
    
print(f'''      
      Total:                                    {total:.0f}      
      
=========================================================      

''')
