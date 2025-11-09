''' Funciones Lambda:

Ejercicio 5:

Problema de Análisis de Datos de Ventas:

Imagina que eres parte de una empresa de comercio electrónico y tienes
información detallada sobre las ventas de productos. Cada venta se representa
como un diccionario, que incluye el nombre del producto, la fecha de venta, el
monto de la venta y la ubicación del comprador. Realiza un análisis avanzado
de estas ventas.

1. Filtra las ventas realizadas en el último trimestre del año.
2. Selecciona solo las ventas de productos con un monto superior a $500.
3. Agrupa las ventas por ubicación del comprador.
4. Calcula el promedio del monto de venta para cada ubicación.
5. Ordena las ubicaciones por el promedio del monto de venta de forma
descendente. Utiliza funciones lambda.

A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada: Registro de ventas (json,dic,etc)

Salida: Ubicaciones por promedio, ej. : [Chile, Ecuador]
'''

from itertools import groupby

def ordenar_empleados(empleados):
    empleados_ordenados = sorted(empleados, key=lambda empleado: (empleado['rendimiento'], empleado['edad']), reverse=True)
    return empleados_ordenados

def agrupar_empleados_por_pais(empleados_ordenados):
    # Agrupar empeleados por país
    empleados_agrupados = {pais: list(grupo_empleados) for pais, grupo_empleados in groupby(empleados_ordenados, key=lambda empleado: empleado['pais'])}
    return empleados_agrupados
    #for pais in set(empleado['pais'] for empleado in empleados_ordenados):

def mostrar_empleados_agrupados(empleados_agrupados):
    print("\n")
    print("Empleados ordenados:")
    for pais, grupo_empleados in empleados_agrupados.items():
        print("")
        print(f"País: {pais}")
        for empleado in grupo_empleados:
            print(f"Nombre: {empleado['nombre']} - Edad: {empleado['edad']} - Rendimiento: {empleado['rendimiento']}")

empleados = [
    {'nombre': 'Juan', 'edad': 30, 'pais': 'Colombia', 'rendimiento': 8},
    {'nombre': 'María', 'edad': 25, 'pais': 'Perú', 'rendimiento': 7},
    {'nombre': 'Pedro', 'edad': 35, 'pais': 'Argentina', 'rendimiento': 6},
]

empleados_ordenados = ordenar_empleados(empleados)
empleados_agrupados = agrupar_empleados_por_pais(empleados_ordenados)
mostrar_empleados_agrupados(empleados_agrupados)
print("")