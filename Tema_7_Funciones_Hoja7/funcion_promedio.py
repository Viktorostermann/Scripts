'''12. Escribe una función llamada "calcular_promedio" que tome una lista de
números como parámetro y calcule el promedio de esos números. Si no
se proporciona una lista, debe usar una lista vacía por defecto.'''


print("")
def calcular_promedio(lista=[]):
    if len(lista) == 0:
        return None
    return sum(lista) / len(lista)
lista = [1, 2, 3, 4, 5]
promedio = calcular_promedio(lista)
print("El promedio de sumatoria de los elementos de la lista es:", promedio)
print("")