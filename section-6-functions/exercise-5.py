"""
Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar,
el segundo es el límite inferior y el tercero el límite superior.

La función tendrá que cumplir lo siguiente:
- Devolver el límite inferior si el número es menor que este.
- Devolver el límite superior si el número es mayor que este.
- Devolver el número sin cambios si no se supera ningún limite.

Comprueba el resultado de recortar 15 entre los números 0 y 10.
"""

def recortar(numero,minimo,maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero

print(recortar(15,0,10))
