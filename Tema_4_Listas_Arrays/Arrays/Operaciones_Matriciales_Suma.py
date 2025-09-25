# Crear una matriz para realizar una operacion de suma de matrices
import numpy as np
print("\n")
a = np.zeros((3, 3), dtype = np.int64) # Matriz o Vector (A) de Ceros
a[:] = 2                               # Asignamos el valor 2 a todos los elementos de la matriz (A)
b = np.arange(1,10).reshape ((3,3))    # Matriz o Vector (B) con valores de 1 a 9
print (a)                              # Imprimimos la matriz (A)   
print(" ")  
print (b)                              # Imprimimos la matriz (B)
print(" ")
print (' ------------- ')
print(" ")
resultado_suma = a + b                 # Suma de las matrices (A) y (B)
print (resultado_suma)                 # Imprimimos la suma de las matrices (A) y (B)
print("\n")