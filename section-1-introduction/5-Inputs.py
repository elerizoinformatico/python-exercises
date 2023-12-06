"""
Realiza un programa con los siguientes requisitos:

- Leer por teclado dos cadenas de caracteres, una llamada nombre y otra llamada apellido.
- Leer por teclado un número entero llamado edad (recuerda que la variable debe ser de tipo entero).
- Leer por teclado un número flotante llamado numero_magico.
- Finalmente debes crear una variable cadena_final con el siguiente formato:

NOMBRE APELLIDO: Tu número de la suerte es el EDAD*NUMERO_MAGICO

Por ejemplo: "Juan", "Pérez", 20 y 4.5, cadena_final contendrá lo siguiente:

Juan Pérez: Tu número de la suerte es el 90.0
"""

# leemos el nombre y el apellido
nombre = input()
apellido = input()

# Leemos la edad y la transformamos a entero
edad = int(input())

# Leemos el número mágico y lo transformamos a flotante
numero_magico = float(input())

cadena_final = nombre + " " + apellido + ": Tu número de la suerte es el " + str(edad * numero_magico)
