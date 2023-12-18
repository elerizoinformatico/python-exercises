"""
Crea un script llamado descomposición.py que realice las siguientes tareas:
- Debe tomar un argumento que será un número entero positivo.
- En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

El objetivo del script es descomponer el número en unidades, decenas, centenas, etc. Por ejemplo:
> 3647
El programa deberá devolver una descomposición línea a línea como la siguiente utilizando formateo:
> 0007
> 0040
> 0600
> 3000

Pista: Que el valor sea un número no significa necesariamente que deba serlo para formatearlo.
"""

import sys

if len(sys.argv) == 2: # Verificamos que se reciba el argumento
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999: # Verificamos que el número no sea negativo o superior a 9999
        print("El número es incorrecto")
        print("Ejemplo: descomposición.py [0-9999]")
    else:
        # Aquí empieza la lógica del script
        cadena = str(numero)
        longitud = len(cadena)
        for i in range(longitud):
            print("{:04d}".format(int(cadena[longitud-1-i])*10**i))
else: # Desplegamos un mensaje de cómo utilizar el script en caso de no ingresar un número
    print("Error, argumento incorrecto")
    print("Ejemplo: descomposición.py [0-9999]")
