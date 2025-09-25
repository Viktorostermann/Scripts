import time
import random

jugador = {
    'nombre': 'Jugador 1',
    'salud': 100,
    'poder_de_ataque': 10,
    'defensa': 0.2,
    'accion': ''  # Inicializamos 'accion' vacía
}

enemigo = {
    'nombre': 'Jugador 2',
    'salud': 100,
    'poder_de_ataque': 8,
    'defensa': 0.15,
    'accion': ''  # Inicializamos 'accion' vacía
}

def atacar(agresor, defensor):
    dano = random.randint(1, agresor['poder_de_ataque'])
    if defensor['accion'] == 'defensa':
        dano = dano * (1 - defensor['defensa'])
    defensor['salud'] -= dano
    print(agresor['nombre'] + " ataca a " + defensor['nombre'] + " causando " + str(int(dano)) + " puntos de dano.")

while jugador['salud'] > 0 and enemigo['salud'] > 0:
    print("Es el turno de " + jugador['nombre'] + ":")
    jugador['accion'] = input("¿Defensa o ataque? ").lower()
    while jugador['accion'] not in ['defensa', 'ataque']:
        jugador['accion'] = input("Por favor, elige entre 'defensa' o 'ataque': ").lower()
    
    atacar(jugador, enemigo)
    time.sleep(1)
    
    if enemigo['salud'] <= 0:
        print(enemigo['nombre'] + " ha sido derrotado. ¡" + jugador['nombre'] + " gana!")
        break

    print("Es el turno de " + enemigo['nombre'] + ":")
    enemigo['accion'] = input("¿Defensa o ataque? ").lower()
    while enemigo['accion'] not in ['defensa', 'ataque']:
        enemigo['accion'] = input("Por favor, elige entre 'defensa' o 'ataque': ").lower()
    
    atacar(enemigo, jugador)
    time.sleep(1)
    
    if jugador['salud'] <= 0:
        print(jugador['nombre'] + " ha sido derrotado. ¡" + enemigo['nombre'] + " gana!")
        break

    print("Salud de " + jugador['nombre'] + ": " + str(jugador['salud']))
    print("Salud de " + enemigo['nombre'] + ": " + str(enemigo['salud']))
    print('-' * 20)