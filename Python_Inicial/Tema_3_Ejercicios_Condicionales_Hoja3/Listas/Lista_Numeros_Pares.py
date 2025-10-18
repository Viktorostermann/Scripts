'''Crea una nueva lista [1,2,3,4,5,6,7,8,9,10] con los números pares de la lista anterior en orden inverso'''

digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
digit = digitos [0:10]
# --- Crea la lista original ---
print("La lista original de numeros es: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

# --- Imprime la lista de forma inversa ---
for i in range (0, len(digit)):
    digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    digitos.reverse()
    print(digitos[i] , sep=' ', end='')
print("\n")

# --- Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por consola ---
print("\n")
for i in digitos: # --- Recorriendo la lista
    if i % 2 == 0: # --- evaluando numeros pares ---
        digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        digitos.reverse()
        print(i**2 , sep=' ', end=' ') # --- Calculando los cuadrados ---
        print("\n")
