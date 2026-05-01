import os

entradaGeneral=25_000
seguroObligatorio=5_000

descuentoEntrada=0
descuentoSeguroObligatorio=0

tipoPase=""
estatura=0

opTipoPase=""

os.system("cls")

print('''
      BIENVENIDO A ECOAVENTURA PARK
            Sistema de cobros

      ''')

estatura=int(input("Ingrese la estatura en centímetros del visitante: "))

opTipoPase=str(input('''
                    
                    Selecciona el tipo de pase del visitante: 
                        1. VIP
                        2. Estándar

''')).strip()

#----------------------------------------------------------asigna tipo de pase
match opTipoPase:
    case "1":
        tipoPase="VIP"
    case "2":
        tipoPase="Estándar"        

#----------------------------------------------------------evaluacion de condiciones
if (estatura <= 150):
    if (tipoPase == "VIP"):
        descuentoEntrada = entradaGeneral * 0.25
        seguroObligatorio *= 0.85
    elif (tipoPase == "Estándar"):
        descuentoEntrada = entradaGeneral * 0.15

elif (151 <= estatura <= 190):
    if (tipoPase == "VIP"):
        descuentoEntrada = entradaGeneral * 0.12
        descuentoSeguroObligatorio = seguroObligatorio*0.15
    elif (tipoPase == "Estándar"):
        descuentoEntrada = entradaGeneral * 0.08
    if estatura >= 185:
        descuentoSeguroObligatorio += seguroObligatorio*0.05

if estatura>190:
    descuentoEntrada=0

totalAPagar = round(entradaGeneral-descuentoEntrada+seguroObligatorio-descuentoSeguroObligatorio)

os.system("cls")

print(f'''
      
      estatura:                             {estatura}
      tipo pase:                            {tipoPase}
      
      valor entrada general:                {entradaGeneral}
      valor seguro obligatorio:             {seguroObligatorio}
      dscto entrada:                        -{descuentoEntrada}
      dscto seguro:                         -{descuentoSeguroObligatorio}
      
      
      
Total a pagar:                              {totalAPagar}
      
      ''')




# VALIDACIONES!!!!!!!!!!!!!!!!!
# while True:
#     estatura=int(input("ingrese estatura: "))
#     if estatura >= 50:
#         break
#     else:
#         print("La estatura debe ser mayor o igual a 50cm")

# while True:
#     if tipoPase=="VIP" or tipoPase=="Estándar":
#         break
#     else:
#         print("El tipo de pase solo puede ser V=VIP o E=Estándar")