def numero_triangular(n):
    ''' Calcular los elementos de una lista
    de numeros triangulares'''
    
    #INPUT:
    # - n: int positivos

    #OUTPUT:
    # - resultado: int positivo

    # Caso base
    if n == 1:
        return 1
    
    # Caso recursivo
    else:
        return (n + numero_triangular(n-1))

# Caso de uso 
print("")
print(numero_triangular(5))
print("")

# Ejemplo de la logica de la funcion con el valor 5
'''
5 + numero_triangular(4) 
5 + 4 + numero_triangular(3)
5 + 4 + 3 + numero_triangular(2)
5 + 4 + 3 + 2 + numero_triangular(1)
5 + 4 + 3 + 2 + 1 = 15
'''