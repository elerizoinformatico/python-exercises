"""
Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
- Todos los números del 0 al 10.
- Todos los números del -10 al 0.
- Todos los números pares del 0 al 20.
- Todos los números impares entre -20 y 0.
- Todos los números múltiplos de 5 entre 0 y 50.
"""

# Todos los números del 0 al 10
print(list(range(0,11)))

# Todos los números del -10 al 0
print(list(range(-10,1)))

# Todos los números pares del 0 al 20
print(list(range(0,21,2)))

# Todos los números impares entre -20 y 0
print(list(range(-19,0,2)))

# Todos los números múltiplos de 5 entre 0 y 50
print(list(range(0,51,5)))
