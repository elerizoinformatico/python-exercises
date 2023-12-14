"""
Realizar las siguientes instrucciones de forma ordenada sobre la variable animales:
- Añade al diccionario las claves perro, gato y rana con sus respectivos valores dog, cat y frog.
- Modifica las claves caballo y vaca con los valores horse y cow respectivamente.
- Por último elimina del diccionario las claves rana y vaca.
"""

animales = {"caballo":"", "vaca":""}

# Añadimos los elementos al diccionario
animales = {"perro":"dog", "gato":"cat", "rana":"frog"}

# Otra forma de añadir elementos al diccionario
# animales["perro"] = "dog"
# animales["gato"] = "cat"
# animales["rana"] = "frog"

# Modificamos los valores de las claves caballo y vaca
animales["caballo"] = "horse"
animales["vaca"] = "cow"

# Eliminamos del diccionario las claves rana y vaca
del(animales["rana"])
del(animales["vaca"])
