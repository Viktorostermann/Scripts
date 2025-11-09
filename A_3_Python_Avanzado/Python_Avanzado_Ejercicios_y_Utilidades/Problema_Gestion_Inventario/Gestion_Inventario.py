''' Trabajamos en una empresa de logistica. La tarea es desarrollar un sistema
de gestion de inventario. El inventario esta representado como una lista de productos 
ordenados por sus codigos. Cada producto se describe como un diccionario con claves
'codigo' y 'cantidad'. El objetivo es Implementar una funcion recursiva que realice
una busqueda binaia en este inventario y devuelva la cantidad disponible para un 
producto especifico, dado su codigo'''

def buscar_cantidad_producto(inventario, codigo_producto, inicio = 0, fin= None):  
    if fin is None:
        fin = len(inventario) - 1

    # Caso base: si el rango no es valido
    if inicio > fin:
        return 0
    
    medio = (inicio + fin) // 2
    
    # Comparar el codigo del producto con el codigo de la posicion media
    if inventario[medio]['codigo'] == codigo_producto:

        # Caso base:
        return inventario[medio]['cantidad']
    elif inventario[medio]['codigo'] == codigo_producto:
        
        # El codigo va a estar en lado derecho del inventario
        return buscar_cantidad_producto(inventario, codigo_producto, inicio, medio - 1)

