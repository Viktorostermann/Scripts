# Crear una matriz para realizar una operacion de multiplicacion de matrices

''' [A B ] X [E F ] = [AE + BG AF + BH ] 
    [C D ] X [G H ] = [CE + DG CF + DH ]'''

import numpy as np
print("\n")
a = np.zeros((3, 3), dtype = np.int64) # Matriz o Vector (A) de Ceros
a[:] = 2                               # Asignamos el valor 2 a todos los elementos de la matriz (A)
b = np.arange(1,10).reshape ((3,3))    # Matriz o Vector (B) con valores de 1 a 9
print (a)                              # Imprimimos la matriz (A)   
print(" ")  
print (b)                              # Imprimimos la matriz (B)
print(" ")
print (' ------ Resultado ------- ')
print(" ")
matrix_multi = np.matmul(a, b)        # Multiplicacion de las matrices (A) y (B)
print (matrix_multi)                  # Imprimimos la multiplicacion de las matrices (A) y (B)
print(" ")
print(a*b)
print("\n")