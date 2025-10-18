''' Pide 4 números y devuelve 
los numeros introducidos en orden ascendente
y el numero mayor.
Para ello puedes usar listas y bucles for. '''
# --- Definicion de Lista de numeros
lista_numeros = []

# --- Crear un bucle para ir pidiendo los numeros
# --- y añadiendo la lista
for i in range(0,4):
    
    # --- Pido al usuario que introduzca un numero
    num = int(input("Introduce un numero: "))
    
    # lo convierto a entero
    numero = int(numero)
    
    # lo añado a la lista de numeros
    lista_numeros.append(num)

    # --- Imprimo la lista de numeros
    #print(lista_numeros)

    # --- imprimo numero mayor de la lista de la lista por pantalla
    print("El numero mayor es: ", max(lista_numeros))
    
    # --- imprimo la lista de numeros por pantalla ordenada
    print("Los numeros introducidos son: ", sorted(lista_numeros))
    