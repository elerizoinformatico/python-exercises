"""
Crea una clase Persona con los atributos nombre y edad. Además, hay que crear un método cumpleaños,
que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con Persona.
"""

class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        return f"{self.nombre} de {self.edad} años"

    def cumpleaños(self):
        self.edad += 1

p = Persona("Cristina",25)
p.mostrar() # 'Cristina de 25 años'
p.cumpleaños()
p.cumpleaños()
p.mostrar() # 'Cristina de 27 años'
