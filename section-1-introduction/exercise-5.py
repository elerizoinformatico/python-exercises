# La siguiente matriz debe cumplir una condición:
# El cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
# Se debe modificar el código utilizando slicing para que se cumpla la condición.

matriz = [
  [1,1,1,3],
  [2,2,2,7],
  [3,3,3,9],
  [4,4,4,13]
]

# Ayuda: La función sum(lista) devuelve la suma de todos los elementos de una lista

matriz[1][-1] = sum(matriz[1][:-1])
matriz[-1][-1] = sum(matriz[-1][:-1])
