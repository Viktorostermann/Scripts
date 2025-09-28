'''7. De ne una función llamada "obtener_maximo" que tome una lista de
números como parámetro y devuelva el número máximo de la lista.'''


lista = [1, 2, 3, 4, 5]
maximo = max(lista)

# Ejemplo_1 Forma básica de hacerlo:
print("")
def obtener_maximo(numeros):
    return maximo
print("El número máximo de la lista es:", obtener_maximo(lista))
print("")

# Ejemplo_2 Otra forma de hacerlo usando un bucle for:
def obtener_maximo(numeros):
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo
print("El número máximo de la lista es:", obtener_maximo(lista))
print("")

# Ejemplo_3 Otra forma de hacerlo usando la función reduce:
from functools import reduce
def obtener_maximo(numeros):
    return reduce(lambda x, y: x if x > y else y, numeros)
print("El número máximo de la lista es:", obtener_maximo(lista))
print("")

# Ejemplo_4 Otra forma de hacerlo usando la función sorted:
def obtener_maximo(numeros):
    return sorted(numeros)[-1]
print("El número máximo de la lista es:", obtener_maximo(lista))
print("")

# Ejemplo_5 Otra forma de hacerlo usando la función heapq.nlargest:
import heapq
def obtener_maximo(numeros):
    return heapq.nlargest(1, numeros)[0]
print("El número máximo de la lista es:", obtener_maximo(lista))
print("")