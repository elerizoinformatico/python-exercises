"""
Realiza un programa que lea 2 números por teclado y permita elegir entre 3 opciones del menú:
- Mostrar una suma de los 2 números.
- Mostrar una resta de los 2 números (el primero menos el segundo)
- Mostrar una multiplicación de los 2 números.
- En caso de no introducir una opción válida, el programa informará que no es correcta.
"""

n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

print("¿Qué quieres hacer?")
print("1. Sumar los dos números")
print("2. Restar los dos números")
print("3. Multiplicar los dos números")
opcion = input("Introduce una opción: ")

if opcion == "1":
  print("La suma de",n1,"+",n2,"=",n1+n2)
elif opcion == "2":
  print("La resta de",n1,"-",n2,"=",n1-n2)
elif opcion == "3":
  print("El producto de",n1,"*",n2,"=",n1*n2)
else:
  print("La opción es incorrecta")
