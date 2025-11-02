"""
Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
una mayúscula o una minúscula.
"""

# --- Pedirn al usuario ingrese una letra
letra = input("Introduce una letra: ")

# --- Comprobacion de longitud del input
if len(letra) == 1:

    # --- Condicional
    # --- Si es mayuscula imprimimos o si es minuscula igualmente
    if 65 <= ord(letra) <= 90:
        print("La letra introducia es una letra Mayuscula")
    elif 97 <= ord(letra) <= 122:
        print("La letra introducida es una letra Minuscula")
else:
    # --- Si es un carcater no reconocido se indicara
    print("Error. Debe introducir una unica letra o caracter valido")
