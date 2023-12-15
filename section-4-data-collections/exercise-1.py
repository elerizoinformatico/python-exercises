"""
Realiza un programa que siga las siguientes instrucciones:
- Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
- Crea un conjunto llamado administradores con los administradores Juan y Marta
- Borra al administador Juan del conjunto de administradores
- Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios
- Muestra todos los usuarios por pantalla de forma dinámica, indicando si cada usuario es administrador o no

Nota: Los conjuntos se pueden recorrer dinámicamente utilizando un bucle for de forma similar a una lista.
También cuentan con un método llamado discard(elemento) que sirve para borrar un elemento
"""

# Creamos el conjunto usuarios
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

# Creamos el conjunto administradores
administradores = {"Juan", "Marta"}

# Borramos a Juan del conjunto administradores
administradores.discard("Juan")

# Añadimos a Marcos en el conjunto administradores
administradores.add("Marcos")

# Mostramos a todos los usuarios con un buble for, indicando si son administradores o no
for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es admin")
    else:
        print(usuario, "no es admin")
