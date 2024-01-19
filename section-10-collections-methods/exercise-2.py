"""
Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
- Borrar los elementos duplicados
- Ordenar la lista de mayor a menor
- Eliminar todos los números impares
- Realizar una suma de todos los números que quedan
- Añadir como primer elemento de la lista la suma realizada
- Devolver la lista modificada
- Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:

nueva_lista = modificar(lista)
print(nueva_lista[0] == sum(nueva_lista[1:])) # True
"""

lista = [29, -5, 12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
    l = list(set(l)) # Convertimos a conjunto para eliminar duplicados y luego la volvemos a convertir en lista
    l.sort(reverse=True) # Ordenamos de forma descendente (mayor a menor)
    l_temp = [] # Lista temporal que contendrá sólo los números pares
    for n in l:
        if n%2 == 0:
            l_temp.append(n)
    suma = sum(l_temp) # Realizamos una suma de todos los elementos que quedan
    l_temp.insert(0,suma) # Añadimos la suma al principio de la lista
    return l_temp # Retornamos la lista modificada

nueva_lista = modificar(lista)

print(lista)
print(nueva_lista)

print(nueva_lista[0] == sum(nueva_lista[1:]))
