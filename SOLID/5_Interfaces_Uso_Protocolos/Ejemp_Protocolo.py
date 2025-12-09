# Definicion de un protocolo; Es una interfaz informal, 
# que define un conjunto de reglas que deben cumplir los 
# objetos que lo implementen, sin necesidad de heredar de una clase base.
# Un protocolo se define mediante la creacion de una clase que contiene 
# metodos abstractos que deben ser implementados por las clases que 
# implementen el protocolo.
# Los protocolos son usados para definir un contrato entre clases, 
# permitiendo que las clases que implementen el protocolo cumplan con ese contrato.

''' Un protocolo es un conjutno de metodos y/o atributos
que un objeto debe tener para ser considerado compatible con ese protocolo.
Los protocolos le permiten definir interfaces informales, quiere decir,
sin necesidad de crear explicitamente una clase o heredar de una clase base especifica.'''

# Beneficios de segregacion de interfaces con Protocolos:

# 1. Flexibilidad: Permiten definir interfaces informales,
# 2. Reutilizacion de codigo: Facilitan la reutilizacion de codigo
# 3. Mantenibilidad: Facilitan el mantenimiento del codigo
# 4. Compatibilidad: Facilitan la compatibilidad entre diferentes clases y modulos

# Nota: Para el uso de interfaces se recomienda usar la letra "I" al inicio del nombre de la interfaz o Clase


# Ejemplo de uso de Clases Abstractas vs Interfaces (Protocolos)
class HumanWorker:
    def work(self):
        print("Humano esta Trabajando...")

    def eat(self):
        print("Humano esta Comiendo...")

class RobotWorker:
    def work(self):
        print("Robot esta Trabajando...")

    def eat(self):
        raise NotImplementedError("Los Robots no Comen")