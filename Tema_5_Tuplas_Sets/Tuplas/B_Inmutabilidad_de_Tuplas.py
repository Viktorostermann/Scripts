print("\n")
# mutabilidad de una lista
mi_lista = [1, 2, 3, 4, 5]
mi_lista[0] = 4 # Reasignacion del valor de la lista
print(mi_lista)
print("\n")

# Inmutabilidad de una tupla
mi_tupla = (1, 2, 3, 4, 5)
mi_tupla[0] = 4 # No se puede reasignar el valor de la tupla
print(mi_tupla)
print("\n")

mi_tupla_2 = (1, 2, 3, 4, 5)
mi_tupla_2.append(6) # No se puede agregar un elemento a la tupla
#print(mi_tupla_2)
print("\n") 

mi_tupla_3 = (1, 2, 3, 4, 5)
mi_tupla_3.insert (0,4) # No se puede agregar un elemento a la tupla
#print(mi_tupla_3)
print("\n")
