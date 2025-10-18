def factorial(n):
    ''' Calcular el factorial de n'''
    #INPUT:
    #-n: int
    #OUTPUT:
    #- resultado: int

    # Planteamiento Caso Base
    if n == 0 or n == 1:
        return 1
    
    # Planteamiento sentencia Recursiva
    else:
        return n * factorial(n - 1)

# Caso de uso
print("")
print(factorial(3))
print("")
