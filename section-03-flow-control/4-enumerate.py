"""
Modificar las cadenas de la lista por la letra inicial de cada cadena en la lista utilizando,
si lo requieres, la función enumerate.

Supongamos que iniciales tiene ["Hola", "Mundo"], el objetivo es transformar esos valores a ["H", "M"]

Notas:
Recuerda que para modificar los valores en una lista necesitas hacerlo mediante el índice de cada elemento:
"""

from evaluate import iniciales

for i,cadena in enumerate(iniciales):
    iniciales[i] = iniciales[i][0]

print(iniciales)
