# Longitud de tuplas
print("\n")
print(" -------------- Longitud de tuplas ---------------")
print("")
mi_tupla = ("fruta", 45, True)
longitud = len(mi_tupla)
print("La longitud de la tupla es:", longitud)
print("\n")

# Numero de apariciones de un elemento en un tupla
print(" -------------- Numero de apariciones de un elemento en un tupla ---------------")
print("")
mi_tupla = ("fruta", 45, True, "fruta", 45, "fruta")
cantidad = mi_tupla.count("fruta")
print("La cantidad de veces que aparece 'fruta' en la tupla es:", cantidad)
print("\n")

# Indicar en que indice se encuetra un elemento en una tupla
print(" -------------- Indicar en que indice se encuetra un elemento en una tupla ---------------")
print("")
mi_tupla = ("fruta", 45, True, "fruta", 45, "fruta")
indice = mi_tupla.index("fruta")
print("El índice de la primera aparición de 'fruta' en la tupla es:", indice)
print("\n")

# Maximos y Minimos de una Tupla

print(" -------------- Maximos y Minimos de una Tupla ---------------")
print("")
mi_tupla = (1, 2, 3, 4, 5 , 6, 7, 8, 9, 10)
maximo = max(mi_tupla)
minimo = min(mi_tupla)
print("El máximo de la tupla es:", maximo)
print("")
print("El mínimo de la tupla es:", minimo)
print("\n")

