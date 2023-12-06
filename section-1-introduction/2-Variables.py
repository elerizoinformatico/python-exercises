"""
Un profesor quiere calcular la nota final de sus alumnos en base a dos exámenes y está desarrollando un algoritmo,
el problema es que los exámenes cuentan diferente y no sabe cómo acabar el programa:

- El primer examen nota_1 cuenta un 40% de la nota final.
- El segundo examen nota_2 cuenta un 60% de la nota final.

Ayudar al profesor a conseguir correctamente la nota final.
"""

# Almacenamos la primera nota
nota_1 = 10
# Almacenamos la segunda nota
nota_2 = 6
# Calculamos la nota final multiplicando cada nota por el porcentaje que vale y sumando los resultados
nota_final = (nota_1*0.4 + nota_2*0.6)
 
print(nota_final)
