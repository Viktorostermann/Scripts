'''
GESTIÓN DE VENTAS
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…])

'''

# Nuestra estructura sera una lista de diccionarios

# [{producto: "nombre producto", precio: precio}, 
    # {"producto": "nombre producto", "precio": precio},
    # ...]

ventas = []

def agregar_venta(producto, precio):
    ''' Agregar una venta a la lista de ventas '''
    #Producto: nombre del producto vendido
    #Precio: precio del producto vendido

    # LIsta de Diccionarios productos se agregan al final de la lista
    venta = {
        "producto": producto,
        "precio": precio    
    }
    ventas.append(venta)

def mostrar_ventas():
    for venta in ventas:
        print("")
        print("Producto:", venta["producto"])
        print("Precio:", venta["precio"])
        print("Sub_Total:", "---------> " , venta["precio"])

# Ejemplo de uso:
total_ventas = 0

print("")
agregar_venta("Camiseta", 25.99)
agregar_venta("Pantalón", 39.95)
agregar_venta("Zapatos", 61.25)
mostrar_ventas()
print("")

for venta in ventas:
    total_ventas += venta["precio"]

print("Total de ventas:", "--->", total_ventas)
print("")