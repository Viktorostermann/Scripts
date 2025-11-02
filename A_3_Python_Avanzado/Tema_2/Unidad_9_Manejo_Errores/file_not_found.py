''' File not found exception '''



# Libreria os para manejar rutas de archivos
import os

# Ruta absoluta del directorio donde está el script actualmente
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Comprobar que existen los archivos cats.txt y dogs.txt
# Si existen, leer su contenido e imprimirlo

filename = "test.txt"

try:
    ruta_ubicacion = os.path.join(BASE_DIR, filename)
    with open(ruta_ubicacion, 'r', encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msj = f"Sorry, the file {filename} does not exist."
    print(msj)
else:
    print(contents)