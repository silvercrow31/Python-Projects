# # Una estructura de datos es una forma de organizar
# la información para que sea útil.

# Un diccionario es una estructura de datos compuesta
# por items. Los items se componen de 2 partes:
# LLAVE -> VALOR
# KEY -> VALUE

import os

os.system("cls")

persona = {"run": "111-1", "nombre": "Pablo", "edad": 26}

print(f"Diccionario: {persona}")


print(f"""
            Nombre:   {persona["nombre"]}
            Edad:     {persona["edad"]}
            RUN:      {persona["run"]}
      """)


# Cambiamos el valor de nombre y volvemos a imprimir el diccionario:

persona["nombre"] = "Carol"
persona["edad"] = "32"
persona["run"] = "222-2"

print(f"""
            Nombre:   {persona["nombre"]}
            Edad:     {persona["edad"]}
            RUN:      {persona["run"]}
      """)


# Podemos recorrer los items del diccionario:
# \t es un tabulador (4 espacios)

for key, value in persona.items():
    print(f"LLAVE: {key} \t VALOR: {value}")
