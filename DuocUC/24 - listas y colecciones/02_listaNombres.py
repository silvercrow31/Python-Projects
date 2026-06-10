import os

profes = []
# queremos cargar 3 nombres de profes
# como sabemos la cantidad de iteraciones usamos un ciclo for

# cuando no se usa el indice del ciclo for se usa un _
for _ in range(3):
    profes.append(str(input("""
                            Ingrese profe: 
                            """)).upper())

print(profes)

# los ordenamos usando sort()

profes.sort()  # ordena alfabeticamente
print(profes)
