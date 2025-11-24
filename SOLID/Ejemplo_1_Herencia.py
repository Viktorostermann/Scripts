# Ejercicio 1: Herencia Multi-nivel

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        pass

class Conejo(Animal):
    def hacer_sonido(self):
        return "Squeak"
mi_conejo = Conejo("Bunny")
#print(f"{mi_conejo.nombre} dice: {mi_conejo.hacer_sonido()}")


# Ejericio 2: Herencia múltiple
class Vehiculo:
    def __init__(self, marca, modelo): # Constructor de la clase Vehiculo, la instruccion __init__ se utiliza para inicializar los atributos de la clase.
        self.marca = marca
        self.modelo = modelo
    def conducir(self):
        return "Run , run"


'''class Persona(Vehiculo, Animal):
    def __init__(self, nombre, marca, modelo):
        Animal.__init__(self, nombre)  # Inicializamos el atributo nombre de la clase Animal1
        Vehiculo.__init__(self, marca, modelo)  # Inicializamos los atributos marca y modelo de la clase Vehiculo
    def presentarse(self):
        return f"Hola, soy {self.nombre} y conduzco un {self.marca} {self.modelo}"

persona1 = Persona("Carlos", "Toyota", "Corolla")
print(persona1.presentarse())
print(persona1.conducir())'''

# _________________________________________________________________________

# Clases compuestas (Composicion)

class Persona:
    def __init__(self, nombre, vehiculo):
        self.nombre = nombre
        self.vehiculo = vehiculo

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo un {self.vehiculo.marca} {self.vehiculo.modelo}"

vehiculo1= Vehiculo("Honda", "Civic")
persona2 = Persona("Victor", vehiculo1)

print(persona2.presentarse())
print(persona2.vehiculo.conducir())