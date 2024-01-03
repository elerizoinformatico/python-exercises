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
