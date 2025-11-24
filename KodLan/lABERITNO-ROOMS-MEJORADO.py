import time

# Habitaciones ajustadas estrictamente en líneas rectas
rooms = {
    'Comienzo': {'rooms': ['1'], 'items': []},
    '1': {'rooms': ['Comienzo', '2'], 'items': []},
    '2': {'rooms': ['1', '3', '4'], 'items': []},  # Conexión vertical con 4
    '3': {'rooms': ['2', '6'], 'items': ['trap']},  # Trampa
    '4': {'rooms': ['2', '5', '6'], 'items': []},  # Conexión con 2
    '5': {'rooms': ['4'], 'items': ['key']},  # Llave 1
    '6': {'rooms': ['3', '4', '7', '10'], 'items': []},
    '7': {'rooms': ['6', '8'], 'items': []},
    '8': {'rooms': ['7', '9'], 'items': ['key']},  # Llave 2
    '9': {'rooms': ['8'], 'items': []},
    '10': {'rooms': ['6', '11'], 'items': []},
    '11': {'rooms': ['10', '12'], 'items': []},
    '12': {'rooms': ['11', 'Salida'], 'items': []},
    'Salida': {'rooms': ['12'], 'items': []},
}

room = 'Comienzo'
keys = 0  # Llaves recolectadas
game_over = False

while not game_over:
    print('=========================================')
    print("Te encuentras en la habitación:", room)
    for near_room in rooms[room]['rooms']:
        print("Puedes ir a la habitación:", near_room)

    new_room = input("¿A qué habitación deseas ir?: ")
    if new_room not in rooms[room]['rooms']:
        print("Esa habitación no existe o no está conectada.")
        time.sleep(2)
        continue

    if new_room == 'Salida' and keys < 2:
        print("No puedes salir aún. Necesitas ambas llaves.")
        time.sleep(2)
        continue

    if new_room == 'Salida':
        print("¡Felicidades! Has salido del laberinto.")
        time.sleep(2)
        break

    if 'trap' in rooms[new_room]['items']:
        print("¡Has caído en una trampa! Fin del juego.")
        game_over = True
        time.sleep(2)
        break

    room = new_room

    if 'key' in rooms[room]['items']:
        keys += 1
        print("¡Has encontrado una llave! Llaves recolectadas:", keys)
        rooms[room]['items'].remove('key')
        time.sleep(2)