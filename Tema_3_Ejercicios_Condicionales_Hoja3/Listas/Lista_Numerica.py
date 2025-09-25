import numpy as np

# Definición de la función


# --- Paso 1
# numeros = np.array([1,2,3,4,5,6,7,8,9,10])

numeros = list(range(1,11))

# ---Paso 2

pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        pares_invertidos = pares[::-1]
    else:
        impares.append(numero)
        impares_invertidos = impares[::-1]
print(pares)
print(impares)
print("\n")
print (pares_invertidos)
print (impares_invertidos)

# ---Paso 3 imprimir el cuadrado de los numeros pares

print ("________________imprime el cuadrado de los numeros pares con bucle______________________")

for numero in pares:
    print(numero**2)

# --- Paso 4 (Invertir listas y convertir el codigo en el menor de numero de lineas posibles
print ("\n")
print ("_________________Convirtiendo el codigo en menor numero de lineas posibles_______________")

numeros_pares_invertidos = [numero**2 for numero in numeros if numero % 2 == 0][::-1]
numeros_impares_invertidos = [numero**2 for numero in numeros if numero % 2 != 0][::-1]
print(numeros_pares_invertidos)
print(numeros_impares_invertidos)
numeros_cuadrados = [numero**2 for numero in numeros]
print ("\n")

print ("__________________Imprimiendo los numeros mas pequeños___________________________________")

# --- Paso 5 utilizar el numero mas pequeño de la lista y imprimelo por pantalla
print ("El numero mas pequeño es: ", min(numeros))
print ("\n")

print ("__________________Imprimiendo los numeros mas grandes____________________________________")

# --- Paso 6 utilizar el numero mas grande de la lista y imprimelo por pantalla
print ("El numero mas grande es: ", max(numeros))
print ("\n")

print ("__________________Imprimiendo la suma sin usar bucles________________________")

# --- Paso 7 suma todos los numeros o elementos de la lista con y sin bucles

suma_numeros = sum(numeros)
print ("La suma de los numeros es: ", suma_numeros)
print ("\n")

print ("___________________Imprimiendo las suma usando bucles________________________")
suma_numeros_bucle = 0
for numero in numeros:
    suma_numeros_bucle += numero
print ("La suma de los numeros es: ", suma_numeros_bucle)
print ("\n")


print ("___________________Imprimiendo las suma usando bucles________________________")
# --- Paso 8 Encuentra el indice del numero 8 en la lista original
print ("\n")
indice_numero_8 = numeros_pares_invertidos.index(8)
indice_numero_8 = numeros_impares_invertidos.index(8)
print ("\n")

