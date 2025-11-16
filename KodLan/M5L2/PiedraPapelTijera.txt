import time
import random
# Imports ^^^^^^

# Variables y codigo :/
PuntajeCompu = 0
MiPuntaje = 0

print("¡Jugaremos Piedra, Papel o Tijera!")
seguir_jugando = "s"

# Bucles!!!! (Comenzamos el juego):
while seguir_jugando == "s":
    print("Elige: Piedra(1), Papel(2), Tijera(3)")
    movimiento_jugador = int(input("Tu elección: "))
    
    if movimiento_jugador < 1 or movimiento_jugador > 3:
        print("Opción inválida. Elige un número entre 1 y 3.")
        continue
    movimiento_compu = random.randint(1, 3)
    
    # Time..
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    
    #PURO CODIGO DE "Si es que..." Y la puntuacion :) 
    if movimiento_compu == 1:
        eleccion_compu = "Piedra"
    if movimiento_compu == 2:
        eleccion_compu = "Papel"
    if movimiento_compu == 3:
        eleccion_compu = "Tijera"
    print("Yo elegí", eleccion_compu)

    if movimiento_jugador == movimiento_compu:
        print("¡Empatamos!")
    if movimiento_jugador == 1 and movimiento_compu == 3:
        print("¡Ganaste!")
        MiPuntaje = MiPuntaje + 1
    if movimiento_jugador == 2 and movimiento_compu == 1:
        print("¡Ganaste!")
        MiPuntaje = MiPuntaje + 1
    if movimiento_jugador == 3 and movimiento_compu == 2:
        print("¡Ganaste!")
        MiPuntaje = MiPuntaje + 1
    if movimiento_jugador == 1 and movimiento_compu == 2:
        print("¡Perdiste!")
        PuntajeCompu = PuntajeCompu + 1
    if movimiento_jugador == 2 and movimiento_compu == 3:
        print("¡Perdiste!")
        PuntajeCompu = PuntajeCompu + 1
    if movimiento_jugador == 3 and movimiento_compu == 1:
        print("¡Perdiste!")
        PuntajeCompu = PuntajeCompu + 1
    # Codigo...^^^^^^^^^^^^
    # Codigo  diciendo la eleccion de el jugador y la compy, si es que debe ganar o no, etc (LAS PUNTUACIONES)
    
    # Mostrar puntos al final de la ronda
    print("Puntos: Jugador =", MiPuntaje, "Compu =", PuntajeCompu)
    print("¿Jugar otra vez? (s/n): ")
    seguir_jugando = input()

print("¡Gracias por jugar!")
# PORFIN TERMINE