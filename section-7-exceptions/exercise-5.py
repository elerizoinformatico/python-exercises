"""
Realiza una función llamada agregar_una_vez() que reciba una lista y un elemento. La función debe
añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además, si
este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes
capturar y mostrar este mensaje en su lugar

Error: imposible añadir elementos duplicados -> [elemento]

Prueba agregando los elementos 10, -2, "Hola" a la lista con la función y muestra su contenido.
"""

elementos = [1, 5, -2]

def agregar_una_vez(lista, e):
    try:
        if e in lista:
            raise ValueError
        else:
            lista.append(e)
    except ValueError:
        print(f"Error: imposible añadir elementos duplicados -> {e}")

elementos = [1, 5, -2]

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")
print(elementos) # [1, 5, -2, 10, 'Hola']
