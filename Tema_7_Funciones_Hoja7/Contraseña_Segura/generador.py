'''
CONTRASENA SEGURA:

Crea un script que solicite una contraseña, analice si es segura y si no lo es
sugiera una nueva contraseña. Para ello puedes crear un script validador.py
que contenga una funcion validar_contrasena que reciba una cadena y
veri que si cumple con los requisitos mínimos de una contraseña segura
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). La función debe devolver un
valor booleano que indique si la contraseña es válida o no. Por otro lado
puedes crear otro script creador.py con una función llamada
generar_contrasena que genere contraseñas seguras de forma aleatoria. Lafunción debe permitir especi car la longitud de la contraseña y qué tipos de
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
minúsculas, números y caracteres especiales).
(Para el generador de contraseñas puedes probar a usar los modulos
random y string)
'''
import random
import string

def generar_contrasena_segura(longitud = 9,incluir_mayusculas=True,incluir_minusculas=True,incluir_numeros=True,incluir_caracteres_especiales=True):
    
    '''Genera una contraseña segura dada una longitud'''
    # Longitud minima de la contraseña segura
    # Incluir_mayusculas: Si la contraseña incluira mayusculas
    # Incluir_minusculas: Si la contraseña incluira minusculas
    # Incluir_numeros: Si la contraseña incluira numeros
    # Incluir_caracteres_especiales: Si la contraseña incluira caracteres especiales
    
    caracteres = ""
    
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase

    if incluir_minusculas:
        caracteres += string.ascii_lowercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return contrasena
    