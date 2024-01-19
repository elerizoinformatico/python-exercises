"""
Realiza una función contar_digitos() que reciba un número entero y determine la cantidad de dígitos.
Comprueba el resultado al ingresar los números 123, 7881 y 0.
"""

def contar_digitos(numero):
    c = 0
    if numero == 0:
        return 1
    while numero != 0:
        numero //= 10
        c += 1
    return c

print(contar_digitos(123))
print(contar_digitos(7881))
print(contar_digitos(0))

# Otra forma de resolver el mismo problema
def contar_digitos(numero):
    return len(str(numero))

print(contar_digitos(123))
print(contar_digitos(7881))
print(contar_digitos(0))
