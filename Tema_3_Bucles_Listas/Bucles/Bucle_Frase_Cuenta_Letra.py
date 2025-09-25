'''Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase.'''

# ---- Pedir frase y letra de la frase
frase = input("Introduce una frase:")
letra = input("Introduce una letra:")

# --- Bucle de la frase
contador = 0
for caracter in frase:
    if caracter == letra :

# --- Contador de la frase 
        contador += 1
print(f"La letra aparece {contador} veces en la frase")

'''
Este programa utiliza un bucle para recorrer cada caracter de la frase. Cuando encuentra
un caracter igual a la letra introducida por el usuario, incrementa el contador en 1.
Finalmente, muestra por pantalla el número de veces que aparece la letra en la frase.'''