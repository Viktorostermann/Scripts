'''Los metodos son "Funciones" que 
   estan asociadas a su vez a otra 
   Funcion Principal / GLobal) 
   que tiene una Clase u Objeto '''


# Para crear una clase se debe realizar los siguiente:

# 1. Definir la clase ---> Nombre_Clase = (Objetos Contenedores)
# 2. Definir los metodos ---> __init__ = (Inicializacion de Funciones)
# 3. Definir los atributos ---> Caracteristicas propias del objeto = (Variables)
# 4. Definir los objetos ---> Instanciar la Clase = (Crear Objetos)

# El metodo __init__ inicializa los atributos de una Clase o Funcion para poder utilizarlos

# Desarrollar un programa que haga una suma simple

class Suma:
    def __init__(self, valor_1, valor_2):
        self.valor_1 = valor_1
        self.valor_2 = valor_2

    def sumar(self):
        return self.valor_1 + self.valor_2

# Crear un objeto de la clase Suma
operacion = Suma(5, 10)

# Acceder a los atributos del objeto
print("")
print(f" El valor del Objeto 1 es: {operacion.valor_1}")  # Salida: El valor 1 es: 5, y el valor 2 es: 10  print(operacion.valor_1)  # Salida: 5
print(f" El valor del Objeto 2 es: {operacion.valor_2}")  # Salida: El valor 1 es: 5, y el valor 2 es: 10  print(operacion.valor_2)  # Salida: 10
print("")
print(f" La suma de los dos objetos es: {operacion.sumar()}")  # Salida: La suma de los dos objetos es: 15 los objetos ---> Instanciar la Clase = (Crear Objetos)
print("")
