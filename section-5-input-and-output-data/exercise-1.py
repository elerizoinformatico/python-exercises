"""
Formatea los siguientes valores para mostrar el resultado indicado
- "Hola mundo", alineado a la derecha en 20 caracteres
- "Hola mundo", truncamiento en el cuarto caracter (índice 3)
- "Hola mundo", alineamiento al centro en 20 caracteres con truncamiento en el segundo caracter (índice 1)
- 150, formateo a 5 números enteros rellenados con ceros
- 7887, formateo a 7 números enteros rellenados con espacios
- 20.02, formateo a 3 números enteros y 3 números decimales
"""

print("{:>20}".format("Hola mundo"))
print("{:.3}".format("Hola mundo"))
print("{:^20.1}".format("Hola mundo"))
print("{:05d}".format(150))
print("{:7d}".format(7887))
print("{:07.3f}".format(20.02))
