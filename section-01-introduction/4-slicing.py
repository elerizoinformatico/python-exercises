"""
Al realizar una consulta en un registro hemos obtenido una cadena de texto al revés.
Al parecer contiene el nombre de un alumno, la nota de un exámen y la materia.

Realiza lo siguiente:
- Voltea la cadena y guárdala en una variable llamada cadena_volteada.
  Puedes devolver una cadena volteada usando un tercer índice negativo con slicing: cadena[::-1]
- Extrae el nombre y apellido del alumno y almacénalos en una variable llamada nombre.
- Extrae la nota y almacénala en una variable llamada nota.
- Extrae la materia y almacénala en una variable llamada materia.
- Genera exactamente la siguiente estructura formateando las anteriores variables en una cadena
  llamada cadena_formateada donde nombre, nota y materia hacen referencia a las variables extraídas:

{nombre} ha sacado un {nota} en {materia}
Ejemplo:

Ramón García ha sacado un 8.1 en Matemáticas
"""

# Variables disponibles
cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

# Invertimos la cadena corrupta
cadena_volteada = cadena_corrupta[::-1]

# Extraemos el nombre, nota y materia con slicing
nombre = cadena_volteada[:12]
nota = cadena_volteada[13:16]
materia = cadena_volteada[17:]

# A partir de las variables extraídas generamos la cadena formateada
cadena_formateada = nombre + " ha sacado un " + nota + " en " + materia
print(cadena_formateada)
