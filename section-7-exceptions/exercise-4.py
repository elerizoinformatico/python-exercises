"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución.
"""

resultado = "20" + 15
print(resultado) # TypeError: can only concatenate str (not "int") to str

# Añadimos la sentencia try-except
try:
    resultado = "20" + 15
except TypeError:
    print("¡Error! Solo es posible sumar datos del mismo tipo")
    print("Debes transformar la cadena a entero o el entero a cadena")
