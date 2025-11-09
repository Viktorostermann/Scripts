''' Ejercicio 8:

Decorador de Control de Acceso:

Imagina que estás trabajando en el desarrollo de un sistema para una
aplicación de gestión de documentos en un entorno empresarial. Deseas
implementar un decorador llamado verificar_acceso_entorno que permita
controlar el acceso a funciones según el entorno de ejecución.

El decorador debe realizar las siguientes acciones:

1. Antes de ejecutar la función, verificar si el entorno de ejecución es
"producción".

2. Si el entorno es "producción", permitir la ejecución de la función y mostrar
un mensaje indicando que el acceso fue permitido en el entorno de
producción.

3. Si el entorno no es "producción", evitar la ejecución de la función y mostrar
un mensaje indicando que el acceso está restringido a entornos de
producción.

Luego, aplica este decorador a dos funciones, subir_documento y
eliminar_documento . Intenta ejecutar estas funciones con diferentes entornos y
observa el comportamiento del decorador.

A continuacion un ejemplo de una posible entrada y salida de la solucion:

Entrada:
- entorno : ‘produccion’ / ‘desarrollo’
- subir_documento("Documento1")
- eliminar_documento("Documento1")

Salida:
- Acceso permitido / rechazado :
- Documento subido
- Documento eliminado

'''