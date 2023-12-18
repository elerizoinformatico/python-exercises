"""
Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio.
Calcula el área de un círculo de 5 de radio.

Nota: Puedes utilizar el valor 3.141592 como pi o importarlo del módulo math
"""

import math

def area_circulo(r):
    return r**2 * math.pi

print(area_circulo(5))
