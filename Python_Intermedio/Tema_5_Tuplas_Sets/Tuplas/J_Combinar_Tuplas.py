#Combinar tuplas

# Combinar tuplas formando una tupla de tuplas
print("\n")
print("Combinando Tuplas")
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_combinada = tuple(zip(tupla1, tupla2))
print(tupla_combinada)
print("")

# Acceder a los elementos de la tupla de tuplas
mi_tupla = ((1, 'a'), (2, 'b'), (3, 'c'))
print("Accediendo a los elementos de la tupla de tuplas:")
print(mi_tupla[0][0])  # Acceder al primer elemento de la primera tupla
print(mi_tupla[1][1])  # Acceder al segundo elemento de la segunda tupla
print(mi_tupla[2][0])  # Acceder al primer elemento de la tercera tupla
print("\n")
