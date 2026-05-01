import os

zonaResidencial=""
temporada=""

opZonaResidencial=""
opTemporada=""

recargos=0
consumoMensual=0
consumoPromedio=0
descuentos=0
edad=0
total=0
tarifa=0

os.system("cls")

opZonaResidencial=str(input('''
                          Seleccione su zona residencial(Rural/Urbana/Turística):
                          
                            1. Rural
                            2. Urbana
                            3. Turística
                          
                          '''))

os.system("cls")


opTemporada=str(input('''
                          Seleccione temporada (normal/alta) :
                          
                            1. Normal
                            2. Alta
                          
                          '''))

match opTemporada:
    case "1":
        temporada="Normal"
    case "2":
        temporada="Alta"

os.system("cls")

consumoMensual=int(input("Ingrese su consumo mensual (en metros cúbicos): "))

os.system("cls")

edad=int(input("Ingrese su edad: "))


# ----------------------------------------------------------CALCULOS TARIFA, CONSUMO Y TOTAL

match opZonaResidencial:
    case "1":
        zonaResidencial="Rural"
        consumoPromedio=12
        
        if consumoMensual<=15:
            tarifa=200
        elif consumoMensual>15:
            tarifa=300
            
    case "2":
        zonaResidencial="Urbana"
        consumoPromedio=18
        
        if consumoMensual<=20:
            tarifa=400
        elif consumoMensual>20:
            tarifa=500
            
    case "3":
        zonaResidencial="Turística"
        consumoPromedio=22
        
        if consumoMensual<=25:
            tarifa=600
        elif consumoMensual>25:
            tarifa=700

total=consumoMensual*tarifa

# ----------------------------------------------------------CALCULOS RECARGOS Y DESCUENTOS
#RECARGOS
if (temporada == "Alta") and (zonaResidencial == "Turística"):
    recargos+=total*0.3

if (temporada == "Alta") and (zonaResidencial == "Urbana"):
    recargos+=total*0.15   

if (consumoMensual>30) and (temporada=="Alta"):
    recargos+=5000
    
#DESCUENTOS
if (zonaResidencial=="Rural") and  (consumoMensual<10):
    descuentos+=total*0.2
    
if (edad > 65) and (consumoMensual < consumoPromedio):
    descuentos+=3000

# ----------------------------------------------------------PRINT

os.system("cls")

print(f"El costo total de su consumo de agua es: ${total+recargos-descuentos}")

print(f'''
      DEBUGGING
      
      Zona {zonaResidencial}
      Temporada {temporada}
      c. mensual {consumoMensual}
      c. promedio {consumoPromedio}
      
      
      Descuentos: {descuentos}
      Recargos: {recargos}
      
      ''')
