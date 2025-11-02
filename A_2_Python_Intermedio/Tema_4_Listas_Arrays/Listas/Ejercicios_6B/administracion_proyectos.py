''' ADMINISTRACION DE PROYECTOS: 
Eres un gerente de proyectos y necesitas un programa para administrar 
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre, 
una descripción y un responsable asignado. Implementa un programa en 
Python que utilice un diccionario para almacenar la información de las 
tareas. El programa debe permitir agregar nuevas tareas, asignar 
responsables a las tareas existentes, actualizar las descripciones de las 
tareas y mostrar la lista completa de tareas y responsables. 
(Pista: puedes comenzar con un diccionario vacío y construir un 
diccionario de diccionarios) '''

# Creamos el diccionario vacio
tareas = {} 

# Agregar nuevas tareas
tareas["Tarea1"] = {"Descripcion": "Realizar analisis de requerimientos", "Responsable":"Juan"}
tareas["Tarea2"] = {"Descripcion": "Desarrollar funcionalidad principal", "Responsable":"Marta"}
tareas["Tarea3"] = {"Descripcion": "Realizar pruebas unitarias", "Responsable":"Jacobo"}
print("Tareas agregadas con exito")
print("---------------------------------------------------")

#Funcion para asignar responsable a una tarea
tareas["Tarea1"]["Responsable"] = "Elena"
tareas["Tarea2"]["Responsable"] = "Maria"
tareas["Tarea3"]["Responsable"] = "Pedro"
print("Responsables asignados con exito:", tareas)

# Actualizar la descripcion de una tarea
tareas["Tarea1"]["Descripcion"] = "Desarrollar la interfaz de usuario"
tareas["Tarea2"]["Descripcion"] = "Desarrollar la logica de negocio"
tareas["Tarea3"]["Descripcion"] = "Realizar pruebas de integracion"
print("Descripcion de la tarea 2 actualizada con exito:", tareas)
print(" ")

#Mostrar la lista de tareas y responsables
for tarea, info in tareas.items():
    #print(f"Tarea: {tarea}, Descripcion: {info['Descripcion']}, Responsable: {info['Responsable']}")
    print("Tarea", tarea)
    print("Descripcion:", info["Descripcion"])
    print("Responsable:", info["Responsable"])
    print("---------------------------------------------------")
    print(" ")
print("Lista de tareas y responsables:", tareas)