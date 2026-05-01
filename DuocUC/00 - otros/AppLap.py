import os

os.system("cls")  # Limpiar pantalla

#----------------------------VARIABLES-----------------------------
# SE DEFINEN, INICIALIZAN Y DOCUMENTAN

nombre=""               # nombre empleado
edad=18                 # edad empleado en años
sexo="F"                # F: femenino   M: masculino
valorHora=0             # valor por 1 hora
hrsTrabajadas=0         # Hrs(float) trabajadas
sueldoBruto=0           # valor hora X hrs trabajadas
dsctoSalud=0            # 7% del sueldo bruto
dsctoPension=0          # 13% del sueldo bruto
liquidoPagar=0          # bruto menos descuento



#   SEGMENTAR CODIGO Y DOCUMENTAR

nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
sexo = str(input("Ingrese su sexo (F/M): "))
valorHora = int(input("Ingrese valor/hora: "))
hrsTrabajadas = float(input("Ingrese horas trabajadas: "))

sueldoBruto = valorHora * hrsTrabajadas
dsctoSalud = sueldoBruto * 0.07
dsctoPension = sueldoBruto * 0.13
liquidoPagar = sueldoBruto - dsctoPension - dsctoSalud

os.system("cls")

sexo=sexo.upper()

if sexo == "F":
    añosParaJubilar = 60 - edad
elif sexo == "M":
    añosParaJubilar = 65 - edad
else:
    print("Error: Sexo ingresado no es válido. ")
    
print(f'''
        -----------------------LIQUIDACION DE SUELDO-----------------------
                        
                        Nombre: {nombre}   Edad: {edad}
                        Sexo: {sexo}      
                        
                        Valor Hora: {valorHora}
                        Horas Trabajadas: {hrsTrabajadas:.0f}
                        
                        Sueldo Bruto: {sueldoBruto:.0f}
                        Descuento de Salud: {dsctoSalud:.0f}
                        Descuento de Pensión: {dsctoPension:.0f}
                        Sueldo Líquido: {liquidoPagar:.0f}
                        
                        Le quedan {añosParaJubilar} años para jubilar.
        --------------------------------------------------------------------
''')