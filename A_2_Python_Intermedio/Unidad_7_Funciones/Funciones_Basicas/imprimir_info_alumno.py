'''14. De ne una función llamada "imprimir_info_alumno" que tome un
argumento posicional “nombre”(y sin valor por defecto) y varios
argumentos de palabra clave: "edad", "curso" y “promedio" (puedes
ponerles como valor por defecto None). La función debe imprimir la
información del alumno en un formato legible.'''


# Ejemplo_1 Forma básica de hacerlo:
print("")
def imprimir_info_alumno(nombre, edad=None, curso=None, promedio=None):
    print(f'Nombre: {nombre}')
    if edad is not None:
        print(f'Edad: {edad}')
    if curso is not None:
        print(f'Curso: {curso}')
    if promedio is not None:
        print(f'Promedio: {promedio}')
    print("")

imprimir_info_alumno("Luis", edad=18, curso="Programación", promedio=9.5)



