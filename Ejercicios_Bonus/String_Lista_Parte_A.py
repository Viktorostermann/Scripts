'''Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
imprimir la nota media de los alumnos junto con el DNI.

Supón ahora que tu input es un string como este:
‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’

Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
de todos los alumnos en ese string.
'''

# --- Definir la lista con la informacion de un alumno
base_datos = [["Alvaro", "Gomez", "87654327B", "64782", "1", "7.6", "5.4", "9.3"]]

# --- Definir la cadena de caracteres con la informacion de un alumno 
cadena = "David Fernandez 12311267A 43527 2 9.1 7.6 2.4"

# --- Convertir la cadena de entrada en una lista de listas
datos_alumno = cadena.split() # separa los datos de la cadena por espacios en blanco

# --- Introducir la lista con los datos del alumno en una lista en la base de datos
base_datos.append(datos_alumno) # añade la lista de datos del alumno a la base de datos

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
    print(" ")
    print(f"El alumno con DNI {dni} Tiene una nota media de {nota_media:.2f}")
    print(" ")
    
    