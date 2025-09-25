'''Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
los números primos de la lista original. Además, el script debe devolver el número total de
números primos encontrados y la suma de los números primos encontrados
'''

# --- Lista de numerois enteros 
# + lista vacia para los numeros primos
# + numero total de numeros primos
# + suma de los numeros encontrados

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = []
total_primos = 0
suma_primos = 0

# --- Bucle para recorrer la lista de numeros
for numero in numeros:
    # comprobar si el numero es primo
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo == True:
        primos.append(numero)
        total_primos = total_primos + 1
        suma_primos = suma_primos + numero

# comprobar si el numerio es primo
## si es primo lo añadimos a la nueva lista
print("Numeros primos encontrados: ", primos)
print("Total de numeros primos encontrados: ", total_primos)
print("Suma de numeros primos encontrados: ", suma_primos)



