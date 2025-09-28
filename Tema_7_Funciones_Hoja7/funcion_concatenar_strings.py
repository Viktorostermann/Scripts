'''6. Escribe una función llamada "concatenar_strings" que tome dos
parámetros "cadena1" y “cadena2" e imprima la concatenación de
ambas cadenas.'''

cadena1 = "Hola "
cadena2 = "Mundo"

print("")
# Ejemplo_1 Forma básica de hacerlo:
def concatenar_strings(cadena1, cadena2):
    '''Concatena dos cadenas y las imprime.'''

    resultado = cadena1 + cadena2
    print(resultado)
concatenar_strings("Hola", " " + "Mundo")
print("")

# Ejemplo_2 Otra forma de hacerlo usando f-strings:
def concatenar_strings(cadena1, cadena2):
    '''Concatena dos cadenas y las imprime.'''

    print(f"{cadena1} {cadena2}")   
concatenar_strings("Hola" , "Mundo")
print("")

# Ejemplo_3 Otra forma de hacerlo usando el método format():
def concatenar_strings(cadena1, cadena2):
    '''Concatena dos cadenas y las imprime.'''

    print(cadena1, "" + cadena2)
concatenar_strings("Hola" , "Mundo")
print("")
