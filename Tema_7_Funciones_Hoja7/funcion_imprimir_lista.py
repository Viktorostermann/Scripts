'''4. De ne una función llamada "imprimir_lista" que tome una lista como
parámetro y la imprima en la consola.'''

lista = [1, 2, 3, 4, 5]

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

imprimir_lista(lista)

# Ejemplo_2 Otra forma de hacerlo en una sola línea:
numeros = [1, 2, 3, 4, 5]
print(", ".join(map(str, numeros)))

# Ejemplo_3 Otra forma de hacerlo usando unpacking:
numeros = [1, 2, 3, 4, 5]
print(*numeros)

# Ejemplo_4 Otra forma de hacerlo usando unpacking con separador personalizado:
print(' '.join(str(n) for n in [1, 2, 3, 4, 5]))
