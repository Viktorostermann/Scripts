
# TIENDA ONLINE

''' Crea una clase "Producto" con atributos como nombre, precio y cantidad en
stock. Luego, crea una clase "Tienda" que contenga una lista de productos
disponibles y métodos para agregar productos, mostrar el inventario y
realizar una compra.'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado a la tienda.")
    
    def mostrar_inventario(self):
        for producto in self.productos:
            print("Inventario de la tienda:")
            print(f"Nombre: {producto.nombre}, Precio: ${producto.precio}, Stock: {producto.stock}")

    def comprar_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto and producto.stock >= cantidad:
                total_pagar = producto.precio * cantidad
                print(f"Compra realizada: {cantidad} unidades de '{nombre_producto}'. Total a pagar: ${total_pagar}")
                producto.stock -= cantidad
                break
        else:
            print(f"No hay suficientes unidades del producto '{nombre_producto}' en stock.")

    def realizar_compra(self, nombre_producto, cantidad):
        """Alias compatibilidad: llama a comprar_producto."""
        return self.comprar_producto(nombre_producto, cantidad)

# Ejemplo de uso
tienda_online = Tienda()

print()
producto1 = Producto("Camiseta", 20.0, 50)
producto2 = Producto("Zapatos", 50.0, 30)
print()

tienda_online.agregar_producto(producto1)
print()

tienda_online.agregar_producto(producto2)
print()

tienda_online.mostrar_inventario()
print()

tienda_online.realizar_compra("Camiseta", 10)
print()

tienda_online.realizar_compra("Zapatos", 20)
print()

tienda_online.realizar_compra("Gorra", 5)
print()

tienda_online.mostrar_inventario()
print()
