# Ordenamiento de CLases con SOLID aplicacndo el pincipio de Responsabilidad Unica y Desacoplamiento.
# Este principio establece que una clase debe tener una, y solo una, razón para cambiar. 
# Y que las clases deben estar desacopladas entre si. 
# Quiere decir que una clase no debe depender de los detalles de otra clase para funcionar, sino de una abstracción
# es decir, una clase debe ser independiente de otras clases para su funcionamiento.
# Esto facilita el mantenimiento y la escalabilidad del código.

# -------------------------------------------------------
class Engine:
    def getRPM(self):
        return 3000  # valor por defecto del motor


# Referencia de codigo Desacoplado:

''' Se puede observar que la clase Vehicle tiene una unica responsabilidad,
ya que maneja solo la logica del vehiculo. La impresion de informacion,
ademas de la persistencia de datos son manejadas por clases separadas. 
Esto cumple con el principio de responsabilidad unica.'''

# ------------------------------------------------------- 
class Vehicle:
    def __init__(self, name, speed, engine):
        self._name = name
        self._speed = speed
        self._engine = engine

    def getName(self):
        return self._name

    def getEngimeRPM(self):
        return self._engine.getRPM()

    def getMaxSpeed(self):
        return self._speed

# -------------------------------------------------------
class VehiclePrinter:
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def printInfo(self):
        print(
            "Vehicle: {}, Max Speed: {}, RPM: {}".format(
                self._vehicle.getName(),
                self._vehicle.getMaxSpeed(),
                self._vehicle.getEngimeRPM(),
            )
        )

# -------------------------------------------------------
class VehiclePersistance:
    def __init__(self, vehicle, db):
        self._vehicle = vehicle
        self._persistance = db
        print("Hey, storing data! in", self._persistance)


# -------------------------------------------------------
if __name__ == "__main__":
    engine = Engine()
    vehicle = Vehicle(name="Car", engine=engine, speed=200)
    persistance = VehiclePersistance(vehicle=vehicle, db="SQL")
    printer = VehiclePrinter(vehicle=vehicle)
    printer.printInfo()
