# Utilizando operadores lógicos determina si una cadena de texto introducida por el usuario
# tiene una longitud mayor o igual que 3 y a su vez es menor que 10

cadena = input("Ingresa una cadena de texto: ")
condiciones = (len(cadena) >= 3) and (len(cadena) < 10)
print("¿La longitud de la cadena es mayor o igual que 3 y menor que 10?", condiciones)
