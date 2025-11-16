# Crear un script que me permita realizar una muestra para debuggear como ejemplo de busqueda de archivos en el sistema operativo

import os
import sys

ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Debuggin.json")
print(ruta)
with open(ruta, 'r') as archivo:
    print("")
    print(archivo.read())

print("Fin del programa")
