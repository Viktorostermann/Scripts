'''Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
completo.
Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
clase'''

estudiantes = ["Juan", "Maria", "Pedro"]

# --- Creamos nuestra base de datos con las notas de cada estudiante---

database = []
for estudiante in estudiantes:
    #Creamos una lista con las notas de cada estudiante
    notas = []
    print(f"Introduce las notas de {estudiante}:")
    # Pedimos las notas de los deberes decada estudiante
    tareas = float(input("Tareas: "))
    # Añadimos las notas a la lista de la base de datos nombres y notas del estudiante
    notas.append(tareas)
    # Pedimos las notas de los exámenes de cada estudiante
    examenes = float(input("Exámenes: "))
    # Añadimos las notas a la lista de la base de datos nombres y notas del estudiante
    notas.append(examenes)
    # Pedimos las notas de los proyectos de cada estudiante
    proyectos = float(input("Proyectos: "))
    # Añadimos las notas a la lista de la base de datos nombres y notas del estudiante
    notas.append(proyectos)
    
    # Añadimos las notas a la lista de la base de datos nombres y notas del estudiante
    #print(f"Notas de {estudiante}: {notas}")

    #Añadimos la lista de notas a la base de datos
    database.append([estudiante, notas])
    #print(f"Base de datos: {database}")



#notas = [ [6.4, 7.0, 9.1], [8.2, 9.8, 6.5], [7.1, 8.4, 5.2] ]
database = [["Juan", [6.4, 7.0, 9.1]], ["Maria", [8.2, 9.8, 6.5]], ["Pedro", [7.1, 8.4, 5.2]]]

'''
# Base de datos
database = [["Juan ", [6.4, 7.0, 9.1]], 
           ["Maria" , [8.2, 9.8, 6.5]], 
           ["Pedro" , [7.1, 8.4, 5.2]]
           ]
'''

print(" ")
print(" ")
print("Calculando medias individuales y totales")
print(" ")
print(" ")


#--- Clacular la nota media de cada estudiante
suma_media = 0
for data in database:
    # Extraemos el nombre del estudiante
    nombre = data[0]
    # Extraemos las notas del estudiante
    notas = data[1]
    # Calculamos la nota media del estudiante
    media = sum(notas) / len(notas)
    # Mostramos la nota media del estudiante
    print(f"Nota media de {nombre}: {media:.2f}")

    suma_media = suma_media + media
    #print("Longitud database",len(database))

    media_clase = suma_media / len(database)
    print("Media de la clase Bucle_1 es: {:.2f}".format(media_clase))
    #print("Print media_clase Bucle_1 es: , {media_clase:.2f}")

# Calculamos la nota media de la clase
total_notas = 0
num_notas = 0
for data in database:
    # Extraemos las notas del estudiante
    notas = data[1]
    # sumar las notas del estudiante
    total_notas = total_notas + sum(notas)
    # numero de motas sumadas
    num_notas = num_notas + len(notas)
    print(f"La cantidad de notas es: {num_notas}")

# Calculamos la nota media de la clase
media_clase = total_notas / num_notas
print(f"Nota media de la clase: {media_clase:.2f}")