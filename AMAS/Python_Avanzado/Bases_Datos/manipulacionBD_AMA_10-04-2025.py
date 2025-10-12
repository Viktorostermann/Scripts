# Sistema de gestion de biblioteca (BD MOCKEADA)
from abc import ABC, abstractmethod

# Enumerable (Enum) para los tipos de libros modelo de datos
from enum import Enum

# Generador de identificadores unicos   
import uuid

# --------------------------- ENUMS ESTADOS Y ROLES -------------------------------- #
# __________________________________________________________________________________ #

# Modelo de datos libro: 
class EstadoLibro(Enum):
    '''Enum para estados posibles de un libro'''
    DISPONIBLE = 'Disponible'
    PRESTADO = 'Prestado'
    RESERVADO = 'Reservado'
    MANTENIMIENTO = 'Mantenimiento'

# Modelo de datos Usuario:
class RolUsuario(Enum):
    '''Enum para roles posibles de un usuario'''
    ADMINISTRADOR = 'Administrador'
    USUARIO = 'Usuario'
# ---------------------------------------------------------------------------------- #


# ----------------------------- MODELOS DE DATOS ----------------------------------- #
# __________________________________________________________________________________ #

# Tabla de libros bd mockea datos: Modelo de datos Libros
# 1. Columnas del archivo (atributos del objeto)
# 2. Clave primaria (id)
# 3. Atributos (isbn, titulo, autor, estado, prestamo, fecha_prestamo)


# Tabla de libros bd mockea datos: Modelo de datos Libros
class Libro: # Clase libro
    def __init__(self, titulo, autor, isbn): 
        self.id = str(uuid.uuid4()) # Genera un id unico clave primaria
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = "Disponible" # Estado por defecto
        self.prestamo = None # Prestamo por defecto
        self.fecha_prestamo = None # Reserva por defecto
    def __str__(self):
        return f"{self.titulo} - {self.autor} - ({self.estado.value})"

#libro = Libro('mil y una noche', 'GGM', '123')
#print(libro)

# ------------------ Clases de usuarios PATRON DE DISEÑO (SRP) --------------------- #
class Usuario: # Tabla de usuarios bd mockea datos: Modelo de datos Usuarios
    def __init__(self,nombre, apellido, email, rol=RolUsuario.USUARIO):
        self.id = str(uuid.uuid4())
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.rol = rol
        self.libros_prestados = [] # Lista de libros prestados por usuarios
        self.activo = True # Activo por defecto
        self.reservas = [] # Lista de reservas por usuario
    def __str__(self):
        return f"{self.nombre} {self.rol.value}"


# ----------------- REPOSITORIO DE LIBROS PATRON DE DISEÑO (SRP) -------------------- #
# ___________________________________________________________________________________ #


# ------------------ Clase que maneja las operaciones de la bd de libros ------------ #
class RepositorioLibros:

# ------------------ Funcion constructora del repositorio --------------------------- #
    def __init__(self):
        # Diccionario que simula una tabla de libros con su id como clave 
        self.libros = [] # Lista de libros

# ------------------ Funcion para crear un libro en la bd --------------------------- #
    def crear_libro(self, libro):
        self.libros.append[libro.id] = libro # Agrega el libro al diccionario
        return libro

# ------------------ Funcion para actualizar un libro en la bd ---------------------- #    
    def actualizar_libro(self, libro_id, libro, **actualizaciones):
        libro = self._libro.get(libro_id) # Actualiza el libro en el diccionario
        if libro:
            for campo, valor in actualizaciones.items():
                setattr(libro,campo,valor)
            return libro
        return None

# ------------------ Funcion para eliminar un libro en la bd ------------------------ #
    def eliminar_libro(self, libro_id):
        libro = self.libros.pop(libro_id) # Elimina el libro del diccionario
        return libro

# ------------------ Funcion para obtener un libro en la bd ------------------------ #
    def obtener_libro(self, libro_id):
        libro = self.libros[libro_id] # Obtiene el libro del diccionario
        return libro

