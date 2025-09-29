'''Definir una funcion que me permita escribir el nombre de mi mascota 
y decir que tipo de animal es, se debe mostrar la informacion de la mascota'''

print("")
def descripcion_de_mascota(nombre_mascota, tipo_animal):
    '''Mostrar informacion de mascota.'''
    
    print("Tengo un " + tipo_animal + ".")
    print("Mi mascota se llama " + nombre_mascota + " y es un" + tipo_animal + ".")

descripcion_de_mascota(nombre_mascota="Luna", tipo_animal="perro")
print("")
