'''RED SOCIAL: 
Una red social tiene una base de datos de usuarios y sus correspondientes amistades. 
Crea un programa que tome una base de datos de una red social como una lista de 
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los 
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas 
diferentes. Deberas eliminar las cuentas duplicadas y después  devolver una tupla de 
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.'''

# Datos de entrada de la Red social 
red_social =  [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro", "Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])] # Lista de usuarios y sus amigos
                                                     

# Eliminar las cuentas duplicadas en lista de amigos
#for i in range(len(red_social)):
  #usaurios = red_social[i][0] # Obtenemos el usuario
  #amigos = red_social[i][1] # Obtenemos la lista de amigos
#for tupla in red_social:
red_social_sin_duplicados = []
for usuarios, amigos in red_social:
    amigos_sin_duplicados = list(set(amigos))  # Convertimos la lista de amigos a un set para eliminar duplicados
    red_social_sin_duplicados.append((usuarios, amigos_sin_duplicados))

# Contar el numero de amigos de cada usaurio
amigos_por_usuario = []
for usuario, amigos in red_social_sin_duplicados:
    numero_amigos = len(amigos)  # Contamos el número de amigos
    amigos_por_usuario.append((usuario, len(amigos))) # Agregamos el usuario y el número de amigos a la lista
amigos_por_usuario = tuple(amigos_por_usuario)  # Convertimos la lista a una tupla
print(amigos_por_usuario)

# Obtener usuario con mas amigos
Lista_usuarios = [tupla[0] for tupla in amigos_por_usuario]  # Extraemos los nombres de los usuarios
numero_amigos = [tupla[1] for tupla in amigos_por_usuario]  # Extraemos los números de amigos
print(Lista_usuarios)
print(numero_amigos)

# Obtener el indice con mas amigos
indice_mas_amigos = numero_amigos.index(max(numero_amigos))  # Encontramos el índice del usuario con más amigos
usuario_mas_amigos = Lista_usuarios[indice_mas_amigos]  # Obtenemos el nombre del usuario con más amigos
print(usuario_mas_amigos)


# OutPut: Tuplas de Tuplas -- Uusuario, Numero de amigos
# OutPut: Usuario con mas amigos