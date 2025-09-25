# Crear un diccionario vacío para almacenar los jugadores y sus estadísticas
jugadores = {}

# Solicitar nombres de jugadores y sus goles
for i in range(3):
    nombre = input("Ingresa el nombre del jugador: ")
    goles = int(input("Ingresa la cantidad de goles marcados por " + nombre + "."))
    jugadores[nombre] = goles

# Mostrar el diccionario con las estadísticas iniciales
print("Estadísticas de goles:", jugadores)

# Preguntar al usuario qué estadísticas quiere cambiar
jugador_a_actualizar = input("¿Qué estadísticas te gustaría cambiar? ")

# Verificar si el jugador está en el diccionario
if jugador_a_actualizar in jugadores:
    # Solicitar el nuevo número de goles
    nuevos_goles = int(input("Ingresa el recuento de goles actualizado para " + jugador_a_actualizar + ": "))
    jugadores[jugador_a_actualizar] = nuevos_goles
    # Mostrar el diccionario con las estadísticas actualizadas
    print("Estadísticas de goles actualizadas:", jugadores)
else:
    print(jugador_a_actualizar + " no está en el diccionario.")