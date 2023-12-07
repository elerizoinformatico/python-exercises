# Al realizar una consulta en un registro hemos obtenido una cadena de texto al revés.
# Esta cadena contiene el nombre de un alumno y la nota de un examen.
# Debemos formatear la cadena para conseguir la siguiente estructura:
# Nombre Apellido ha sacado un Nota de nota.

# Ayuda: Para voltear una cadena rápidamente utilizando slicing usamos un tercer índice cad[::-1]

cadena = "zeréP nauJ,01"

cadena_invertida = cadena[::-1]

nota = cadena_invertida[:2]
nombre_apellido = cadena_invertida[3:]
print(nombre_apellido, "ha sacado un", nota, "de nota")
