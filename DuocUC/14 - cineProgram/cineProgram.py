import os
#--------------------------VARIABLES-------------------------------------
edad=0
diaSemana=""
tipoPelicula=""
precioBase=0
tipoPublico=""
precioFinal=0
#--------------------------CODIGO PPAL-------------------------------------
os.system("cls")
print("#-------------CINEPROGRAM--------------")
edad=int(input("Ingrese su edad: "))

diaSemana=str(input("Ingrese dia semana: ")).strip().lower() #¿hay una forma de automatizar esto con fecha de sistema?

tipoPelicula=str(input("Ingrese tipo de película: ")).strip().upper()

#regla 1: cálculo del precio base
if edad<12:
    precioBase=2500
    tipoPublico="Niños"
elif 12<=edad<=17:
    precioBase=4000
    tipoPublico="Estudiantes"
elif 18<=edad<=64:
    precioBase=6000
    tipoPublico="Adultos"
elif edad >= 65:
    precioBase=3000
    tipoPublico="Adultos Mayores"

#regla 2: promocion mitad de semana
precioFinal = precioBase * 0.5 if diaSemana=="miercoles" else precioBase

#regla 3: control de acceso a salas (match-case)
match tipoPelicula:
    case "A":
        print("Tiene acceso a la película")
    case "C":
        if (tipoPublico == "Niños") or (tipoPublico == "Estudiantes"):
            print("NO tiene acceso a la película!!!")
        elif (tipoPublico=="Adultos") or (tipoPublico=="Adultos Mayores"):
            print("Tiene acceso a la película")
    case _:
        print("La categoría no es válida")
     
os.system("cls")
        
print(f'''
      TICKET
      -------------------------------
      Edad: {edad}
      Día semana: {diaSemana}
      Tipo publico: {tipoPublico}
      Tipo película: {tipoPelicula}
      Precio base: {precioBase}
      _______________________________
      
      Precio final: {precioFinal}
      
      
      ''')