import time
import random

jugador = {
    'nombre': 'Jugador 1',
    'salud': 100,
    'poder_de_ataque': 10
}

enemigo = {
    'nombre': 'Jugador 2',
    'salud': 100,
    'poder_de_ataque': 8
}

def atacar(agresor, defensor):
    dano = random.randint(1, agresor['poder_de_ataque'])
    defensor['salud'] -= dano
    print(agresor['nombre'] + " ataca a " + defensor['nombre'] + " causando " + str(dano) + " puntos de dano.")

while jugador['salud'] > 0 and enemigo['salud'] > 0:
    atacar(jugador, enemigo)
    time.sleep(1)
    
    if enemigo['salud'] <= 0:
        print(enemigo['nombre'] + " ha sido derrotado. ¡" + jugador['nombre'] + " gana!")
        break
    
    atacar(enemigo, jugador)
    time.sleep(1)
    
    if jugador['salud'] <= 0:
        print(jugador['nombre'] + " ha sido derrotado. ¡" + enemigo['nombre'] + " gana!")
        break

    print("Salud de " + jugador['nombre'] + ": " + str(jugador['salud']))
    print("Salud de " + enemigo['nombre'] + ": " + str(enemigo['salud']))
    print('-' * 20)