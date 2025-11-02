'''
En la clase de hoy se vio cómo utilizar estructuras de datos 
como listas anidadas en Python para organizar y gestionar información académica. 
Se aprendió a recorrer estas listas mediante bucles for, extrayendo elementos específicos como nombres y notas. 
También se practicó el uso de funciones integradas como sum() y len() para calcular promedios, 
demostrando cómo aplicar operaciones matemáticas sobre listas. Además, 
se reforzó el concepto de acumuladores para obtener resultados globales, como la media de toda la clase, 
destacando la lógica detrás del procesamiento de datos.
'''

''' Ejemplo de base de dfatos de un colegio: Trabajas en un colegio y estas encargado de mantener un seguimiento
de las notas de los estudiantes de una clase. En tu base de datos tienes una lista con los nombres de los
estudiantes de una clase. En tu base de datos tienes una lista con las notas de los estudiantes de una clase.
y para cada estudiante debes guardar sus nots provenienttes de sus deberes, examenes y proyectos.
Tambien necesitas calculae la nota media de cada estudiante y la nota definitiva de la clase al completo.

Pista: Para resolver este problema puedes usar una lista anidada donde guardas las notas de cada estudiante.
Luego puedes usar un bucle for para recorrer esta lista y calcular la nota media de cada estudiante.
Tambien puedes usar otro bucle for para calcular la nota media de toda la clase.
'''

estudiantes= [
["Alberto", [8, 9, 10]],
["Andres", [7, 6, 8]],
["Maria", [9, 8, 9, ]],
["Juan", [10, 9, 8]],
]

# Calcular la nota media de cada estudiante
suma_total_notas = 0

print("")
print("*** Nota Media de cada Estudiante:")

for estudiante in estudiantes: # Recorremos la lista de estudiantes desde el indice 0 hasta el indice 4 con saltos de 1 en 1.
    nombre = estudiante[0] # Accedemos a la lista de notas del estudiante actual utilizando el índice 1 dentro de la lista estudiantes.
    notas = estudiante[1] # Accedemos a la lista de notas del estudiante actual utilizando el índice 1 dentro de la lista estudiantes.
    media = sum (notas) / len(notas) # Calculamos la media de las notas del estudiante actual utilizando la función sum() y dividiéndola con len() entre la longitud de la lista notas.
    print("")
    print(f" - {nombre} : Nota media: {media:.2f}") # Imprimimos el nombre del estudiante actual.
    print(f" - Notas: {notas}") # Imprimimos las notas del estudiante actual.
    suma_total_notas += suma_total_notas + media # Sumamos la media de las notas del estudiante actual a la variable suma_total_notas.
    
# Calcular la nota media de toda la clase
print("")
media_clase = suma_total_notas / len(estudiantes) # Calculamos la media de la clase utilizando la variable suma_total_notas y la longitud de la lista estudiantes.
print(f"*** Nota media de la clase es: {media_clase:.2f}     \n")