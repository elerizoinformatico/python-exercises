"""
A partir del ejemplo anterior, extiende la clase Vehiculo y realiza la siguiente implementación:

Vehiculo:
- Color
- Ruedas

Coche(Vehiculo):
- Velocidad (km/h)
- Cilindrada (cc)

Bicicleta(Vehiculo):
- Tipo (urbana/deportiva)

Camioneta(Coche):
- Carga (kg)

Motocicleta(Bicicleta):
- Velocidad (km/h)
- Cilindrada (cc)

Experimenta:
- Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
- Realiza una función catalogar() que reciba la lista de vehiculos y muestre el nombre de su clase y sus atributos.
- Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los
  que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje
  
  "Se han encontrado {} vehiculos con {} ruedas"
  
  Únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"color {self.color}, {self.ruedas} ruedas"
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", {self.velocidad} km/h, {self.cilindrada} cc"

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f", {self.carga} kg de carga"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", {self.velocidad} km/h, {self.cilindrada} cc"

vehiculos = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

def catalogar(lista):
    for v in lista:
        print(f"{type(v).__name__} {v}")

catalogar(vehiculos)

def catalogar2(lista, ruedas=None):
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador += 1
        print(f"Se han encontrado {contador} vehiculos con {ruedas} ruedas:\n")

    for v in lista:
        if ruedas == None:
            print(f"{type(v).__name__} {v}")
        else:
            if v.ruedas == ruedas:
                print(f"{type(v).__name__} {v}")

catalogar2(vehiculos, 0)
catalogar2(vehiculos, 2)
catalogar2(vehiculos, 4)
