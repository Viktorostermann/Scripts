import time 

rooms = {
    'Start': {'rooms': ['1'], 'items': []},
    '1': {'rooms': ['Start', '2', '3'], 'items': []},
    '2': {'rooms': ['1'], 'items': ['key']},
    '3': {'rooms': ['1', '4'], 'items': []},
    '4': {'rooms': ['3', '5'], 'items': []},
    '5': {'rooms': ['4', 'Exit'], 'items': []}
}

room = 'Start'
key = False 
while True:
    print('=========================================')
    print("Tu te encuentras en la habitacion", rooms)
    for near_room in rooms[room]['rooms']:
        print("Puedes ir a la habitacion", near_room)
    new_room = input("¿A que habitacion desea ir?: ")
    if new_room