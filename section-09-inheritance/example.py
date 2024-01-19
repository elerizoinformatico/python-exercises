"""
En este ejercicio trabajaremos el concepto de herencia a profundidad con un problema.
"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas"
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color {self.color}, {self.velocidad} Km/h, {self.ruedas} ruedas, {self.cilindrada} CC"
    
c = Coche("Azul", 4, 150, 1200)
print(c)

"""
El inconveniente más evidente de ir sobreescribiendo es que tenemos que volver a escribir el código de la superclase
y luego el específico de la subclase. Para evitar escribir código innecesario, podemos utilizar un truco que consiste
en llamar al método de la superclase y luego simplemente escribir el código de la clase.
"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas"
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        # Llamamos al método de la superclase par evitar reescribir el mismo código
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + f", {self.velocidad} Km/h, {self.cilindrada} CC"
        # Llamamos al método de la superclase par evitar reescribir el mismo código
    
c = Coche("Azul", 4, 150, 1200)
print(c)

"""
Como tener que determinar constantemente la superclase puede ser fastidioso, Python nos permite utilizar un acceso
directo mucho más cómodo llamado super(). Hacerlo de esta forma además nos permite llamar cómodamente los métodos o
atributos de la superclase sin la necesidad de especificar el self.
"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas"
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas) # Utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", {self.velocidad} Km/h, {self.cilindrada} CC"
    
c = Coche("Azul", 4, 150, 1200)
print(c)
