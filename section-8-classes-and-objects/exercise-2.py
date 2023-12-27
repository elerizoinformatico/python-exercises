"""
Escribir una clase llamada circulo que contenga un radio y dos métodos:
- Uno que devuelva el área.
- Otro que devuelva el perímetro.
"""

import math

class Circulo:
    def __init__(self, r=0):
        self.r = r
    
    def area(self):
        self.area = math.pi * (self.r)**2
        print(f"El área del círculo es {self.area}")
    
    def perimetro(self):
        self.perimetro = 2 * math.pi * self.r
        print(f"El área del círculo es {self.perimetro}")

c = Circulo(3)
c.area()
c.perimetro()
