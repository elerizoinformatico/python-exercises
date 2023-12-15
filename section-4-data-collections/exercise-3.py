"""
Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas
se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad)

Debes crear una estructura de tipo cola con todas las tareas ordenadas pero sin los números de orden.

Pista: para poder ordenar automáticamente una lista es posible utilizar el método sort()
"""

tareas = [
    [6,"Distribución"],
    [2,"Diseño"],
    [1,"Concepción"],
    [7,"Mantenimiento"],
    [4,"Producción"],
    [3,"Planificación"],
    [5,"Pruebas"]
]

print("*** Tareas desordenadas ***")
for tarea in tareas:
    print(tarea[0], tarea[1])

from collections import deque

# Ordenamos la lista
tareas.sort()

# Creamos una cola vacía
cola = deque()

# Agregamos a la cola las tareas
for tarea in tareas:
    cola.append(tarea[1])

# Mostramos la cola ordenada
print("\n*** Tareas ordenadas ***")
for tarea in cola:
    print(tarea)
