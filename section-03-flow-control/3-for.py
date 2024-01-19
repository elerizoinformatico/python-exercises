"""
En este ejercicio se te facilitará un numero aleatorio que no conoces en la variable numero.
Utilizando lo que conoces sobre los bucles for y la función range() , debes realizar un sumatorio
de todos los números desde 0 hasta ese numero (incluido) exceptuando los múltiples de 5 y 7, y
almacenarlo en la variable sumatorio.

Ejemplo, si numero fuera 7, el sumatorio sería igual a 1+2+3+4+6 = 16.
Recuerda, únicamente debes sumar los números NO múltiples de 5 y 7 al sumatorio.
"""

from evaluate import numero

sumatorio = 0

for i in range(numero+1):
    if (not i % 5 == 0) and (not i % 7 == 0):
        print(i)
        sumatorio += i

print(sumatorio)
