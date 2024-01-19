"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución.
"""

resultado = 10/0
# ZeroDivisionError
# ZeroDivisionError: division by zero

# Añadiendo un try-except tenemos
try:
    resultado = 10/0
    print(resultado)
except ZeroDivisionError:
    print("¡Error! No es posible dividir por cero")
