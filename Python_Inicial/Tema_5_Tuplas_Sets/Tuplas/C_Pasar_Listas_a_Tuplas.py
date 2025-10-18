# Pasar de listas a tuplas
print("\n")
Mi_lista  = [0,1,2, "hola", True]
print("Mi_lista es de tipo...", type(Mi_lista)) # Clase de Objeto Lista
print("")
Mi_tupla = tuple(Mi_lista) # Convertir la lista en tupla
print("Mi_tupla es de tipo...", type(Mi_tupla)) # Clase de Objeto Tupla
print("")
print("Mi_lista ahora es Tupla...", Mi_tupla) # Imprime el cambio de Lista a Tupla 
print("\n")

# Pasar de tuplas a listas
print("\n")
Mi_tupla = (0,1,2, "hola", True)
print("Mi_tupla es de tipo...", type(Mi_tupla)) # Clase de Objeto Tupla
print("")
Mi_lista = list(Mi_tupla) # Convertir la tupla en lista
print("Mi_lista es de tipo...", type(Mi_lista)) # Clase de Objeto Lista
print("")
print("Mi_tupla ahora es Lista...", Mi_lista) # Imprime el cambio de Tupla a Lista 
print("\n")
