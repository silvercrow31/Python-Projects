import os

valorCuotaAPagar=0
valorKitAPagar=0
cantidadIntegrantes=0
quintil=0
descuentoCuota=0
descuentoKit=0
valorCuotaMensual=12_000
valorKitInicial=15_000

while True:                             #input cantidadIntegrantes con validación
    cantidadIntegrantes=int(input("Ingrese integrantes del hogar: "))
    if (cantidadIntegrantes>0):
        break
    else:
        print("ERROR: el numero de integrantes debe ser positivo. ")
        os.system("pause")
        


while True:                             #input quintil con validación
    quintil=int(input("Ingrese quintil (1 a 5): "))
    if (quintil==1 or quintil==2 or quintil==3 or quintil==4 or quintil==5): #comprobar
        break
    else:
        print("ERROR: El quintil debe ser un número entero entre 1 y 5. ")
        os.system("pause")
        

#--------------------------------------CODIGO PPAL

# descuentos en cuota segun quintil y cantidad de integrantes
if (cantidadIntegrantes>=5):
    if (quintil==1) or (quintil==2):
        descuentoCuota+=valorCuotaMensual*0.25
    elif (quintil==3) or (quintil==4):
        descuentoCuota+=valorCuotaMensual*0.18

elif (2<=cantidadIntegrantes<5):
    if (quintil==1) or (quintil==2):
        descuentoCuota+=valorCuotaMensual*0.15
    elif (quintil==3) or (quintil==4):
        descuentoCuota+=valorCuotaMensual*0.10

# descuentos en kit
if (quintil==1) or (quintil==2) or (quintil==3):
    descuentoKit+=valorKitInicial*0.12
if cantidadIntegrantes>=4:
    descuentoKit+=valorKitInicial*0.05
if (quintil==5) or (cantidadIntegrantes<2):
    descuentoCuota=0

valorCuotaAPagar=valorCuotaMensual-descuentoCuota
valorKitAPagar=valorKitInicial-descuentoKit

os.system("cls")

print(f'''
      
      El valor de la cuota es:  ${valorCuotaAPagar:,.0f}
      El valor del kit es:      ${valorKitAPagar:,.0f}
      
      ''')

# print(f'''
#             ________________________________
#       DEBUGGING
#       descuento cuota: {descuentoCuota}
#       descuento kit: {descuentoKit}
#       quintil: {quintil}
#       ''')