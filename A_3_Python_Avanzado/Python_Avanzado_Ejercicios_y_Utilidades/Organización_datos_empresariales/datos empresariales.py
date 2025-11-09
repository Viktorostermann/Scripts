'''Funciones Lambda:
Ejercicio 4:
Problema de Organización de Datos Empresariales:
Imagina que trabajas en una empresa internacional con equipos distribuidos en
diferentes países. Cada equipo tiene una lista de empleados, representados
como diccionarios, con información sobre el nombre, la edad y el rendimiento
en proyectos recientes.
Tu tarea es organizar una lista consolidada de todos los empleados de la
empresa. La organización debe seguir ciertas reglas:
1. Los empleados se deben ordenar por el rendimiento en proyectos recientes
de forma descendente.
2. Para aquellos con el mismo rendimiento, se deben ordenar por edad de
forma ascendente. Además, deseas agrupar a los empleados por país para
un análisis más efectivo. Utiliza funciones lambda.'''

from itertools import groupby

def ordenar_empleados(empleados):
    empleados_ordenados = sorted(empleados, key=lambda emp: (emp['rendimiento'], -emp['edad']), reverse=True)
    return empleados_ordenados

def agrupar_empleados_por_pais(empleados_ordenados):
    empleados_agrupados = {pais: list(grupo_empleados) for pais, grupo_empleados in groupby(empleados_ordenados, key=lambda emp: emp['pais'])}
    return empleados_agrupados

def mostrar_empleados_agrupados(empleados_agrupados):
    for pais, grupo_empleados in empleados_agrupados.items():
        print(f"Empleados del país {pais}:")
        for empleado in grupo_empleados:
            print(empleado)
            print("")

empleados = [
    {'nombre': 'Juan', 'edad': 30, 'pais': 'España', 'rendimiento': 8},
    {'nombre': 'María', 'edad': 25, 'pais': 'Francia', 'rendimiento': 7},
    {'nombre': 'Pedro', 'edad': 35, 'pais': 'España', 'rendimiento': 6},
    {'nombre': 'Ana', 'edad': 28, 'pais': 'Alemania', 'rendimiento': 9},
]

empleados_ordenados = ordenar_empleados(empleados)
empleados_agrupados = agrupar_empleados_por_pais(empleados_ordenados)
print("")
mostrar_empleados_agrupados(empleados_agrupados)
print("")