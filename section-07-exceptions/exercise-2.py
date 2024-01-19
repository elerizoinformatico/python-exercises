"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución.
"""

lista = [1, 2, 3, 4, 5]
print(lista[10]) # IndexError: list index out of range

# Añadimos la sentencia try-except
try:
    print(lista[10])
except IndexError:
    print("¡Error! El índice al que intentas acceder se encuentra fuera del rango")
    print("Ejemplo: lista[0-4]")
