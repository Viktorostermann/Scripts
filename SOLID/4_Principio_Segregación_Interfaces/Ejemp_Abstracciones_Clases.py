# ABC -> Abstract methods and classes

# Clase informal

class Mando: 
    def siguiente_canal(self): 
        pass 
    def anterior_canal(self): 
        pass 
    def volumen_up(self): 
        pass 
    def volumen_down(self): 
        pass

# Clase que implementa la interfaz mando 
class MandoLG(Mando): 
    def siguiente_canal(self):
        print("LG-> Siguiente canal")
    def anterior_canal(self):
        print("LG-> Anterior canal")
    def volumen_up(self):
        print("LG-> Subir volumen")
    def volumen_down(self):
        print("LG-> Bajar volumen")

''' Interfas formal de las clases abstractas de Mando no pueden ser usadas directamente porque son 
clases abstractas, sin embargo las clases que hereden de Mando deben implementar todos sus métodos 
abstractos de la clase abstracta Mando. En caso de que una clase hija no implemente todos los métodos 
abstractos de la clase padre Mando, se generará un error en tiempo de ejecución.'''

# Ejemplo de clase abstracta
from abc import ABC, abstractmethod
from abc import ABCMeta

class Mando(metaclass=ABCMeta):
    @abstractmethod
    def siguiente_canal(self):
        pass
    @abstractmethod
    def anterior_canal(self):
        pass
    @abstractmethod
    def volumen_up(self):
        pass
    @abstractmethod
    def volumen_down(self):
        pass

class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung -> Siguiente Canal")
    def anterior_canal(self):
        print("Samsung -> Anterior Canal")
    def volumen_up(self):
        print("Samsung -> Subir Volumen")
    def volumen_down(self):
        print("Samsung -> Bajar Volumen")
