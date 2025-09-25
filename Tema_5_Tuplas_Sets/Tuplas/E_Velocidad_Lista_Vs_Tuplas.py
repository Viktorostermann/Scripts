import timeit

# Calculo de la diferencia de tiempo de ejecucion entre Tuplas y Listas
print("\n")
mi_tupla =  (1, 2, 3, 4, 5)
mi_lista =  [1, 2, 3, 4, 5]
print("El tiempo de ejecucion de la lista es:", timeit.timeit(stmt="[1,2,3,4,5]", number=10000000))
print("")
print("El tiempo de ejecucion de la tupla es:", timeit.timeit(stmt="(1,2,3,4,5)", number=10000000))
print("\n")

# Calcular diferencia entre tuplas y lista
print("La diferencia de tiempo entre la lista y la tupla es: ", timeit.timeit(stmt="[1,2,3,4,5]", number=10000000) - timeit.timeit(stmt="(1,2,3,4,5)", number=10000000))
print("\n")
