''' Trabajar con matrices en Python sin usar librerías externas como NumPy. 
Aprendimos a crear matrices desde cero, implementar operaciones básicas 
(suma, multiplicación por escalar) y avanzadas (multiplicación matricial), 
calcular determinantes para aplicaciones prácticas como resolver sistemas de ecuaciones, 
y visualizar matrices con formato profesional. Todo esto usando solo listas anidadas y bucles, 
entendiendo la lógica detrás de las operaciones matriciales que paquetes como NumPy optimizan.'''

import numpy as np

def crear_matriz(filas: int, columnas:int ,valor_defecto=0): 
    # Crea una matiz de tamaño x filas y x columnas llena de "valor_defecto"
    # Equivalente a numpy.zeros() o numpy.full()
    
    # return [[valor_defecto for _ in range(columnas)] for _ in range(filas)] <---- Esto es un bucle comprimido / Compresion de listas
    matriz = []
    for i in range(filas):
        fila = []
        for j in range (columnas):
            fila.append(valor_defecto)
        matriz.append(fila)
    return matriz


def multiplicar_por_escalar(matriz:list , escalar : float) -> list:
    #Multiplicar cada elemento de la matriz por un escalar
    #Equivalente a numpy.multiply(matriz,escalar)
    
    return [[elemento * escalar for elemento in fila] for fila in matriz] # <----- Utilizamos la compresion de listas y comentamos el bucle
    # matriz_nueva = []
    # for fila in matriz:
    #    fila_nueva = []
    #    for elemento in fila:
    #        fila_nueva.append(elemento*escalar) 
    #    matriz_nueva.append(fila)
    # return matriz_nueva



# lista_zeros = np.zeros(2) # Valor entre parentesis es = (1 Columna x 1 Fila)
# print(type(lista_zeros)) # < ------ Matriz Numpy.array
# print(np.full(3,5)) # < ----- Vector 3 columnas de un mismo valor
# print(type(crear_matriz(2,2)))
# print(lista_zeros)
# print(crear_matriz(2,2))  # <------ Vector sin numpy
# print(crear_matriz(2,2,5))  # <----- Vector sin numpy


# Multiplica cada elemento por 1.5 (ESC_MUL) 
# Crea una matriz de 2x2 con todos los valores en 5 (MTZ_2x2)

print(multiplicar_por_escalar(crear_matriz(2,2,5),1.5)) 
