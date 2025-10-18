# Espacio en memoria listas Vs tuplas
import sys
mi_lista = [1, 2, 3, "hola", True]
print("\n")
print(sys.getsizeof(mi_lista), 'Bytes en uso de memoria para objetos de Lista') # Instruccion para saber el espacio en memoria de una lista
print("")

mi_tupla = (1, 2, 3, "hola", True)
print("")
print(sys.getsizeof(mi_tupla), 'Bytes en uso de memoria para objetos de Tupla') # Instruccion para saber el espacio en memoria de una tupla
print("\n")
