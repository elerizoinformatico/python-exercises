"""
Tomando la solución del ejercicio anterior, en lugar de devolver None al dividir entre cero, debes capturar
una excepción que muestre por pantalla EXACTAMENTE el siguiente mensaje si falla el código:

"No se puede dividir entre cero"
"""

# Función actual
def dividir(a, b):
    if b != 0:
        return a/b
    else:
        return None

# Función agregando try/except
def dividir(a, b):
    try:
        return a/b
    except:
        print("No se puede dividir entre cero")
