def potencia(base, exponente):
    ''' Calcular el factorial de un numero'''
    #INPUT:
    # - Base: el numero que queremos elevar (int positivo)
    # - Potencia: int positivo
    #OUTPUT:
    #- resultado: int positivo


    # Planteamiento Caso Base
    if exponente==0:
        return 1

    # Sentencia recursiva 
    else:
        return base*potencia(base,exponente-1)

# Caso de uso
print("")
print(potencia(10,2))
print("")

# Logica de la funcion
'''
10 * potencia (10, 1)
10 * 10 * potencia (10, 0)
10 * 10 * 1 = 100
'''