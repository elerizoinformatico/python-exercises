"""
En la función del ejercicio hay un fallo potencial, averigua cuando sucede y retorna el valor None en ese caso especial,
en cualquier otro caso devuelve el resultado normal de la función.

Pista: Valor indeterminado.
"""

def dividir(a, b):
    return a/b

# La función anterior se indetermina si b=0, debemos corregir este inconveniente
def dividir(a, b):
    if b != 0:
        return a/b
    else:
        return None
