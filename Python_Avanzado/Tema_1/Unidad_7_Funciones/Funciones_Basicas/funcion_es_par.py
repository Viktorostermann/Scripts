''' 5. Crea una función llamada "es_par" que tome un número como
parámetro e imprima True si es par, o False si es impar.'''

def es_par(numero):
    if numero % 2 == 0:
        print(True)
    else:
        print(False)

# Ejemplo de uso
es_par(4)  # Imprime: True
es_par(7)  # Imprime: False
es_par(0)  # Imprime: True
