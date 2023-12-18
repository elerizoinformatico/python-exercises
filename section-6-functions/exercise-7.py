"""
Realiza una función factores_primos() que reciba un número entero y despliegue sus factores primos.

Por ejemplo:
factores_primos(10) [2,5]
factores_primos(20) [2,2,5]
"""

def factores_primos(numero):
    factores = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            factores.append(divisor)
            numero = numero // divisor
        else:
            divisor += 1
    return factores

# Probamos la función con los números 20 y 36
print(factores_primos(20))
print(factores_primos(36))
