'''
Durante la clase de hoy, repasamos los principios SOLID, la Programación Orientada a Objetos (POO). 
Las clases abstractas, las clases estáticas y los métodos abstractos. 
Estos conceptos se abordaron de manera profunda a través de un ejercicio práctico extenso, 
lo que nos ayudó a comprender cada principio de forma clara y aplicada.

Las Clases Abstractas sustituyen en gran medida la implementación de estructuras condicionales en el código.
'''

import math
from abc import ABC, abstractmethod

### Circulo ###
# ---> Formula para calcular area y perimetro de un circulo y declaracion de sus variables:
# area = PI * (radio ** 2)
# perimetro = 2 * PI * radio

### Triangulo ###
# ---> Formula para calcular area y perimetro de un triangulo y declaracion de sus variables:
# area = (base * altura) / 2
# perimetro = base + altura + hipotenusa

### Rectangulo ###
# ---> Formula para calcular area y perimetro de un rectangulo y declaracion de sus variables:
# area = base * altura
# perimetro = 2 * (base + altura)

# Variables globales
PI = 3.1416

# ---> Formula para calcular area y perimetro de un cuadrado y declaracion de sus variables:

# 📌 Variables locales:
# La expresion "lados". Se refiere al valor representado en numeros, para calcular el area y perimetro de una figura geométrica. 
# area = (lados * lados) ó (lados ** 2)
# perimetro = lados * 4

# Declaracion de Variables
Area_total = 0

#---------------------------------------------------------------------------------------------------------------------------

class Calculo_Area:  # Clase abstracta para calcular el area de un cuadrado
    @staticmethod    # Decorador para indicar que el método es estático
    def calculo_cuadrados(lados): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        return lados ** 2         # Se retorna el area del cuadrado    
#---------------------------------------------------------------------------------------------------------------------------

class Calculo_Perimetro:  # Clase abstracta para calcular el perimetro de un cuadrado
    @staticmethod    # Decorador para indicar que el método es estático
    def calculo_cuadrados(lados): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        return lados * 4         # Se retorna el perimetro del cuadrado
#---------------------------------------------------------------------------------------------------------------------------

class Calculo_Circulo:  # Clase abstracta para calcular el area y perimetro de un circulo
    @staticmethod    # Decorador para indicar que el método es estático
    def calculo_circulo(radio): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        return PI * (radio ** 2) # Se retorna el area y perimetro del circulo
#---------------------------------------------------------------------------------------------------------------------------

class Calculo_Triangulo:  # Clase abstracta para calcular el area y perimetro de un triangulo
    @staticmethod    # Decorador para indicar que el método es estático
    def calculo_triangulo(base, altura): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        return (base * altura) / 2 # Se retorna el area y perimetro del triangulo
#---------------------------------------------------------------------------------------------------------------------------

class Calculo_Rectangulo:  # Clase abstracta para calcular el area y perimetro de un rectangulo
    @staticmethod    # Decorador para indicar que el método es estático
    def calculo_rectangulo(base, altura): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        return base * altura # Se retorna el area y perimetro del rectangulo
#---------------------------------------------------------------------------------------------------------------------------

            # Calcular plicacion de pintura y Productos de imprimacion a BARCOS #

# SOLID -> 1. single responsability principle (Principio de responsabilidad única)
class Calculo_Area:                         # Clase para calcular el area de un cuadrado
    @staticmethod                           # Decorador para indicar que el método es estático
    def calculo_cuadrados(MetrosCuadrados): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        return MetrosCuadrados * 10.763     # Se retorna el area del cuadrado (Ejemplo)

class Calculo_Pintura:   # Clase para calcular el perimetro de un cuadrado
    @staticmethod        # Decorador para indicar que el método es estático
    
    def calcular_antifouling(area): # Funcion. El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        return area * 0.22   # Se retorna el perimetro del cuadrado (Ejemplo)

    def calcular_primer(area):
        return area * 0.1106  # Funcion. El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita. Se retorna el primer producto de pintura (Ejemplo)


# Division de clases en base a BARCOS: 

# --> (Open-Closed = Los metodos de los hijos no pueden usar los metodos de los padres o reemplazar los metodos de los padres) 
       # Ejemplo: Un barco siempre sera un BARCO. 

# --> (Liskov Principle = Los metodos de los hijos puede usar o reemplazar los metodos de los padres)
        # Ejemplo: Un barco puede ser un barco, pero tambien
          

# SOLID -> 2. open-closed principle (Principio de abierto-cerrado) Liskov Principle

class BARCO(ABC):  # Clase para calcular el area de un barco
    @abstractmethod # Decorador para indicar que el método es abstracto, 
                    # lo cual impide que se cree una instancia de la clase, se utiliza para indicar que la clase es abstracta o Padre.
                    # La cual da por herencia a sus clases hijos los metodos abstractos de la clase padre.
    def obtener_area(self): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        pass
#---------------------------------------------------------------------------------------------------------------------------

# Hijo 1 de BARCO
class Barco_a_Motor(BARCO):  # Clase para calcular el area de un barco motora
    def __init__(self, valor1, valor2): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        self.valor1 = valor1
        self.valor2 = valor2
            
    
    def obtener_area(self): # Modificar segun los parametros de un barco motora (Ejemplo)
        return self.valor1 * self.valor2 * 0.5 # Se retorna el area del barco motora (Ejemplo: area = eslora * manga + calado) * 0.85 ) 
