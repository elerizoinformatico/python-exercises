"""
Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
La primera con los números pares y la segunda con los números impares.

Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares) [2, 6]
print(impares) [1, 5, 7]
"""

def separar(lista):
    lista.sort() # Ordenamos la lista
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

numeros = [-12, 84, 13, 20, -33, 101, 9]
pares, impares = separar(numeros)
print(pares)
print(impares)
