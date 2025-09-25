'''Crea un script que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última'''

palabra = input("Introduce una palabra: ")
longitud = len(palabra)
print("\n")

# --- Bucle que recorra el string ---
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])