"""
Realizar las siguientes instrucciones de forma ordenada sobre la variable grupo:

- Añade los siguientes usuarios: Ana, Ramón, Marta, Eric y David (respeta las tildes).
- Elimina a los usuarios Mario, Miguel y Ramón.
- Optativo: Cuando tu solución valide, intenta optimizarlo utilizando listas y bucles.

(*) Para eliminar un registro de un conjunto puedes utilizar su método interno conjunto.remove("registro").
"""

grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

grupo.add("Ana")
grupo.add("Ramón")
grupo.add("Marta")
grupo.add("Eric")
grupo.add("David")
grupo.remove("Mario")
grupo.remove("Miguel")
grupo.remove("Ramón")

# Utilizando sentencias iterativas

lista1 = ["Ana", "Ramón", "Marta", "Eric", "David"]
lista2 = ["Mario", "Miguel", "Ramón"]

for usuario in lista1:
    grupo.add(usuario)
 
for usuario in lista2:
    grupo.remove(usuario)
