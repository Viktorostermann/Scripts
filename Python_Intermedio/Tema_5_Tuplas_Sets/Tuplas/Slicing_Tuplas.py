mi_tupla = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\n")
# Slicing de una tupla interior
tupla_interior = mi_tupla[1]
print("Slicing de mi tupla interior:", tupla_interior)  # (4, 5, 6)
print("")

# Slicing de una porcion de la tupla de tuplas
porcion_tupla = mi_tupla[0:2]
print("Slicing de una porcion de la tupla de tuplas:", porcion_tupla)  # ((1, 2, 3), (4, 5, 6))
print("")

# Slicing de una porcion de una tupla interior
porcion_tupla_interior = mi_tupla[2][0:2]
print("Slicing de una porcion de una tupla interior:", porcion_tupla_interior)  # (7, 8)
print("\n")


# Tupla unitaria
mi_tupla = (1)
print(f"No es tupla. Falta una coma despues del numero (,):",type(mi_tupla)) # Clase de Objeto Entero
print("")

mi_tupla = (1,)
print(f"Si es tupla. Agregando una coma despues del numero (,):",type(mi_tupla)) # Clase de Objeto Tupla
print("")