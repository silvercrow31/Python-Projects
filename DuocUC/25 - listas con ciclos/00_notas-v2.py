import random
import os

os.system("cls")

notas = []

for _ in range(20):
    notas.append(random.randint(1, 7))

print(f"Todas las notas:        {notas}")

listaAzules = []

for k in range(20):
    if notas[k] >= 4:
        listaAzules.append(notas[k])


print(f"Notas azules:       {listaAzules}")


cantidad = notas.count(4)
print(f"Hay {cantidad} notas 4. ")
