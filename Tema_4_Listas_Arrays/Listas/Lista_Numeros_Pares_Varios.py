'''Crea una nueva lista [1,2,3,4,5,6,7,8,9,10] con los números pares de la lista anterior en orden inverso'''

digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digit = digitos [0:10]
print("\n")

# --- Crea la lista original ---
print("Ejemplo_1: La lista original de numeros es:" ,digitos)
print("\n")

print("Ejemplo_2:")
digit = digitos [0:11]
# --- Imprime la lista de forma inversa ---
for i in range (0, len(digit)):
    digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    digitos.reverse() # --- Imprimiendo los numeros en orden inverso ---
print(digitos , sep=' ', end=' ') 
print("\n")

# --- Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por consola ---
print("Ejemplo_3:")
for i in digitos: # --- Recorriendo la lista
    if i % 2 == 0: # --- evaluando numeros pares ---
        digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        digitos.reverse()
    print(i**2 , sep=' ', end=' ') # --- Calculando los cuadrados ---
print("\n")

# --- Imprime la lista de numeros con Declaracion extendida del Bucle FOR() ---
print(f"Ejemplo_4:")
numeros_cuadrados = []
for valor in range(1,11):
    cuadrado = valor**2
    numeros_cuadrados.append(cuadrado)
print("El cuadrado de los numeros pares es: ", digitos[i]**2 , sep=' ', end=' ')
print("\n")

# --- Imprime la lista de numeros con Declaracion comprimida del Bucle FOR() ---
print(f"Ejemplo_5:")
numeros_cuadrados = [valor**2 for valor in range(1,11)]
print("El cuadrado de los numeros pares es: " ,numeros_cuadrados , sep=' ', end=' ')
print("\n")
