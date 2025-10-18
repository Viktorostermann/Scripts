'''Crea un script que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras
de la palabra introducida empezando por la última'''

# --- Pedir palabra al usuario
palabra = input("Introduce una palabra: ")
print("\n")

# --- Bucle que recorra el string ---
for letra in palabra[::-1]:
    print(letra)