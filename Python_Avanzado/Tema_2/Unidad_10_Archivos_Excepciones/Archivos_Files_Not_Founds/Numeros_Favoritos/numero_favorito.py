'''
Escribe un programa que solicite al usuario su número favorito. 
Utiliza json.dump() para almacenar este número en un archivo. 
Escribe un programa separado que lea este valor e imprima el mensaje: “Sé cuál es tu número favorito… Es.”
Combina ambos programas en un solo archivo (puedes crear tantas funciones como necesites). 
Si el número ya está almacenado, muestra el número favorito al usuario. 
Si no lo está, solicita al usuario su número favorito y guárdalo en un archivo. 
Ejecuta el programa al menos dos veces para asegurarte de que funciona correctamente.
'''

import json

# Pedir el numero favorito al usuario
# Guardar el numero en un archivo usando json.dump()
# Comprobar si el archivo esta guardado
# Imprimir el numero favorito si ya esta guardado

filename = "Python_Avanzado/Tema_2/Unidad_10_Archivos_Excepciones/Archivos_Files_Not_Founds/numero_favorito.json"

def comprobar_num_fav():
    ''' Comprobar si el numero favorito ya esta guardado o existe
    y si existe devolver el numero favorito, si no devolver None
    '''

    try:
        # Abrir el archivo en modo lectura
        with open('numero_favorito.json', 'r') as file:
            # Cargar el numero favorito usando json.load()
            num_fav = json.load(file)
            return num_fav  # Devolver el numero favorito
    except FileNotFoundError:
        return None  # Si el archivo no existe, devolver None

# Funcion que guarda el numero favorito en un archivo
def guardar_num_fav(num_fav):
    ''' Guardar el numero favorito en un archivo '''
    # Abrir el archivo en modo escritura
    with open(filename, 'w') as file:
        # Guardar el numero favorito usando json.dump()
        json.dump(num_fav, file)


# Funcion que pregunta el numero favorito al usuario
def pregunta_num_fav():
    ''' Preguntar al usuario su numero favorito '''
    # Preguntar al usuario su numero favorito
    num_fav = input("¿Cuál es tu número favorito? ")
    # Guardar el numero favorito en un archivo
    guardar_num_fav(num_fav)
    return num_fav

# Imprmir el numero favorito si ya esta guardado
def print_num_fav(num_fav):
    ''' Imprimir el numero favorito '''
    print(f"Sé cuál es tu número favorito... Es {num_fav}.")

# Progrma principal
numero_fav = comprobar_num_fav()

if numero_fav:
    print_num_fav(numero_fav)
else:
    numero_fav = pregunta_num_fav()
    print_num_fav(numero_fav)