''' Manejo de archivos JSON en Python '''

import json

numeros = [1, 2, 3, 4, 5]
filename = 'numeros.json'

# Escritura en el archivo JSON
with open(filename, 'w') as f_object:
    json.dump(numeros, f_object)

# Lectura del archivo JSON
with open(filename) as f_object:
    numeros_leidos = json.load(f_object)
print(numeros_leidos)  # Salida: [1, 2, 3, 4, 5]

# Escritura de un diccionario en un archivo JSON
persona = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
with open('persona.json', 'w') as f_object:
    json.dump(persona, f_object)

# Lectura de un diccionario desde un archivo JSON
with open('persona.json') as f_object:
    persona_leida = json.load(f_object)
print(persona_leida) # Salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}



