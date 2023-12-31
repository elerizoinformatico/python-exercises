"""
El objetivo del ejercicio es modificar el contenido de la matriz dinámicamente,
sustituyendo todos sus números pares por 0 y los impares por 1.
"""

matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]

# Recorremos la matriz
for i, fila in enumerate(matriz):
    for j, columna in enumerate(fila):
        if matriz[i][j] % 2 == 0: # Si es par reemplazamos por un 0
            matriz[i][j] = 0
        else: # En caso contrario, reemplazamos con un 1
            matriz[i][j] = 1

print(matriz)
