"""
Realiza un programa que pida al usuario un número entero del 0 al 9 y que,
mientras el número no sea correcto repita el proceso. Luego debe comprobar
si el número se encuentra en la lista de números y notificarlo.

Consejo: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).
"""

numeros = [1, 3, 6, 9]

while True:
    num = int(input("Introduce un número entre 0 y 9: "))
    if num >= 0 and num <= 9:
        break

if num in numeros:
    print("El numero",num,"SI se encuentra en la lista",numeros)
else:
    print("El numero",num,"NO se encuentra en la lista",numeros)
