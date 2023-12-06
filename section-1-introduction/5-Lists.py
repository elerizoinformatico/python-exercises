"""
Dadas dos listas lista1 y lista2 debes realizar diferentes tareas por el orden indicado:

- Añade a la lista1 el número 1234 y luego el texto Hola.
- Añade a la lista2 el texto Adiós y luego el número 1234.
- Genera una lista3 con todos los elementos de la lista1 excepto el último.
- Genera una lista4 con todos los elementos de la lista2 excepto el primero y el último.
- Genera una lista5 con los elementos de la lista4 más la lista3.
- Los nombres de las variables deben ser los que se especifican o el ejercicio no validará.
"""

lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

# Añadimos los elementos a la primera lista
lista1.append(1234)
lista1.append("Hola")

# Añadimos los elementos a la segunda lista
lista2.append("Adiós")
lista2.append(1234)

# Generamos la tercera lista con los elementos de la primera y luego eliminamos el último
lista3 = lista1
lista3[-1:] = []

# Generamos la cuarta lista con los elementos de la segunda y luego eliminamos el primero y el último
lista4 = lista2
lista4 = lista2[1:-1]

# Generamos la quinta lista sumando la cuarta y la tercera
lista5 = lista4 + lista3
