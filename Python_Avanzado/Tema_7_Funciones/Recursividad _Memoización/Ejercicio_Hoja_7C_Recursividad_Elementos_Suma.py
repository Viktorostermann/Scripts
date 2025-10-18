def suma_lista(lista):
    ''' Calcular los elementos de una lista
    de numerios enteros'''
    
    #INPUT:
    # - Lista: Lista de numeros enteros

    #OUTPUT:
    #- resultado: int - suma de elementos de la lista


    # Planteamiento Caso Base
    if len(lista) == 1:
        return lista[0]

    # Sentencia recursiva 
    else:
        return (lista[0] + suma_lista(lista[1:]))

# Caso de uso
lista = [1, 2, 3, 4, 5]
suma_lista(lista)

print("")
print(suma_lista(10,2))
print("")


# Planteamiento de Logica del problema
'''
1 + suma_lista([2,3,4,5])
1 + 2 + suma_lista([3,4,5])
1 + 2 + 3 + suma_lista([4,5])
1 + 2 + 3 + 4 + suma_lista([5])
1 + 2 + 3 + 4 + 5
15
'''