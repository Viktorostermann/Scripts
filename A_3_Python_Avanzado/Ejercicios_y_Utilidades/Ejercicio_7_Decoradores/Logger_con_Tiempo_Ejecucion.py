''' Decoradores:

Ejercicio 7:

Logger con Tiempo de Ejecución
Imagina que estás desarrollando un sistema complejo que incluye múltiples
funciones críticas. Para asegurarte de que todo funcione correctamente y para
realizar un seguimiento del tiempo de ejecución de estas funciones, decides
implementar un decorador de registro (logger) con tiempo de ejecución.
El decorador debería realizar las siguientes acciones:

1. Antes de llamar a la función original (puedes incluir cualquier función),
debe imprimir un mensaje indicando que la función está a punto de
ejecutarse.

2. Después de que la función se haya ejecutado, debe imprimir un mensaje
que incluya el tiempo que tardó la función en ejecutarse.

3. Si la función original arroja una excepción, el decorador debe manejarla e
imprimir un mensaje adecuado, indicando que se ha producido una
excepción.

A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada: -

Salida: 

- Invocando a la función 'mi_funcion'...
- La función 'mi_funcion' ha tardado 0.0012459754943847656 segundos en ejecutarse.
- Resultados de la funcion: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
'''
    