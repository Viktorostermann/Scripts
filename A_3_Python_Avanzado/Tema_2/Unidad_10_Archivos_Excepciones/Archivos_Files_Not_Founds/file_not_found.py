'''
Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de gatos en el primer archivo y tres nombres de perros en el segundo archivo. 
Escribe un programa que intente leer estos archivos e imprima el contenido de cada archivo en la pantalla. 
Envuelve tu código en un bloque try-except para capturar el error de FileNotFoundError, e imprime un mensaje amigable si falta algún archivo. 
Mueve uno de los archivos a una ubicación diferente en tu sistema y asegúrate de que el código en el bloque except se ejecute correctamente. 
Modifica tu bloque except para que falle en silencio si falta alguno de los archivos.
'''
# Libreria os para manejar rutas de archivos
import os

# Ruta absoluta del directorio donde está el script actualmente
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Comprobar que existen los archivos cats.txt y dogs.txt
# Si existen, leer su contenido e imprimirlo


# Lista de archivos a leer y mostrar por pantalla
mascotas = ['gatos.txt', 'perros.txt']
print("")

for filename in mascotas:
    ruta_ubicacion = os.path.join(BASE_DIR, filename)
    try:
        with open(ruta_ubicacion, 'r', encoding='utf-8') as file:
            print(f"Contenido del archivo {filename}:\n")
            contenido = file.read()
            print(contenido)
            print("")
    except FileNotFoundError:
        #pass
        print(f"El archivo {filename} No se encuentra disponible.")
        print("")
    except Exception as e:
        print(f"Error al leer el archivo {filename}: {e}")
        print("")