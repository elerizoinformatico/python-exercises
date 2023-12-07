"""
Utilizando una condición if-elif-else debes realizar un programa que compare la longitud de dos variables (cadena_1 y cadena_2)
y en función del resultado almacene un valor en otra variable llamada resultado:
- Si cadena_1 es más larga que cadena_2 la variable resultado deberá tener el valor entero 1.
- Si cadena_1 es más corta que cadena_2 la variable resultado deberá tener el valor entero 2.
- Si cadena_1 tiene la misma longitud que cadena_2 la variable resultado deberá tener el valor entero 0.
"""

# Variables del ejercicio
from evaluate import cadena_1, cadena_2

l1 = len(cadena_1)
l2 = len(cadena_2)

if l1 > l2:
    resultado = 1
elif l1 < l2:
    resultado = 2
else:
    resultado = 0
