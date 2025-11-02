# CLases - > Protagonistas de la POO (Estructura de datos y Contenedores de Objetos)
# Clases - > Dentro de las clases se crean Instancias de una clase (Se crean objetos a partir de clases)
# Objeto - > Instancia de una clase (Objetos son instancias de una clase)
# Atributos -> Variables que pertenecen al objeto (Objetos son instancias de una clase)
# Metodos -> Funciones que pertenecen al objeto (Objetos son instancias de una clase)

# Abstraccion -> Permite crear nuevas clases basadas en otras clases existentes (Permite reutilizar codigo)
# Modularidad -> Permite dividir un programa en partes mas pequeñas y facilmente manejables (Permite reutilizar codigo)
# Herencia -> Permite crear nuevas clases basadas en otras clases existentes (Permite reutilizar codigo) de Clases Padre a Clases Hijas.
# Encapsulamiento -> Permite ocultar los atributos y metodos de una clase para evitar que sean modificados por otros objetos (Permite reutilizar codigo)
# Polimorfismo -> Permite crear multiples objetos a partir de una misma clase (Permite reutilizar codigo)


# Crear Clase Personas con sus respectivos atributos y metodos.
    # Atributos: Nombre, Apellido, Edad, DNI, Telefono, Email.
class Persona:
    def __init__(self, nombre, apellido, edad, dni, tel, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.tel = tel
        self.email = email

# Metodos Mostradares Generales --------------------------

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, DNI: {self.dni}, Telefono: {self.tel}, Email: {self.email}"

    def mostrar_nombre(self):
        return f"Nombre: {self.nombre}"
    
    def mostrar_apellido(self):
        return f"Apellido: {self.apellido}"
    
    def mostrar_edad(self):
        return f"Edad: {self.edad}"
    
    def mostrar_dni(self):
        return f"DNI: {self.dni}"
    
    def mostrar_tel(self):
        return f"Telefono: {self.tel}"
    
    def mostrar_email(self):
        return f"Email: {self.email}"

# Ejemplo de uso:
print("")
persona1 = Persona("Juan","Perez",35,"12345678","1122334455","juan.perez@gmail.com")
print(persona1.mostrar_datos())
print("")

persona2 = Persona("Maria","Gomez",28,"87654321","9988776655","maria.gomez@gmail.com")
print(persona2.mostrar_datos())
print("")

persona3 = Persona("Luis","Garcia",42,"34567890","1122334455","luis.garcia@gmail.com")
print(persona3.mostrar_datos())
print("")