import os
os.system("cls")

#-----------------------------VARIABLES

nombre          = ""            #nombre del usuario
estatura        = 0             #
peso            = 0             #
imc             = 0             #
clasificacion   = ""            #

#-----------------------------CODIGO PPAL

nombre=str(input("Por favor, ingrese su nombre: ")).strip()

os.system("cls")

estatura=float(input("Ingrese su estatura en metros: "))

os.system("cls")

peso=float(input("Ingrese su peso en Kg: "))

os.system("cls")

#-----------------------------CALCULO IMC
imc = peso/(estatura)**2

#-----------------------------ASIGNACION DE CLASIFICACION
if imc < 18.5:
    clasificacion="bajo peso"
elif (imc >= 18.5) & (imc <= 24.9):
    clasificacion="normal"
elif (imc>=25) & (imc<=29.9):
    clasificacion="sobrepeso"
elif imc>30:
    clasificacion="obesidad"
else:
    print("Error: IMC calculado escapa a los valores de clasificación.")

#-----------------------------PRINT TICKET

os.system("cls")

print(f'''
=========================================================      
      
      Nombre: {nombre}
      Peso: {peso}
      Estatura: {estatura}
      
      IMC calculado: {imc:.2f}
      
      Usted pertenece a la categoría {clasificacion}.
      
=========================================================      

''')



