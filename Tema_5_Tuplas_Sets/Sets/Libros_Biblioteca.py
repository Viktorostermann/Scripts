# Input data
lista_Libros = [( 'El aleph', 'Jorge Luis Borges'), ('cien años de soledad', 'Gabriel García Márquez'), ('Rayuela', 'Julio Cortázar'), ('El túnel', 'Ernesto Sabato'), ('Ficciones', 'Jorge Luis Borges')]

# Hacemos un recorrido de la lista de libros y los mostramos por pantalla
titulos_y_apellidos = []  # Lista para almacenar los títulos y apellidos de los autores
for tupla in lista_Libros:
    titulo, autor = tupla # Desempaquetamos la tupla
    apellido = autor.split()[-1] # Obtenemos el apellido del autor
    titulos_y_apellidos.append((titulo, apellido)) # Agregamos el título y apellido al diccionario
    
print(titulos_y_apellidos) # Mostramos los datos de cada libro

# Contamos el número de libros por autor