#---------------------------------------------------------------------------------------------------------------------------    

# Hijo 2 de BARCO    
class Barco_Pesquero(BARCO): # Clase para calcular el area de un barco pesquero
    def __init__(self, valor1, valor2): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        self.valor1 = valor1
        self.valor2 = valor2
    
    def obtener_area(self): # Modificar segun los parametros de un barco pesquero (Ejemplo)
        return self.valor1 * self.valor2 * 0.75 # Se retorna el area del barcopesquero (Ejemplo)
#---------------------------------------------------------------------------------------------------------------------------

# Hijo 3 de BARCO
class Barco_Velero(BARCO): # Clase para calcular el area de un barco pesquero
    def __init__(self, valor1, valor2): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        self.valor1 = valor1
        self.valor2 = valor2
    
    def obtener_area(self): # Modificar segun los parametros de un barco velero (Ejemplo)
        return self.valor1 * self.valor2 * 0.8 # Se retorna el area del barco velero (Ejemplo)
#---------------------------------------------------------------------------------------------------------------------------

# Hijo 4 de BARCO
class Barco_de_Guerra(BARCO): # Clase para calcular el area de un barco de guerra (Ejemplo)
    def __init__(self, valor1, valor2): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        self.valor1 = valor1
        self.valor2 = valor2
    
    def obtener_area(self): # Modificar segun los parametros de un barco de guerra (Ejemplo)
        return self.valor1 * self.valor2 # Se retorna el area del barco de guerra (Ejemplo)
#---------------------------------------------------------------------------------------------------------------------------    

# Ejemplo: Traductor de texto a otros idiomas Calculadora BARCO

# OPEN-CLOSED / Interface-Segregation Principle
class Traductor(ABC): # Clase para calcular el area de un barco
    @abstractmethod # Decorador para indicar que el método es abstracto,
    def traducir(self, texto): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        pass

# Hija 1 de Traductor
class Traductor_Español(Traductor): # Clase para calcular el area de un barco motora
    def traducir(self, texto): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        return f"Texto: {texto} traducido al español"

# Hija 2 de Traductor
class Traductor_Ingles(Traductor): # Clase para calcular el area de un barco motora   
    def traducir(self, texto): # Modificar segun los parametros de un barco motora (Ejemplo)
        return f"Texto: {texto} traducido al inglés"

# Hija 3 de Traductor
class Traductor_Ucraniano(Traductor): # Clase para calcular el area de un barco motora
    def traducir(self, texto): # Modificar segun los parametros de un barco motora (Ejemplo)
        return f"Texto: {texto} traducido al Ucraniano"


# Clase mas grande y el corazon del codigo
class Calculadora_de_Barcos: # Clase para calcular el area de un barco:
    def __init__(self, barco, Traductor): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        self.barco = barco
        self.Traductor = Traductor

    
    def calculo_y_Traducccion(self): # El metodo estatico se usa para que no se cree una instancia de la clase ya que no se necesita
        area = self.barco.obtener_area() # Se instancia la clase barco y se retorna el area del barco (Ejemplo)
        areaPies = Calculo_Area.calculo_cuadrados(area) # Se instancia la clase calculo_area y se retorna el area del barco (Ejemplo)
        antiFouling = Calculo_Pintura.calcular_antifouling(area) # Se instancia la clase calculo_pintura y se retorna el area del barco (Ejemplo)
        primer = Calculo_Pintura.calcular_primer(area) # Se instancia la clase calculo_pintura y se retorna el area del barco (Ejemplo)
        
        resultadoOriginal = (
            f" Area: {area} metros cuadrados, AntiFouling: {antiFouling} pinturas, Primer: {primer} pinturas"
        )
        return self.Traductor.traducir(resultadoOriginal)    
#---------------------------------------------------------------------------------------------------------------------------    

# Para introducir valores para cada caso se debe hacer mediante un metodo de opcion y bucles.

# Instanciar las clases
valor1_Usuario1 = int(input("Ingrese el valor 1: ")) # Se solicita al usuario el valor 1
valor2_Usuario1 = int(input("Ingrese el valor 2: ")) # Se solicita al usuario el valor 2

print("\n")
BarcoVelero = Barco_Velero(valor1_Usuario1, valor2_Usuario1)
BarcoMotor = Barco_a_Motor(12, 13)

TraductorEspañol = Traductor_Español()
TraductorIngles = Traductor_Ingles()

calculo1 = Calculadora_de_Barcos(BarcoVelero, TraductorEspañol)
calculo2 = Calculadora_de_Barcos(BarcoMotor, TraductorIngles)  

resultado1 = calculo1.calculo_y_Traducccion()
resultado2 = calculo2.calculo_y_Traducccion()

print(resultado1)
print(resultado2)

'''
# Barco de Guerra
Barco_de_Guerra = Barco_de_Guerra(12, 13)
Traductor_Ucraniano = Traductor_Ucraniano()
claculo3 =Calculadora_de_Barcos = Calculadora_de_Barcos(Barco_de_Guerra, Traductor_Ucraniano)    
resultado3 = Calculadora_de_Barcos.calculo_y_Traducccion()
print(resultado3)
print("\n")
'''