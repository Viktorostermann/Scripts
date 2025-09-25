''' Pide 4 números y devuelve 
los numeros introducidos en orden ascendente
y el numero mayor.
Para ello puedes usar listas y bucles for. '''
# --- Definicion de Lista de numeros
lista_numeros = []
terminado = False

# --- Crear un bucle para ir pidiendo los numeros

# --- y añadiendo la lista
while terminado == False:
    
    # --- Pido al usuario que introduzca un numero
    numero = input("Introduce un numero: ")

    # --- Si el numero es alguna letra se detiene el bucle y regresa al inicio hasta cargar la cantidad solicitada
    if numero.isnumeric() == False: # --- Comprobacion de errores comprobando que cada elemento introducido es un numero, de los cuales no puede haber separadores o delimitadores
       print("El numero no es valido")
       continue
    
    # --- Lo convierto a entero
    numero = int(numero)
    
    # lo añado a la lista de numeros
    lista_numeros.append(numero)

    # --- Imprimo la lista de numeros
    if len(lista_numeros) == 4:
        terminado = True

# output bucle --- print lista_numeros enteros
#print(lista_numeros)

# --- Devolver numero mayor de la lista de la lista por pantalla
#print("El numero mayor es: ", max(lista_numeros))
    
# --- Devolver numeros orden ascendente
#print("Los numeros introducidos son: ", sorted(lista_numeros))

# --- Imprimo el numero mayor de la lista de numeros
lista_numeros.sort()
print("El numero mas alto es:" ,lista_numeros[-1] ,"y la lista ordenada en forma ascendente es:" ,lista_numeros)