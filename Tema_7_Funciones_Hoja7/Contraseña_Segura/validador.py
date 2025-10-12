'''ESta funcion valida como argumento que recibimos de una contraseña segura'''

def validar_contraseña(contrasena):
    ''' ESta funcion valida que la contraseña dada como argumento'''
    longitud_minima = 9
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    # Comprobamos si la contraseña cumple con los requisitos de longitud
    if len(contrasena) < longitud_minima:
        return False
    
    # Comprobamos si la contraseña contiene al menos un número y un carácter especial
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        else:
            tiene_caracter_especial = True
    
    # Comprobamos si la contraseña cumple con todos los requisitos
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial
