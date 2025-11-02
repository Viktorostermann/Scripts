'''10. De ne una función llamada "es_divisible" que tome dos parámetros
"num" y "divisor" e imprima True si "num" es divisible por "divisor", o
False si no lo es.'''

print("")
def es_divisible(num, divisor):
    """Verifica si 'num' es divisible por 'divisor'."""
    num = int(input("Introduce un numero entero: "))
    print("")
    divisor = int(input("Introduce otro numero entero: "))
    if divisor == 0:
        return False  # Evitar división por cero
    elif num < divisor:
        return False
    elif num > divisor and num % divisor != 0:
        return False
    elif num > divisor and num % divisor == 0:
        return True
    elif num < divisor and num % divisor == 0:
        return True
    elif num == divisor:
        return True
    elif num < divisor and num % divisor != 0:
        return False
    else:
        return num % divisor == 0
    
# Llamada a la función
print(es_divisible(2, 2))  # True


