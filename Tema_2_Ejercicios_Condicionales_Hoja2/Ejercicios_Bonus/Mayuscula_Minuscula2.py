"""
Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
una mayúscula o una minúscula.
"""

# --- Pedirn al usuario ingrese una letra
letra = input("Introduce una letra: ")

letras_minusculas = "abcdfghijklmnñopqrstuvwxyz"
letras_mayusculas = "ABCDFGHIJKLMNÑOPQRSTUVWXYZ"
caracter_simbolos = "#$%&/()=?¿+*\{[]-}_<>~^'"
caracter_acentuacion = "´,.:';"
caracter_exclamacion = "!¡"

# --- Comprobacion de longitud del input
if len(letra) == 1:

    # --- Condicional issupper() / islower()

    # --- Si es mayuscula imprimimos o si es minuscula igualmente
    if letra.isupper():
        print("La letra introducia es una letra Mayuscula")
    elif letra.islower():
        print("La letra introducida es una letra Minuscula")
    else:
        if letra in caracter_acentuacion:
            print("La letra introducida es un carcater de acentuacion")
        elif letra in caracter_simbolos:
            print("Usted introdujo un caracter tipo simbolo")
        elif letra in caracter_exclamacion:
            print("Usted introdujo un caracter de exclamacion")
else:
    # --- Si es un carcater no reconocido se indicara
    print("Error. Debe introducir una unica letra o caracter")
