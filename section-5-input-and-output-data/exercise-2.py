"""
Crear un script llamado tabla.py que realice las siguientes tareas:
- Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
- El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
- En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
- El script contendrá un bucle for que itere el número de veces del primer argumento.
- Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
- Dentro del segundo for ejecuta una instrucción print("*",end=''). (end=" evita el salto de línea)
- Ejecuta el código y observa el resultado.

Ahora intenta deducir donde y cómo añadir otra instrucción print para dibujar una tabla.
"""

import sys

if len(sys.argv) == 3: # Verificamos que se reciban ambos argumentos
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9: # Verificamos que el rango de filas y columnas sea entre 1 y 9
        print("Filas o columnas incorrectas")
        print("Ejemplo: tabla.py [1-9] [1-9]")
    else:
        # A partir de aquí empieza la lógica del script
        for f in range(filas):
            print("")
            for c in range(columnas):
                print("* ",end='')
            print("")
else: # Desplegamos un mensaje de cómo utilizar el script en caso de no ingresar uno o ambos números
    print("Error, argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9] [1-9]")
