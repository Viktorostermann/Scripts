# Ordenamiento de CLases con SOLID aplicacndo el pincipio de Responsabilidad Unica con Acoplamiento de Clases.
# EL uso de clases acopladas va en contra del principio de responsabilidad unica, 
# ya que una clase asume multiples responsabilidades y depende de otras clases para cumplir con su funcion.
# Por lo tanto, se recomienda evitar el acoplamiento excesivo entre clases.
# Debido a que una clase debe tener una, y solo una, razón para cambiar.
# Entonces el acoplamiento se refiere a la dependencia entre clases de manera directa.  



class Engine:
    def __init__(self):
        pass

    def getRPM(self):
        return 3000

# Referencia de codigo Acoplado:

''' Se puede observar que la clase Vehicle tiene multiples responsabilidades, 
ya que maneja la logica del motor, la impresion de informacion, 
ademas de la persistencia de dato. Esto viola el principio de responsabilidad unica.'''

# ---------------------------------------------------------------

class Vehicle:
    def __init__(self, name, speed):
        self._name = name
        self._speed = speed
        self._engine = Engine()

    def getName(self):
        return self._name

    def getEngineRPM(self):
        return self._engine.getRPM()

    def getMaxSpeed(self):
        return self._speed

    def printInfo(self):
        print(
            "Vehicle: {}, Max Speed: {}, RMP: {}".format(
                self._name, self._speed, self._engine.getRPM()
            )
        )
# -------------------------------------------------------------

if __name__ == "__main__":
    vehicle = Vehicle("Car", 200)
    vehicle.printInfo()
