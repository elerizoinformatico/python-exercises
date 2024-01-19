"""
Realiza un programa que pida al usuario cuántos números quiere introducir.
Luego lea los números y realice una media aritmética.
"""

n = int(input("¿Cuántos números quieres introducir?: "))
i = 0
suma = 0
while i < n:
    num = float(input("Ingresa un número: "))
    suma += num
    i += 1
print("La media es:",suma/n)

# Otra forma de resolverlo
n = int(input("¿Cuántos números quieres introducir?: "))
suma = 0
for i in range(n):
    suma += float(input("Introduce un número: "))
print("La media es:",suma/n)
