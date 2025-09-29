'''Crear una funcion para crear y devolver un nombre formateado de acuerdo a los parametros recibidos'''
print("\n")
def recibir_nombre_formateado(nombre, apellido):
    ''' DEvuelve el nombre completo del usuario formateado '''
    nombre_completo = nombre + ' ' + apellido
    return nombre_completo.title()

musico = recibir_nombre_formateado('victor', 'miletic')
print(musico)
print("\n")