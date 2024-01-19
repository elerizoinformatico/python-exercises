"""
Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres argumentos:
- El primero es el número a recortar
- El segundo es el límite inferior
- El tercero el límite superior.

La función tendrá que cumplir lo siguiente:
- Devolver el límite inferior si el número es menor que éste
- Devolver el límite superior si el número es mayor que éste.
- Devolver el número sin cambios si no se supera ningún límite.

Notas:
- Única y exclusivamente tienes que programar la función, no debe haber ningún otro código en el ejercicio.
- No utilices la sentencia match-case, ya que el ejercicio está validando con Python 3.8.
"""

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero
