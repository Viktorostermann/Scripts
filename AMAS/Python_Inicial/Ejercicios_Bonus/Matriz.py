''' Crea un script que dada una lista de listas M (Numerica)
identifique si se trata de una matriz y en caso imprima dos listas
correspondientes a:

1- La fila cuyos elementos suman el maximo 
2- La columna cuyos elementos suman el maximo

M1=[[2,5,3],[6,1,8],[7,5,4]]
M2=[[4,2,3],[4,5],[6,8,2]]
'''

# --- Definimos la lista de listas M1
M = [[2, 5, 3],
    [6, 1, 8],
    [7, 5, 4]]
# --- Verificamos si M1 es una matriz
n_columnas = len(M[0])
n_filas = len(M)
es_matriz = True

# --- Recorremos la lista de listas M1
for i in range(0,n_filas):
# --- Verificamos si el número de filas tiene la misma domension de referencia
    if len(M[i]) != n_columnas: #Si no tiene la misma dimension
        es_matriz = False         # Si alguna fila tiene un numero de columnas diferente 
        print("No es una matriz") # de la referencia columna distinta, No es una matriz 
        break
    
# Parte 1 calculamos fila con suma maxima y la imprimimos
# --- Si es una matriz ejecutamos el siguiente codigo
if es_matriz == True:
    # --- Definimos la variable de suma maxima o el indice de la fila con el valor maximo
    suma_maxima = 0    
    # --- Recorremos la lista de listas M1
    for i in range(0,n_filas):
        fila = M[i] # cada una de las filas 
        suma_fila = sum(fila) # calculamos la suma de la fila 
        # --- Verificamos si la suma de la fila es mayor que el maximo o fila anterior
        if suma_fila > suma_maxima:
            # --- Si es mayor actualizamos el maximo
            suma_maxima = suma_fila
            # --- actualizamos el valor del indice de la fila con el valor maximo
            fila_valor_maximo = i
    print(f"\nLa columna con los elementos que suman el maximo, es la columna con los valores de: {M[fila_valor_maximo]} con una suma total de {suma_maxima}")
    print("\n")

# Parte 2 calculamos columna con suma maxima y la imprimimos
'''
M = [[2, 5, 3],
    [6, 1, 8],
    [7, 5, 4]]
'''
# --- Si es una matriz ejecutamos el siguiente codigo
if es_matriz == True:
    # --- Definimos la variable de suma maxima o el indice de la columna con el valor maximo
    suma_maxima = 0    
    # --- Recorremos la lista de listas M1
    for j in range(0,n_columnas):
        columna = [] # cada una de las columnas
        suma_columna = 0 
        # --- Recorremos la lista de listas M1
        for fila in M:
            suma_columa = suma_columna + fila[j] # sumamos los elementos de la columna j
            columna.append(fila[j]) # agregamos el elemento de la columna j a la lista columna
        # --- Verificamos si la suma de la columna es mayor que el maximo o columna anterior
        if suma_columa > suma_maxima:
            # --- Si es mayor actualizamos el maximo
            suma_maxima = suma_columa
            # --- actualizamos el valor del indice de la fila con el valor maximo
            columna_valor_maximo = columna[:]
    print(f"La fila con los elementos que suman el maximo, es la fila con los valores de: {columna_valor_maximo} con una suma total de {suma_maxima}")
    print("\n")
else:
    print("Es una matriz")