# Crear una lista llamada notas a la que se cargan 100 noras random entre 1 y 7
# luego determinar entre estas notas cuántos son azules >=4 y rojos <4
# OBS. use random.randint(1,7)
import random
import os

notas = []
contadorAzules = 0
contadorRojos = 0


os.system("cls")

for _ in range(100):
    nuevaNota = random.randint(1, 7)
    notas.append(nuevaNota)
    if nuevaNota >= 4:
        contadorAzules += 1
    elif nuevaNota < 4:
        contadorRojos += 1

prom = sum(notas) / len(notas)


print(f"""\n
      Se han registrado {len(notas)} notas exitosamente. 
      Azules: {contadorAzules}
      Rojos: {contadorRojos}
      """)
print(notas)
print(f"Promedio de notas: {prom}")
