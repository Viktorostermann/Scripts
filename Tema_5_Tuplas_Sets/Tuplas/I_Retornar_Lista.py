# Ordenar elementos de una tupla
# Crear una lista con los números de la tupla
print("\n")
mi_tupla = (5, 3, 1, 4, 2, 5, 9, 6)
mi_lista_ordenada = sorted(mi_tupla)
print(mi_lista_ordenada)
print(type(mi_lista_ordenada))
print("")

# Retorna un objeto tipo reverse
print("\n")
mi_tupla = (5, 3, 1, 4, 2, 5, 9, 6)
tupla_inversa = reversed(mi_tupla)
print(tupla_inversa)
print(type(tupla_inversa))
print("") 

# Retorna una lista
mi_tupla = (3, 1, 4, 1, 5, 9, 2, 6, 5)
mi_tupla_ordenada = tuple(sorted(mi_tupla))
print(mi_tupla_ordenada)
print(type(mi_tupla_ordenada))
print("")

# Retorna un objeto tipo reverse
mi_tupla = (3, 1, 4, 1, 5, 9, 2, 6, 5)
tupla_inversa = tuple(reversed(mi_tupla))
print(tupla_inversa)
print(type(tupla_inversa))
print("")