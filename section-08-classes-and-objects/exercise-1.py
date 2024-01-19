"""
Ejercicio:
- Crea una clase llamada Punto con sus dos coordenadas X e Y.
- Crea un método constructor para crear puntos. Completar con 0 si no se recibe una coordenada.
- Sobreescribe el método string para mostrar un punto en formato (X,Y).
- Crea un método cuadrante que indique a qué cuadrante pertenece el punto o si es el origen.
- Crea un método vector que tome otro punto y calcule el vector resultante entre los dos puntos.
- Crea un método distancia que tome otro punto y calcule la distancia entre ellos, y la muestre por pantalla.
- Crea una clase llamada Rectángulo con dos puntos (inicial y final) que formarán su diagonal.
- Crea un método constructor para crear ambos puntos. Completar con dos puntos en el origen por defecto.
- Añade al rectángulo un método base que muestre la base.
- Añade al rectángulo un método altura que muestre la altura.
- Añade al rectángulo un método area que muestre el área.
"""

import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print(f"{self} pertenece al primer cuadrante")
        elif self.x < 0 and self.y > 0:
            print(f"{self} pertenece al segundo cuadrante")
        elif self.x < 0 and self.y < 0:
            print(f"{self} pertenece al tercer cuadrante")
        elif self.x > 0 and self.y > 0:
            print(f"{self} pertenece al cuarto cuadrante")
        else:
            print(f"{self} se encuentra en el origen")

    def vector(self, p):
        print(f"El vector entre {self} y {p} es ({p.x - self.x},{p.y - self.y})")

    def distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print(f"La distancia entre los puntos {self} y {p} es {d}")

class Rectangulo:
    def __init__(self, pIni=Punto(), pFin=Punto()):
        self.pIni = pIni
        self.pFin = pFin
    
    def base(self):
        self.base = abs(self.pFin.x - self.pIni.x)
        print(f"La base del rectángulo es {self.base}")
    
    def altura(self):
        self.altura = abs(self.pFin.y - self.pIni.y)
        print(f"La altura del rectángulo es {self.altura}")

    def area(self):
        self.base = abs(self.pFin.x - self.pIni.x)
        self.altura = abs(self.pFin.y - self.pIni.y)
        self.area = self.base * self.altura
        print(f"El área del rectángulo es {self.area}")

# Crea los puntos A(2,3), B(5,5), C(-3,-1) y D(0,0)
A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto()

# Consulta a qué cuadrante pertenecen los puntos A, B, C y D
A.cuadrante()
B.cuadrante()
C.cuadrante()
D.cuadrante()

# Consulta los vectores AB y BA
A.vector(B)
B.vector(A)

# Consulta la distancia entre los puntos 'A y B' y 'B y A'
A.distancia(B)
B.distancia(A)

# Determina cuál de los 3 puntos A, B y C se encuentra más lejos del origen (0,0)

A.distancia(D)
B.distancia(D) # Este es el punto más alejado del origen
C.distancia(D)

# Crea un rectángulo utilizando los puntos A y B
R = Rectangulo(A,B)

# Consulta la base, altura y área del rectángulo creado
R.base()
R.altura()
R.area()
