"""
Realiza un programa que lea un número impar por teclado. Si el usuario no introduce
un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.
"""

n = int(input("Introduce un número impar: "))

while n % 2 == 0:
  print("El número ingresado NO es impar, intenta nuevamente")
  n = int(input("Introduce un número impar: "))

print(n)
