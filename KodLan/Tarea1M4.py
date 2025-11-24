equipo = []
# Solicitar al usuario que ingrese los nombres de 5 jugadores
# Se usa un bucle para agregar los nombres a la lista 'equipo'
for i in range(5):
    # Pedir el nombre de cada jugador
    jugador = input("Introduce el nombre del jugador " + str(i + 1) + ": ")
    # Agregar el jugador a la lista
    equipo.append(jugador)

# Mostrar el equipo completo con todos los jugadores
print("Aquí está tu equipo:", equipo)

# Preguntar al usuario si desea eliminar a un jugador
# El input se convierte a minúsculas y se elimina cualquier espacio al inicio o final
desea_eliminar = input("¿Quieres eliminar a un jugador del equipo? (si/no): ").strip().lower()

# Si el usuario desea eliminar un jugador
if desea_eliminar == "si":
    # Pedir el nombre del jugador a eliminar
    jugador_a_eliminar = input("Introduce el nombre del jugador que deseas eliminar: ").strip()
    # Verificar si el jugador está en el equipo
    if jugador_a_eliminar in equipo:
        # Eliminar al jugador de la lista
        equipo.remove(jugador_a_eliminar)
        # Mostrar el equipo actualizado
        print("Equipo actualizado:", equipo)
    else:
        # Si el jugador no está en la lista, informar al usuario
        print("El jugador " + jugador_a_eliminar + " no está en el equipo.")
else:
    # Si el usuario no desea eliminar a nadie, informar que no se realizó ningún cambio
    print("No se ha realizado ningún cambio en el equipo.")

# Mensaje final para agradecer al usuario
print("Gracias por usar el programa para gestionar tu equipo de fútbol.")