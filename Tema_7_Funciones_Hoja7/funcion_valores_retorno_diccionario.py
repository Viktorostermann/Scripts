'''Crear una funcion para crear y devolver un nombre formateado 
de acuerdo a los parametros dentro del diccionario de la funcion'''

print("")
def construir_persona(nombre, apellido ,edad=""):
    '''Devuelve un diccionario con el nombre completo'''
    persona = {
        "nombre":   nombre,
        "apellido": apellido,
        "edad":     edad
    }
    return persona

datos_persona = construir_persona("Victor", "Miletic", 45)
print(f"El nombre completo es: {datos_persona['nombre']} {datos_persona['apellido']} y su edad es: {datos_persona['edad']}")
print("")
