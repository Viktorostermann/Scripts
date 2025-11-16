import time
import random

# Variables
puntaje_compu1 = 0
puntaje_compu2 = 0

print("¡Batalla de Bots: Piedra, Papel o Tijera!")

# Bucle del juego
seguir_jugando = "s"
while seguir_jugando == "s":
    # Bots eligen aleatoriamente
    movimiento_compu1 = random.randint(1, 3)
    movimiento_compu2 = random.randint(1, 3)
    
    # Conversión de números a opciones
    opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}
    eleccion_compu1 = opciones[movimiento_compu1]
    eleccion_compu2 = opciones[movimiento_compu2]
    
    # Muestra las elecciones
    print("\n¡Nueva ronda!")
    time.sleep(1)
    print("Bot 1 eligió:", eleccion_compu1)
    time.sleep(1)
    print("Bot 2 eligió:", eleccion_compu2)
    time.sleep(1)
    
    # Determina el resultado
    if movimiento_compu1 == movimiento_compu2:
        print("¡Empate!")
    elif (movimiento_compu1 == 1 and movimiento_compu2 == 3) or \
         (movimiento_compu1 == 2 and movimiento_compu2 == 1) or \
         (movimiento_compu1 == 3 and movimiento_compu2 == 2):
        print("Bot 1 gana esta ronda!")
        puntaje_compu1 += 1
    else:
        print("Bot 2 gana esta ronda!")
        puntaje_compu2 += 1

    # Muestra los puntajes
    print("Puntaje: Bot 1 =", puntaje_compu1, "Bot 2 =", {puntaje_compu2})
    
    # Pregunta si continuar
    print("¿Jugar otra vez? (s/n): ")
    seguir_jugando = input().lower()

print("¡Gracias por observar la batalla de bots!")
print("Puntaje final: Bot 1 =", puntaje_compu1, "Bot 2 =", puntaje_compu2)
if puntaje_compu1 > puntaje_compu2:
    print("🎉 ¡Bot 1 es el campeón! 🎉")
elif puntaje_compu2 > puntaje_compu1:
    print("🎉 ¡Bot 2 es el campeón! 🎉")
else:
    print("🤝 ¡Es un empate épico! 🤝")