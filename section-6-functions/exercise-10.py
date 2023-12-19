"""
Definir una función llamada es_palindromo() que reconoce palíndromos, es decir,
palabra que tienen el mismo aspecto escritas invertidas.

Ejemplo: es_palindromo("radar") tendría que devolver True.
"""

# Generamos una función que invierta cualquier cadena
def invertir_cadena(cadena):
    return cadena[::-1]

# Aunque utilizando slicing podemos invertir una cadena fácilmente, aquí te muestro como hacerlo manual
def invertir_cadena_manual(cadena):
    cadena_invertida = ""
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

def es_palindromo(cadena):
    c = 0
    cadena_invertida = invertir_cadena(cadena)
    for i,n in enumerate(cadena):
        if cadena[i] == cadena_invertida[i]:
            c += 1
        else:
            return False
    if c == len(cadena):
        return True

print(es_palindromo("radar")) # True
print(es_palindromo("ana")) # True
print(es_palindromo("hola")) # False
print(es_palindromo("amigo")) # False
print(es_palindromo("123321")) # True
