from functools import lru_cache

# Funcion Recursiva
def recursiva(i):
    if i == 1:
        return i
    else:
        return i * recursiva(i-1)
    # Caso de prueba 1
print("")
print(f" La recursividad de 100! es =",(recursiva(100)))
print("")   


# Caso de prueba 2
indice = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
fibonacci = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 

fibonacci_cache = {}

@lru_cache(maxsize=20)
def fibonacci_indice(indice):
    if indice <= 1:
        return indice
    else:
        return fibonacci_indice(indice - 1) + fibonacci_indice(indice - 2)

for i in range (1, 11):
    print(f" El fibonacci de {i} es = ",(fibonacci_indice(i)))