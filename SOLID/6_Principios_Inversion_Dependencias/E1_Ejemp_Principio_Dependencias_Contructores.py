'''Tecnicas de Inyeccion de Dependencias aplicando Inyeccion de Constructores.
La inyeccion de dependencias es una tecnica de diseño de software que permite separar las
dependencias de una clase de su implementación, facilitando la mantenibilidad y escalabilidad del
código. Una de las formas más comunes de implementar la inyección de dependencias es a través de
la inyección de constructores, donde las dependencias se pasan como parámetros al constructor de la clase.
Este principio establece que una clase debe tener una, y solo una, razón para cambiar. 
Y que las clases deben estar desacopladas entre si. '''

#Ejemplo de inyeccion de dependencias a traves del constructor

from abc import ABC, abstractmethod
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

class EmailNotificador(Notificador):
    def enviar(self, mensaje: str):
        print(f"Enviando email con el mensaje: {mensaje}")

# Clase de Alto Nivel que maneja la logica de negocios
class App:
    def __init__(self, notificador: Notificador): #Clase constructora recibe un objeto de tipo Notificador
        self.notificador = notificador

    def enviar_notificacion(self):
        # Lógica de la aplicación
        self.notificador.enviar("Acción realizada en la aplicación.")
        print("Notificación enviada.")

# Ejemplo de uso
notificador = EmailNotificador()
app = App(notificador)
#app.enviar_notificacion("Hola Mundo!")


# ________________________________________________________________________________________________

#Ejemplo de inyeccion de dependencias a traves de setters
class App:
    def __init__(self):
        self.notificador = None

    def set_notificador(self, notificador: Notificador) -> None:
        self.notificador = notificador

    def enviar_notificacion(self, mensaje: str):
        if self.notificador:
            self.notificador.enviar(mensaje)
            print("Notificación enviada.")
        else:
            print("No se ha configurado ningún notificador.")

# Ejemplo de uso
notificador = EmailNotificador()
app = App()
app.set_notificador(notificador)
app.enviar_notificacion("Hola Mundo!")