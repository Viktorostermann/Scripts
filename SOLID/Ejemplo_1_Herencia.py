# Ejercicio 1: Herencia Multi-nivel

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
        pass

class Conejo(Animal): # Sub Clase o CLase Hija de la clase Animal
    def hacer_sonido(self):
        return "Squeak"
mi_conejo = Conejo("Bunny")
#print(f"{mi_conejo.nombre} dice: {mi_conejo.hacer_sonido()}")

class Leon(Animal): # Sub Clase o CLase Hija de la clase Animal
    def hacer_sonido(self):
        return "Ruge"
mi_leon = Leon("Simba")
#print(f"{mi_leon.nombre} dice: {mi_leon.hacer_sonido()}")


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
    def __init__(self, nombre, vehiculo, mi_leon):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.mi_leon = mi_leon

    def presentarse(self):
        print("")
        return f"Hola, soy {self.nombre} y tengo un {self.vehiculo.marca} {self.vehiculo.modelo} tambien tengo una mascota y se llama {self.mi_leon.nombre} es un león y {self.mi_leon.hacer_sonido()}"

vehiculo1= Vehiculo("Honda", "Civic")
mi_leon = Leon("Simba")
persona2 = Persona("Victor", vehiculo1, mi_leon)

print(persona2.presentarse())
print("")


