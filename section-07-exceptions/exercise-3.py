"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución.
"""

colores = {"rojo": "red", "verde": "green", "negro": "black"}
print(colores["blanco"]) # KeyError: 'blanco'

# Añadimos la sentencia try-except
try:
    print(colores["blanco"])
except KeyError:
    print("¡Error! La clave del diccionario no se encuentra")
    print("Prueba con alguna que exista: {rojo, verde, negro}")
