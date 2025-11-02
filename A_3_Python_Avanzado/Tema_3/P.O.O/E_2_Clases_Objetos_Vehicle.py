

class Coche():
    def __init__(self, marca, modelo, anio):
         '''Inicializa los atributos del coche'''
         self.marca = marca
         self.modelo = modelo
         self.anio = anio
         self.contador_kilometros = 0

    def crear_descripcion(self):
        '''Devuelve una descripcion formateada del coche'''
        descripcion = f"Mark: {self.marca} / Model: {self.modelo} / Year: {self.anio} "
        return descripcion.title()

    def leer_kilometros(self):
        '''Muestra o Imprime el valor del contador de kilometros'''
        print(f"Este coche tiene {self.contador_kilometros} kilometros recorridos.")

    def actualizar_kilometros(self, kilometros):
        '''Establece el valor del contador de kilometros'''
        self.contador_kilometros = kilometros
        if kilometros >= self.contador_kilometros:
            self.contador_kilometros = kilometros
        else:
            print("No puedes reducir el valor de los kilometros.")

print("")
mi_coche = Coche("Toyota", "Corolla", 2020)   # Instancia de la clase Coche
print(mi_coche.crear_descripcion())           # Muestro la descripcion del coche
print("")

mi_coche.actualizar_kilometros(15000)  # Intento de aumentar los kilometros
mi_coche.leer_kilometros()             # Muestro los kilometros actuales
print("")

mi_coche.actualizar_kilometros(12000)  # Intento de reducir los kilometros
mi_coche.leer_kilometros()             # Muestro los kilometros actuales
print("")

''' Creamos la Sub_Clase ElectricCar que hereda de la Super_Clase Coche '''
class ElectricCoche(Coche):
    def __init__(self, marca, modelo, anio):
        super().__init__(marca, modelo, anio)

''' Creamos la Clase Bateria_Litio que hereda de la Super_Clase Bateria '''    
def Baterias(self, Bat_Litio, Bat_Plom):
    def __init__(self, capacidad_bateria=75):
        '''Inicializa los atributos de la bateria'''
        self.capacidad_bateria = capacidad_bateria

class Bat_Litio():
    def __init__(self, capacidad_bateria=75):
        '''Inicializa los atributos de la bateria'''
        self.capacidad_bateria = capacidad_bateria

    def descripcion_bateria(self):
        '''Muestra la descripcion de la bateria'''
        print(f"Este coche tiene una bateria de {self.capacidad_bateria} kWh.")