''' 
Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y en que posición. 
Puedes usar find()). Puedes usar el archivo pi_10000.txt
'''

# Leer el archivo pi_10000.txt y buscar la fecha de nacimiento
# Guardar el contendo ----> .read()
# BUscar un string dentro de pi ----> .find()

# Libreria os para manejar rutas de archivos
import os

# Ruta absoluta del directorio donde está el script actualmente
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Comprobar que existen los archivos cats.txt y dogs.txt
# Si existen, leer su contenido e imprimirlo

def buscar_fecha_en_pi(filename, string):
    ''' 
    Buscar la fecha de nacimiento deltro del archivo 
    de las primeras 10000 cifras de pi
    '''

    # Abrir el archivo y leer su contenido
    ruta_ubicacion = os.path.join(BASE_DIR, filename)
    with open(ruta_ubicacion, 'r', encoding='utf-8') as file:
        pi_digits = file.read()  # Leer el contenido del archivo
        posicion = pi_digits.find(string)  # Buscar la posición de la cadena
        return (posicion) # Devolver la posición (o -1 si no se encuentra)

# Ejemplo de uso
filename = 'pi_10000.txt' # Nombre del archivo con los dígitos de pi
string = '30041980' #  Fecha de nacimiento

# Preguntamos la posición de la fecha en pi
posicion = buscar_fecha_en_pi(filename, string)
# Se imprime el resultado encontrado
if posicion != -1:
    print("")
    print(f"La fecha '{string}' se encuentra en la posición {posicion} de pi.")
# Si no se encuentra la fecha
else:
    print("")
    print(f"La fecha '{string}' no se encuentra en los primeros 10000 dígitos de pi.")
    print("")