# Realiza un programa que cumpla el siguiente algoritmo:
# Guarde en una variable numero_magico el valor 12345679
# Lea por pantalla otro numero_usuario, espeficica que sea entre 1 y 9
# Multiplica el numero_usuario por 9 en sí mismo
# Multiplica el numero_magico por el numero_usuario en sí mismo
# Muestra el valor final del numero_magico por pantalla

numero_magico = 12345679
numero_usuario = int(input("Ingresa un número del 1 al 9: "))
numero_usuario *= 9
numero_magico *= numero_usuario
print("El número mágico es", numero_magico)
