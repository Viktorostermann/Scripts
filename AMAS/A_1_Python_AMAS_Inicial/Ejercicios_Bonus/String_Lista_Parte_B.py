'''
Supón ahora que tu input es un string como este:
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’
'''

# --- Base de datos (Lista de listas con los datos de los alumnos)
base_datos = [["Alvaro", "Gomez", "87654327B", "64782", "1", "7.6", "5.4", "9.3"]]

# --- Cadena de entrada con los datos de los todos los alumnos
cadena_alumnos = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n\
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n\
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n"

# --- Se formatea los datos de entrada de cada alumno

# --- Convertir la cadena de entrada en una lista de listas diferentes para cada alumno
alumnos = cadena_alumnos.split("\n") # separa los datos de la cadena por saltos de línea
for alumno in alumnos:
    alumno = alumno.strip() # separa los datos de cada alumno por espacios en blanco
    datos_alumno = alumno.split() # separa los datos de cada alumno por espacios en blanco
    if datos_alumno: # Comprobamos si la lista de datos del alumno no está vacía. 
                     # Esto es importante para evitar errores
# --- Añade la lista de datos del alumno a la base de datos
        base_datos.append(datos_alumno) 

# --- Recorre la base de datos y calcula la nota media de cada alumno
for alumno in base_datos:
    dni = alumno[2] # obtiene el DNI del alumno
# --- Calcular la nota media
    suma_notas = 0 # inicializa la variable suma_notas
    n_notas = 0 # inicializa la variable n_notas

# --- Recorre la lista de notas del alumno
    for i in range(5, len(alumno)): # recorre la lista de notas del alumno
        suma_notas = suma_notas + float(alumno[i]) # suma las notas del alumno
        n_notas = n_notas + 1 # suma 1 a la variable n_notas sumando el número total de notas
    
    nota_media = suma_notas / n_notas # calcula la nota media del alumno
# --- Imprimir el DNI y la nota media del alumno
    print(f"El alumno con DNI {dni} Tiene una nota media de {nota_media:.2f}")