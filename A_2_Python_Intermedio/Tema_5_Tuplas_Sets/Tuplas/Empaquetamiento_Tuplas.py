''' Los errores en las tuplas se pueden observar cuando le indicas a la tupla que:
1- Te muestre una cantidad mayor de elementos de los que tiene la tupla.
2- Te muestre una cantidad menor de elementos de los que tiene la tupla.
3- Te muestre un elemento que no existe dentro de la tupla.
'''

# Empaquetamiento de tuplas
print("\n")
mi_tupla = "fruta", 45, True
print(mi_tupla)
print(type(mi_tupla))
print("")

# Desempaquetamiento de tuplas
mi_tupla = ("fruta", 45, True)
string, entero, booleano = mi_tupla
print(string)
print(entero)
print(booleano)
print(type(mi_tupla))
print("\n")