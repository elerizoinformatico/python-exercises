"""
Realiza una función ecuacion_cuadratica() que reciba los coeficientes a, b y c de una ecuación
de segundo grado y determine sus soluciones (ya sean reales o complejas).

Ejemplo:
ecuacion_cuadratica(1,2,1) x1 = -1 y x2 = -1
ecuacion_cuadratica(1,2,1) x1 = -1 y x2 = -5
ecuacion_cuadratica(1,0,1) x1 = i y x2 = -i
"""

import math

def ecuacion_cuadratica(a,b,c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        x1 = -b / (2*a)
        x2 = -b / (2*a)
        return x1, x2
    else:
        real = -b / (2*a)
        imag = (math.sqrt(-d)) / (2*a)
        x1 = complex(real,imag)
        x2 = complex(real,-imag)
        return x1, x2

a = int(input("Introduce el valor del coeficiente a: "))
b = int(input("Introduce el valor del coeficiente b: "))
c = int(input("Introduce el valor del coeficiente c: "))
x1, x2 = ecuacion_cuadratica(a,b,c)
print(f"Ecuación: {a}x^2 + {b}x + {c} = 0")
print(f"Soluciones: x1 = {x1} y x2 = {x2}")
