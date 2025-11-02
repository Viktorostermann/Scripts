# --- Metodo de ordenamiento SORT() --- Ordena elementos de una lista por orden alfabetico o por numero de manera permanente


# 1- --- Ordenar una lista de coches por orden alfabetico y Bucle. Adicionalmente se imprime solo la primera letra del Auto --- 

#Ejemplo_1:
            # for objeto in lista:
            # print(objeto)
print("\n")
coches = []
coches = ['bmw'.title(), 'audi'.title(), 'seat'.title()]
coches.sort()
print("Lista de coches ordenada por orden alfabetico: ", coches)
for coches in coches: # El siguiente FOR() Trabaja directamente con el objeto de la lista y no con el indice del objeto
    print(coches.title())
print("------------------------------------------------------------------------------------------")

# 2- --- Ordenar una lista de coches por orden alfabetico y Bucle ---

#Ejemplo_2:
            # for i in range(0, len(lista)):
            # print(lista[i]) 
print("\n")
coches = []
coches = ['bmw'.title(), 'audi'.title(), 'seat'.title()]
coches.sort()
print("Lista de coches ordenada por orden alfabetico: ", coches)
for i in range(0, len(coches)): # El siguiente FOR() Trabaja directamente con el indice del objeto y no con el objeto de la lista
    print("El coche en la posicion", i, "y el coche es un:" , coches[i])
print("------------------------------------------------------------------------------------------")

# 3- --- Ordenar una lista de coches por orden alfabetico con Bucle y mostrar la primera letra del coche, ademas de la cantidad de coches por lista ---

#Ejemplo_3:
            # for i in range(0, len(lista)):
            # print(lista[i]) 
print("\n")
coches = []
coches = ['bmw'.title(), 'audi'.title(), 'seat'.title()]
coches.sort()
print("Lista de coches ordenada por orden alfabetico: ", coches)
for i in range(0, len(coches)): # El siguiente FOR() Trabaja directamente con el indice del objeto y no con el objeto de la lista
    print("El coche en la posicion", i, "y el coche es un:" , coches[i]," Y la primera letra del coche es:", coches[i][0])
print("La cantidad de autos en la lista son: ", len(coches))
print("Lista terminada, Bucle finalizado")    
print("------------------------------------------------------------------------------------------")
