'''
Durante esta clase aprendimos a crear y utilizar *decoradores personalizados*
en Python para modificar el comportamiento de funciones. 
Implementamos un decorador llamado reintentar_3_veces, 
que permite *reintentar automáticamente la ejecución de una función hasta tres veces* 
en caso de error, con pausas de un segundo entre intentos. 
Además, desarrollamos otro decorador llamado validar_datos que 
*verifica los tipos de datos* de los argumentos antes de ejecutar una función, 
lanzando errores si no se cumplen los requisitos. 
Estos ejercicios reforzaron conceptos clave como funciones de orden superior, 
manejo de errores con try/except, argumentos posicionales y por palabra clave, 
y encapsulamiento de lógica mediante funciones internas (wrapper). 
Todo se probó en un entorno de celdas tipo notebook, 
permitiendo analizar el funcionamiento de cada decorador paso a paso.
'''

''' Nota: La funcion de un decorador es envolver una funcion dentro de otra,
que permite agregar funcionalidades adicionales sin modificar la funcion original
los decoradores se identifican por tener el simbolo @ encima de la funcion
''' 
# Decorador es una funcion que modifica el comportamiento de una funcion. Envuelve otra funcion y la expande funcionalidad
# Envuelve una funcion (wrapper)
# Devolver una funcion modificada

# Ejemplo 1: Decorador que valida los tipos de datos de los argumentos que coincidan con los tipos especificados

# Primero retornamos la funcion decoradora.
# Luego retornamos la funcion wrapper. 
# Y finalmente retornamos la funcion original.

def validar_datos (tipos_de_datos): # Recibe los tipos de datos esperados como argumento.
    def decorador(func): # Envuelve la funcion.
        def wrapper(*args,**kwargs): # Funcion interna que recibe los argumentos posicionales y nombrados.
            
            for i, (arg, tipo_esperado) in enumerate(zip(args, tipos_de_datos)):
                if not isinstance(arg, tipo_esperado):
                    raise TypeError(f"El argumento {i} debe ser de tipo {tipo_esperado.__name__}, no [{type(arg).__name__}]")
            
            # Verificar los tipos de datos de los argumentos o palabras claves nombrados con el ciclo for    
            if kwargs and len(tipos_de_datos) >len(args): 
                for key , tipo_esperado in zip(kwargs.keys(), tipos_de_datos[len(args):]):
                    if not isinstance(kwargs[key], tipo_esperado):
                        raise TypeError(f"El argumento {key} debe ser de tipo {tipo_esperado.__name__}, no [{type(kwargs[key]).__name__}]")
            
            return func(*args, **kwargs)
        return wrapper
    return decorador

# Funcion para crear el producto con validacion de tipos de datos
@validar_datos([int, str, float]) # Validacion de tipos de datos con el decorador
def crear_producto(id, nombre, precio):
    return f"Producto {id}: {nombre} - ${precio} - registrado"
try :
    print(crear_producto(101, "Laptop", 899.99))
    print(crear_producto(102, "Tablet", 299.99))
except Exception as e :
    print(e)


# Verificar los tipos de datos de los argumentos posicionales con el ciclo for
            # la funcion (len) devuelve la cantidad de elementos de una (lista o cadenas)
            # la funcion (enumerate) devuelve el indice y el valor de cada elemento de la lista (args)
            # la instruccion (zip) une dos listas en una sola lista de tuplas con elementos correspondientes, 
            # Ejemplo de comprime zip: Tipo de dato: [(Cantidad = Numero, Producto = String)] / Retorna: [(12, Producto)] 