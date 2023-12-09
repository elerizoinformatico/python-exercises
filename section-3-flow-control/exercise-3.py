"""
Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100.
"""

# Primera forma de resolverlo

num = 0
sum = 0
while num <= 100:
  sum += num
  num += 2

print("La suma de los 100 primeros números pares es",sum)

# Segunda forma de resolverlo

suma = sum(range(0,101,2))
print(suma)
