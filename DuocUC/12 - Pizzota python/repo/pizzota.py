import os
#-----------------------------------------------VARIABLES

opMenu="0"                         #op para menu ppal
opTamano="0"                         #op para tamaño pizza
opAgregado="0"                         #op para agregados
opFormaPago="0"

valorPizza=0
valorAgregado=0
subtotal=0                      #sin descuentos
totalCompra=0                   #precio final a pagar
cantidad=0
descuento=0

tamanoPizza=""
tipoPizza=""
tipoAgregado=""

formaPago=""
deseaAgregado="N"                #por defecto se asume que no quiere agregado


#-----------------------------------------------CODIGO
os.system("cls")

print('''
        __________________________________________________

                            MENU PIZZOTA
        
        Tipo Pizza              Mediana         Familiar
        __________________________________________________
        
        1. Napolitana           $10.000         $18.000
        2. Vegetariana          $8.000          $17.000
        3. Española             $12.000         $20.000
        __________________________________________________


      ''')

opMenu=str(input("Seleccione una opción: "))

if opMenu=="1":
    tipoPizza="Napolitana"
    
    opTamano=str(input("Seleccione tamaño de pizza deseado: ")).strip().upper()
    
    if opTamano=="M":
        tamanoPizza="Mediana"
        valorPizza=10_000
        
    elif opTamano=="F":
        tamanoPizza="Familiar"
        valorPizza=18_000

if opMenu=="2":
    tipoPizza="Vegetariana"
    
    opTamano=str(input("Seleccione tamaño de pizza deseado: ")).strip().upper()
    
    if opTamano=="M":
        tamanoPizza="Mediana"
        valorPizza=8_000
        
    elif opTamano=="F":
        tamanoPizza="Familiar"
        valorPizza=17_000       

if opMenu=="3":
    tipoPizza="Española"
    
    opTamano=str(input("Seleccione tamaño de pizza deseado: ")).strip().upper()
    
    if opTamano=="M":
        tamanoPizza="Mediana"
        valorPizza=12_000
        
    elif opTamano=="F":
        tamanoPizza="Familiar"
        valorPizza=20_000

cantidad=int(input(f"¿Cuántas pizzas {tipoPizza.lower()}s desea llevar?"))

os.system("cls")

print('''
        __________________________________________________

                            MENU AGREGADOS
        
        Agregado                                Precio         
        __________________________________________________
        
        1. Palos de ajo                         $3.000
        2. Aros de cebolla                      $2.200 
        3. Palos de ajo y Aros de cebolla       $5.200
        4. Sin agregados                        $0
        __________________________________________________

      ''')

opAgregado=str(input("¿Desea llevar agregados con su compra?: "))

if opAgregado==1:
    tipoAgregado="Palos de ajo"
    valorAgregado=3000
    
elif opAgregado==2:
    tipoAgregado="Aros de cebolla"
    valorAgregado=2200
    
elif opAgregado==3:
    tipoAgregado="Palos de ajo y Aros de cebolla"
    valorAgregado=5200
    
elif opAgregado==1:
    tipoAgregado="Sin agregado"
    valorAgregado=0


#-----------------------------------------------FORMA DE PAGO
opFormaPago=str(input('''
Seleccione forma de pago:

1. Efectivo
2. Tarjeta
'''))

#-----------------------------------------------CALCULOS

subtotal=cantidad*(valorPizza+valorAgregado)


if opFormaPago==1:
    formaPago="Efectivo"
    totalCompra=subtotal*0.8
    descuento=subtotal-totalCompra
    
elif formaPago==2:
    formaPago="Tarjeta"
    totalCompra=subtotal



#-----------------------------------------------TICKET


print(f'''
        _________________________________________________________________

                                    TICKET
        
        Tipo Pizza: {tipoPizza}         ${valorPizza}       x{cantidad}
        Agregado:   {tipoAgregado}      ${valorAgregado}
        
        
        Forma de pago:                  {formaPago}
        
        Subtotal:                       ${subtotal}
        Descuento:                      ${descuento}
        _________________________________________________________________

        Total a pagar: {totalCompra}
        _________________________________________________________________


      ''')