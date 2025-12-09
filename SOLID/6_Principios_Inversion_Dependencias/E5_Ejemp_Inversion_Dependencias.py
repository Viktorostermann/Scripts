from abc import ABC, abstractmethod


# Definir la ABSTRACCION del servicio de almacenamiento de productos
class AlmacenamientoProductos(ABC):
    @abstractmethod
    def agregar_producto(self, nombre: str, cantidad: int):
        pass

    @abstractmethod
    def obtener_stock(self, nombre: str) -> int:
        pass


# Implentacion del almacenamiento de productos
# METODO DE BAJO NIVEL --> detallado
class MemoriaAlmacenamientoProductos(AlmacenamientoProductos):
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre: str, cantidad: int):
        if nombre in self.inventario:
            self.inventario[nombre] += cantidad
        else:
            self.inventario[nombre] = cantidad

    def obtener_stock(self, nombre: str) -> int:
        return self.inventario.get(nombre, 0)


# METODO DE ALTO NIVEL -- logica de negocios
class GestorProductos:
    def set_almacenamiento(self, almacenamiento: AlmacenamientoProductos):
        self.almacenamiento = almacenamiento

    def agregar_producto(self, nombre: str, cantidad: int):
        self.almacenamiento.agregar_producto(nombre, cantidad)
        print(f" Producto { nombre} agregado al inventario")

    def obtener_stock(self, nombre: str):
        stock = self.almacenamiento.obtener_stock(nombre)
        print(f"Stock de {nombre}:{stock}")
        return stock


almacenamiento_memoria = MemoriaAlmacenamientoProductos()

gestor_productos = GestorProductos()
gestor_productos.set_almacenamiento(almacenamiento_memoria)  # INYECCION DE DEPENDENCIAS
gestor_productos.agregar_producto("Camisa", 2)
gestor_productos.agregar_producto("Pantalon", 10)
gestor_productos.obtener_stock("Camisa")
gestor_productos.obtener_stock("Pantalon")

gestor_productos.agregar_producto("Camisa", 1)
gestor_productos.agregar_producto("Pantalon", 1)
gestor_productos.obtener_stock("Camisa")
gestor_productos.obtener_stock("Pantalon")