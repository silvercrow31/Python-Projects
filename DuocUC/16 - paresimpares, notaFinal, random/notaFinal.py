import os
nota1=0
nota2=0
nota3=0
notaPresentacion=0
notaExamen=0
notaFinal=0

os.system("cls")
nota1=float(input("Ingrese nota 1: "))
nota2=float(input("Ingrese nota 2: "))
nota3=float(input("Ingrese nota 3: "))

notaPresentacion = round((nota1*0.3 + nota2*0.4 + nota3*0.3), 1)

notaExamen = float(input("Ingrese nota Examen: "))

notaFinal = round((notaPresentacion*0.6 + notaExamen*0.4), 1)

print(f'''
      
      Su nota de presentación es:   {notaPresentacion}
      
      Su nota final es:             {notaFinal}
            
      ''')