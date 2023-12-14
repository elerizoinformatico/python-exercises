"""
Realizar las siguientes instrucciones de forma ordenada sobre la variable animales:
- Añade al diccionario las claves perro, gato y rana con sus respectivos valores dog, cat y frog.
- Modifica las claves caballo y vaca con los valores horse y cow respectivamente.
- Por último elimina del diccionario las claves rana y vaca.
"""

animales = {"caballo":"", "vaca":""}

animales = {"perro":"dog", "gato":"cat", "rana":"frog"}

animales["caballo"] = "horse"
animales["vaca"] = "cow"

del(animales["rana"])
del(animales["vaca"])
