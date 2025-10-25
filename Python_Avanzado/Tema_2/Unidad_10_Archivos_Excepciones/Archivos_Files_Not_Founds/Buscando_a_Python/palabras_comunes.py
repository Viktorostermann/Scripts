'''
Encuentra o crea algunos textos que te gustaría analizar 
(puedes visitar Project Gutenberg (http://gutenberg.org/) 
o crear textos usando ChatGPT). Copia el texto sin formato desde tu navegador 
en un archivo de texto en tu computadora (o descarga los archivos). 
Averigua cuántas veces aparece una palabra o frase en el texto (puedes usar el método count()).
'''

# Libreria os para manejar rutas de archivos
import os

# Ruta absoluta del directorio donde está el script actualmente
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Comprobar que existen los archivos cats.txt y dogs.txt
# Si existen, leer su contenido e imprimirlo

# Lista de archivos a leer y mostrar por pantalla
Python = ['Python.txt']
print("")

def contar_apariciones(filename, palabra):
    """Cuenta las apariciones de una palabra en un archivo de texto."""
    ruta_ubicacion = os.path.join(BASE_DIR, filename)
    with open(ruta_ubicacion, "r", encoding="utf-8") as file:
        print(f"Contenido del archivo {filename}:\n")
        texto = file.read()  # Leer el contenido y convertir a minúsculas
        
        # guardamos el conteo de la palabra buscada
        count = texto.count(palabra)
        return count

# Ejemplo de uso
filename = "Python.txt"  # Reemplaza con el nombre de tu archivo de texto
palabra_count = str("PYTHON")   # Reemplaza con la palabra que deseas buscar

ocurrencias = contar_apariciones(filename, palabra_count)
print(f"La palabra '{palabra_count}' aparece {ocurrencias} veces en el archivo '{filename}'.")
print("")