"""
A partir de una variable llamada tupla debes imprimir por pantalla los siguientes apartados
(usando un print() para cada apartado), de forma ordenada:
- El último elemento de la tupla.
- El número de elementos que tiene la tupla.
- La posición donde se encuentra el número 123 de la tupla.
- Una lista con los primeros tres elementos de la tupla.
- El elemento que hay en la posición con índice 4 de la tupla.
- El número de veces que aparece el número 4 en la tupla.
Nota: En total son 6 prints uno debajo de otro, no puedes redefinir ni modificar la tupla o
el test fallará, simplemente muestra lo que se pide por pantalla.
"""

print(tupla[-1])
print(len(tupla))
print(tupla.index(123))
print(list(tupla[:3]))
print(tupla[4])
print(tupla.count(4))
