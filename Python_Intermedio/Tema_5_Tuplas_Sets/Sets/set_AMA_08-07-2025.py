#Sets
''' 
    Los sets son estructuras de datos que se utilizan para almacenar un conjunto de elementos, 
    pero con una característica especial: no pueden contener elementos duplicados.
    Los sets son mas rapidos que las listas
    Los sets ocupan menos espacio en memoria que las listas
    Los sets son mas seguros que las listas
    Los sets ocupan menos espacio en memoria que las listas
    Si requerimos guardar muchos elementos en una sola variable, y en el futuro solo queremos recorrerlos para verlos es mejor usar sets
    Los sets Pueden ser como llaves de un diccionario
    Los sets son mas facil de usar que las listas
    Los sets no permiten datos duplicados'''

# Creando mi Set
mi_set = { 10, 20, 30, 40, 50 }
print(type(mi_set)) # <class 'set'>

mi_set.add(60) # Agregamos un elemento al set
print(mi_set)

mi_set.remove(10) # Eliminamos un elemento del set
print(mi_set)

mi_set.discard(30) # Eliminamos un elemento del set
print(mi_set)

mi_set.clear() # Eliminamos todos los elementos del set
print(mi_set)

# Comprobar si un elemento existe en el set
print(10 in mi_set) # True
print(100 in mi_set) # False