# ------------------ Funcion para obtener todos los libros en la bd ---------------- #
    def obtener_todos_libros(self):
        return list(self.libros.values())
    
# ------------------ Funcion para prestar un libro a un usuario --------------------- #
    def prestar_libro(self, libro_id, usuario):
        libro = self.obtener_libro(libro_id) # Obtiene el libro del diccionario
        if libro.estado == EstadoLibro.DISPONIBLE.value: # Verifica si el libro esta disponible
            libro.estado = EstadoLibro.PRESTADO.value # Cambia el estado del libro a prestado
            usuario.libros_prestados.append(libro) # Agrega el libro a la lista de libros prestados del usuario
            return True

        return False
    

# ----------------- REPOSITORIO DE USUARIOS PATRON DE DISEÑO (SRP) -------------------- #
# _____________________________________________________________________________________ #

# CLase que maneja las operaciones de la bd de usuarios
class RepositorioUsuarios:
    def __init__(self):
        self.usuarios = {}

    def crear_usuario(self, usuario):
        self.usuarios[usuario.id] = usuario
        return usuario
    
    def actualizar_usuario(self, usuario_id, usuario, **actualizaciones):
        usuario =self._usuarios.get(usuario_id)
        if usuario:
            for campo, valor in actualizaciones.items():
                setattr(usuario,campo,valor)
        return usuario
    
    def eliminar_usuario(self, usuario_id):
        usuario = self.usuarios.pop(usuario_id)
        return usuario

    def obtener_usuario(self, usuario_id):
        usuario = self.usuarios[usuario_id]
        return usuario
    
    def obtener_todos_usuarios(self):
        return list(self.usuarios.values())


# --------------- REPOSITORIO DE CLASES BASE PATRON DE DISEÑO (SRP) --------------------------------- #
'''  Los repositorios siguientes son clases no implementadas, pero son futuras implementaciones que 
pueden crearse y desarrollar para manejar en futurolas operaciones de la bd de libros y usuarios
heredadas por otras clases que manejan las operaciones de la bd de libros y usuarios y se encargan 
de realizar las operaciones CRUD sobre la bd de libros y usuarios. Los metodos abstractos son los que 
se implementaran en las clases hijas aqui podemos observar el significado o la aplicacion de: 
Abstraccion, Encapsulamiento y Polimorfismo'''
# ___________________________________________________________________________________________________ #

class RepositorioBase(ABC):
    def __init__(self):
        self._datos={}

    @abstractmethod
    def crear(self, entidad):
        pass

    @abstractmethod
    def actualizar(self, entidad_id, entidad_actualizada):
        pass

    @abstractmethod
    def eliminar(self, entidad_id):
        pass

    @abstractmethod
    def obtener(self, entidad_id):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def prestar_libro(self, libro_id, usuario):
        pass

    @abstractmethod
    def devolver_libro(self, libro_id, usuario):
        pass
    
    @abstractmethod
    def reservar_libro(self, libro_id, usuario):
        pass
    
    @abstractmethod
    def cancelar_reserva(self, libro_id, usuario):
        pass
    
    @abstractmethod
    def buscar_libro_por_autor(self, autor):
        pass
    
    @abstractmethod
    def buscar_libro_por_titulo(self, titulo):
        pass
    
    @abstractmethod
    def buscar_libro_por_isbn(self, isbn):
        pass
    
    @abstractmethod
    def buscar_libro_por_estado(self, estado):
        pass
    
    @abstractmethod
    def buscar_libro_por_fecha_prestamo(self, fecha_prestamo):
        pass
    
    @abstractmethod
    def buscar_libro_por_fecha_reserva(self, fecha_reserva):
        pass
    
    @abstractmethod
    def buscar_libro_por_fecha_devolucion(self, fecha_devolucion):
        pass


Usuario = Usuario('Juan', 'Perez', 'juan@gmail.com')
print(Usuario)

