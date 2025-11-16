''' Ejercicio 6:

Problema de Transformación y Filtrado de Nombres:

Imagina que te encuentras desarrollando una herramienta de procesamiento de
nombres para una aplicación de gestión de contactos. Tienes una lista de
nombres en el formato "Apellido, Nombre", realiza las siguientes tareas:

1. Utiliza la función lambda para transformar una lista de nombres completos
al nuevo formato.

2. Filtra la lista para incluir solo los nombres que contienen al menos dos
vocales y tienen una longitud mayor a 10 caracteres.

A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada:Lista de nombres, ej: ["Pérez, Juan", "García, José", "López, María", "Martínez, Ana", "Rodríguez, Pedro"]

Salida: Nombres filtrados, ej: ['María López', 'José García', 'Ana Martínez', 'Pedro Rodríguez', 'Juan Pérez']
'''

# Lista de nombres en formato "Apellido, Nombre"
nombres = ["Pérez, Juan", "López, María", "García, José", "Martínez, Ana", "Rodríguez, Pedro"]  

# Función lambda para transformar nombres al formato "Nombre Apellido"
transformar_nombre = lambda nombre: f"{nombre.split(', ')[1]} {nombre.split(', ')[0]}"

# Filtrar nombres con al menos dos vocales y longitud mayor a 10 caracteres
nombres_filtrados = list(filter(
    lambda nombre: sum(1 for c in nombre.lower() if c in "aeiou") >= 2 and len(nombre) > 10,
    map(transformar_nombre, nombres)
))

def contar_caracteres(nombre):
    # Cuenta solo letras y espacios, ignora comas
    return len(nombre.replace(",", ""))

print("\nNombres originales y sus modificaciones:\n")
for original in nombres:
    modificado = transformar_nombre(original)
    if modificado in nombres_filtrados:
        print(
            f"Nombre original: {original} (Longitud: {contar_caracteres(original)} caracteres)  "
            f"-->  Nombre Modificado: {modificado} (Longitud: {contar_caracteres(modificado)} caracteres)"
        )
