'''
En la clase de hoy se vio cómo manejar diferentes estructuras de datos en Python y NumPy 
para organizar y manipular información de manera eficiente. 
Se trabajó con listas, aprendiendo a agregar, eliminar y recorrer elementos. 
Luego, se exploraron las tuplas, destacando su inmutabilidad. 
También se estudiaron los sets, conjuntos sin orden ni duplicados, 
y sus operaciones básicas como agregar, eliminar y verificar elementos. 
Finalmente, se introdujo NumPy para crear arrays con diferentes tipos de datos 
y cómo usar vistas (view) para reinterpretar la memoria sin copiar datos. 
Estas herramientas son fundamentales para manejar datos en programación.
'''

# Listas
mi_lista = [] # Lista vacía
print("")

mi_lista = [10, 20, 30, 40, 50] # Lista con elementos
print("")
print(f"Sirve para almacenar secuencia de datos diferentes tipos variables modificables, mutables {mi_lista}")

mi_lista.append(60) # Agrega un elemento al final de la lista
print(mi_lista)

mi_lista[2] = 35 # Modifica el valor del tercer elemento de la lista por 35
print(mi_lista)

mi_lista[2] = 35
mi_lista.remove(35) # Elimina un elemento específico de la lista
print(mi_lista)

len(mi_lista) # Longitud de la lista
print("")
print(len(mi_lista)) # Imprime el tamaño de la lista

# Ejercicio.
''' Crea una lista de compra con almenos 4 elementos.
Luego muestra la lista completa,
agrega un nuevo producto
ELimina uno que ya no necesites.
Muestra uno que ya no ncesites.
Elimina uno que ya no estas usando.'''

lista_compra = ["Pan", "leche", "Huevos", "azucar"]

print(lista_compra)

lista_compra.append("Arroz") # Agregar un nuevo producto a la lista de compra

lista_compra.remove("Leche")
del lista_compra[-1] # Elimina el último elemento de la lista

