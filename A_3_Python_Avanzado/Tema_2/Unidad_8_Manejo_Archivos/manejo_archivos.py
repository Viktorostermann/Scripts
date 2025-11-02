''' Ejemplo de primera clase de conquer asociada a manejo de archivos'''

import numpy as np

# Ejemplo_1: Lectura y escritura de manejo de archivos en Python
filename='archivo_ejemplo.txt'
with open('archivo_ejemplo.txt', 'w', encoding='utf-8') as archivo_objeto: # w = write, r = read, a = append encoding = para evitar problemas con caracteres especiales
    contenido = archivo_objeto.read() # lee todo el contenido del archivo
    print(contenido)

# Ejemplo_2: Agregar contenido a un archivo existente
filename = 'archivo_ejemplo.txt'
with open('archivo_ejemplo.txt', 'a', encoding='utf-8') as archivo_objeto: # w = write, r = read, a = append encoding = para evitar problemas con caracteres especiales
    if archivo_objeto is not None:
        print('El archivo existe.')
    else:
        print('El archivo no existe.')

# Ejemplo_3: Crear un archivo y escribir varias líneas
filename = 'programa.txt'
with open('programa.txt', 'w', encoding='utf-8') as archivo_objeto: # w = write, r = read, a = append encoding = para evitar problemas con caracteres especiales
    archivo_objeto.write('Primera línea de texto.\n')
    archivo_objeto.write('Segunda línea de texto.\n')
    archivo_objeto.write('Tercera línea de texto.\n')

# Ejemplo_4: Imprimir el contenido del archivo línea por línea
filename = 'programa.txt'
with open('programa.txt', 'r', encoding='utf-8') as archivo_objeto: # w = write, r = read, a = append encoding = para evitar problemas con caracteres especiales
    for linea in archivo_objeto:
        print(linea.strip())  # strip() elimina los espacios en blanco y saltos de línea adicionales

# Ejemplo_5: Guardar por separado la informacion de linea por linea por linea leida de un archivo
filename = 'digits.txt' 
with open(filename) as archivo_objeto: # w = write, r = read, a = append encoding = para evitar problemas con caracteres especiales
    for linea in archivo_objeto:
        filename.append(linea.strip())  # strip() elimina los espacios en blanco y saltos de línea adicionales
    print(filename)
print(filename[0])
print(type(filename))

# Ejemplo_6: Escribir en Archvios vacios
filename = 'archivo_vacio.txt'
with open('archivo_vacio.txt', 'w', encoding='utf-8') as archivo_objeto: # w = write, r = read, a = append encoding = para evitar problemas con caracteres especiales
    archivo_objeto.write('Este es un archivo nuevo.\n')
    archivo_objeto.write('Contiene varias líneas de texto.\n')
    archivo_objeto.write('Fin del archivo.\n')

# Ejemplo_7: Añadir Elementos a un Archivo existente
filename = 'archivo_vacio.txt'
with open('archivo_vacio.txt', 'a', encoding='utf-8') as archivo_objeto: # w = write, r = read, a = append encoding = para evitar problemas con caracteres especiales
    archivo_objeto.write('Esta es una línea añadida al final del archivo.\n')
    archivo_objeto.write('Otra línea añadida.\n')
    archivo_objeto.write('Última línea añadida.\n')

# Ejemplo_8: 
filename = 'archivo_vacio.txt'
f = open(filename, 'w')  # Abrir el archivo en modo lectura
f.write("Nueva línea de texto")  # Escribir en el archivo

