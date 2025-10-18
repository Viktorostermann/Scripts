''' " Las tuplas son elementos inmutables, es decir, no se pueden modificar. "
"1- No permiten añadir, eliminar, o mover elementos de la tupla. "
"(append, remove, insert, pop, del, clear, etc.) "
"2- Permite extraer porciones pero eso da como resultado una tupla nueva"
"3- Permiten comprobar si un elemento se encuentra en la tupla"
"4- Las tuplas son mas rapidas que las listas"
"5- Las tuplas ocupan menos espacio en memoria que las listas"
"6- Las tuplas son mas seguras que las listas"
"7- Las tuplas ocupan menos espacio en memoria que las listas" ("Si requerimos guardar" \
"muchos elementos en una sola variable, y en el futuro solo queremos recorrerlos para verlos es mejor usar tuplas")
"8- Las tuplas Pueden ser como llaves de un diccionario" '''

# Sintaxis de una tuplas
print("\n")
mi_tupla = ("Viktor","Mariano","Carlos","Juan","Pedro","Vicente") # Con el uso de parentesis (Recomendable)
print(type(mi_tupla))
print(mi_tupla)
print("\n")

otra_tupla = ("Frutas", 45, False) 
print(type(otra_tupla))
print(otra_tupla)
print("\n")

mi_tupla_2 = "Frutas", 45, False # Sin el uso de parentesis (No recomendable)
print(type(mi_tupla_2))
print(mi_tupla_2)
print("\n")

# Sintaxis de Listas
mi_lista = ["Viktor","Mariano","Carlos","Juan","Pedro","Vicente"]
print(type(mi_lista))
print(mi_lista)
print("\n")

otra_lista = ["Frutas", 45, False]
print(type(otra_lista))
print(otra_lista)
print("\n")
