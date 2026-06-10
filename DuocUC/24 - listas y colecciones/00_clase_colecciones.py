import os
os.system("cls")
# Una coleccion es un grupo de datos.

# 1. Listas: coleccion DINAMICA

# Index         0           1       2
verduras = ["zanahoria","tomate","palta"]

print(verduras)


#   ----------  Funciones de listas ----------
print(f"\n{verduras[2]} tiene el index 2!!!")

print("\n----------       APPEND y REMOVE     ----------")

# .remove() elimina por NOMBRE
verduras.append("lechuga")
verduras.remove("palta")
print(verduras)

verduras.remove("tomate")
verduras.append("papas")
print(verduras)

print("\n----------     INSERT      ----------")

verduras.insert(1, "repollo")
print(verduras)

# .pop() elimina por INDEX
# si no se especifica indice, se elimina el elemento de la última posición

print("\n ----------    POP     ----------") 

verduras.pop(0)
print(verduras)

verduras.pop(1)
print(verduras)

verduras.pop()
print(verduras)