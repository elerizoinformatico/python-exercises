"""
Realiza una función llamada par_o_impar(numero) que imprima por pantalla PAR o IMPAR (todo en mayúsculas)
dependiendo de si numero es par o impar.

Notas:
- Se debe imprimir única y exclusivamente PAR o IMPAR o la comprobación de la solución fallará.
- Única y exclusivamente tienes que programar la función, no debe haber ningún otro código en el ejercicio.
"""

def par_o_impar(numero):
    if numero % 2 == 0:
        print("PAR")
    else:
        print("IMPAR")
