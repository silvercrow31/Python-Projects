import os

os.system("cls")

nota1=float(input("Ingrese nota 1: "))

os.system("cls")


nota2=float(input("Ingrese nota 2: "))

os.system("cls")


nota3=float(input("Ingrese nota 3: "))

promedio=(nota1+nota2+nota3)/3

os.system("cls")

#Determinamos estado

estado=""
if promedio>=4:
    estado="APROBADO"
elif promedio<4:
    estado="REPROBADO"


print(
    
    f'''
    ----------------Ticket----------------

                Nota 1 = {nota1}
                Nota 2 = {nota2}
                Nota 3 = {nota3}
    
                Promedio = {promedio:.2f}
                
                Estado: {estado}
                
    --------------------------------------
    
    '''
    
)