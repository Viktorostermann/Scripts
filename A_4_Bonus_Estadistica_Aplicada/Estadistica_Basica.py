'''Estadistica descriptiva'''

from collections import Counter

def calculo(vector):
    '''Funcion que calcula la media, moda y mediana de un vector'''

    # Media_1 ------------------------------------------------------
    suma = 0
    n = 0
    for elemento in vector:
        suma += elemento
        n += 1
    media = suma / n
    print("\nLa media_1 es:", media)

    # Moda ---------------------------------------------------------
    conteo = Counter(vector)
    moda = max(conteo, key=conteo.get)
    print("La moda es:", moda)

    # Mediana ------------------------------------------------------
    vector.sort()
    n = len(vector)
    punto_medio = n // 2
    if n % 2 == 0:
        mediana = (vector[punto_medio - 1] + vector[punto_medio]) / 2
    else:
        mediana = vector[punto_medio]
    print("La mediana es:", mediana)

    return media, moda, mediana


vector = [1,2,3,4,5,6,7,8,9,8,6,5,7,5]
calculo(vector)
print("")
