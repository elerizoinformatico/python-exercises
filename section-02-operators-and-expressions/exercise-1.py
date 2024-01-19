# Escribe un programa que lea 2 números por teclado y determine los siguientes aspectos:
# Si los 2 números son iguales
# Si los 2 números son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero

# Es suficiente con mostrar True o False
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

print("¿Son iguales?", a == b)
print("¿Son Diferentes?", a != b)
print("¿El primero es mayor que el segundo?", a > b)
print("¿El segundo es mayor o igual que el primero?", b >= a)
