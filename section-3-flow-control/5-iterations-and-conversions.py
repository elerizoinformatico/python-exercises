"""
Pide al usuario que introduzca un número entero por teclado entre 1 y 9 (ambos incluidos)
y guárdalo en la variable numero. Debes asegurarte de que esa variable numero contiene un
numero entero del 1 al 9, utiliza un bucle para repetir hasta que se cumpla la condición.

Genera una lista de nombre multiplos que contenga los múltiplos de numero en el rango 1 a
100 (ambos incluidos) utilizando la conversión de un range a list con un paso:

list(range(Min,Max,Paso)).
"""

multiplos = []

numero = int(input("Ingresa un número entre 1 y 9: "))

while (numero < 1 or numero > 9):
    numero = int(input("Ingresa un número entre 1 y 9: "))

multiplos = list(range(numero,101,numero))
print(multiplos)
