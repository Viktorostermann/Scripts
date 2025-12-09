'''Tecnicas de Inyeccion de Dependencias aplicando Inyeccion de Constructores.
La inyeccion de dependencias es una tecnica de diseño de software que permite separar las
dependencias de una clase de su implementación, facilitando la mantenibilidad y escalabilidad del
código. Una de las formas más comunes de implementar la inyección de dependencias es a través de
la inyección de constructores, donde las dependencias se pasan como parámetros al constructor de la clase.
Este principio establece que una clase debe tener una, y solo una, razón para cambiar. 
Y que las clases deben estar desacopladas entre si. '''

#Ejemplo de inyeccion de dependencias a traves de Setters con dependencia de class o abstraccion del Notificador

from abc import ABC, abstractmethod
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

class EmailNotificador(Notificador):
    def enviar(self, mensaje: str):
        print(f"Enviando email con el mensaje: {mensaje}")

# ________________________________________________________________________________________________

#Ejemplo de inyeccion de dependencias a traves de setters
class App:
    def enviar_notificacion(self, notificador: Notificador, mensaje: str):
        notificador.enviar(mensaje)
        print("Notificacion enviada correctamente")

# Ejemplo de uso
app = App()
notificador = EmailNotificador()
app.enviar_notificacion(notificador, "Hola Mundito!") 

