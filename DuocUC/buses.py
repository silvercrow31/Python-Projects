import os


#------------------------------- VARIABLES

origen="Santiago"
destino=""
precioPasaje=0
tipoPasaje=""
total=0
cantidad=0
descuento=0
opTipoPasaje=""
opMenu=""
pagoEfectivo=""
opPagoEfectivo=""
subtotal=0

#------------------------------- CODIGO PPAL

print('''
      Bienvenido a TarBas. 
      
      
         Destino                   Ida                 Ida y vuelta
      ____________________________________________________________
      
      1. Curicó                    $5.000              $8.000
      2. Temuco                    $12.000             $20.000
      3. Puerto Montt              $15.000             $28.000
      
      ''')



opMenu=str(input("Por favor seleccione uno de nuestros servicios disponibles: \n "))

if opMenu=="1":
    destino="Curicó"
    opTipoPasaje=str(input('''¿Ida y vuelta?
                           1. Solo ida
                           2. Ida y vuelta
                           '''))
    
    if opTipoPasaje=="1":
        tipoPasaje="ida"
        precioPasaje=5000
        
    elif opTipoPasaje=="2":
        tipoPasaje="ida y vuelta"
        precioPasaje=8000
    else:
        Print("Error: opción seleccionada no es válida")
        
elif opMenu=="2":
    destino="Temuco"
    opTipoPasaje=str(input('''¿Ida y vuelta?
                              1. Solo ida
                              2. Ida y vuelta
                           '''))
        
    if opTipoPasaje=="1":
        tipoPasaje="ida"
        precioPasaje=12000
        
    elif opTipoPasaje=="2":
        tipoPasaje="ida y vuelta"
        precioPasaje=20000
        
    else:
        Print("Error: opción seleccionada no es válida")
    
elif opMenu=="3":
    destino="Puerto Montt"
    opTipoPasaje=str(input('''¿Ida y vuelta?
                             1. Solo ida
                             2. Ida y vuelta
                           '''))
        
    if opTipoPasaje=="1":
        tipoPasaje="ida"
        precioPasaje=15000
        
    elif opTipoPasaje=="2":
        tipoPasaje="ida y vuelta"
        precioPasaje=28000
        
    else:
        Print("Error: opción seleccionada no es válida")
    
else:
    print("Error: opción seleccionada no es válida")
    
cantidad=int(input(f"¿Cuántos pasajes de {tipoPasaje} a {destino} desea comprar? "))

    
#------------------------------- CALCULO DSCTO
subtotal=precioPasaje*cantidad

pagoEfectivo=str(input("¿Paga en efectivo? (S/N)")).strip().upper()

if pagoEfectivo=="S":
    descuento=subtotal*0.1
    total=subtotal*0.9

#------------------------------- PRINT FINAL

print(f'''
      TICKET
      
      Valor pasaje: ({destino}, {tipoPasaje})        {precioPasaje}
      Cantidad:                                      {cantidad}


      Subtotal:                                      {subtotal}
      Descuento:                                     {descuento}
      Total:                                         {total}
      
      ''')
