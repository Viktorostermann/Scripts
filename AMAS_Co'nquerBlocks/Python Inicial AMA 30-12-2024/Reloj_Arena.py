# Programa que muestra un reloj en la arena

import time
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Reloj de arena")
    print("Tiempo restante:")
    print("00:00:10")  # Simulación de tiempo restante
    time.sleep(1)  # Espera de un segundo
    print("00:00:09")
    time.sleep(1)
    print("00:00:08")
    time.sleep(1)
    print("00:00:07")
    time.sleep(1)
    print("00:00:06")
    time.sleep(1)
    print("00:00:05")
    time.sleep(1)
    print("00:00:04")
    time.sleep(1)
    print("00:00:03")
    time.sleep(1)
    print("00:00:02")
    time.sleep(1)
    print("00:00:01")
    time.sleep(1)
    print("00:00:00")
    print("¡El reloj ha terminado!")
    print("¡Felicidades por completar el reloj!")
    time.sleep(2)  # Espera de 2 segundos antes de reiniciar el reloj
    # Si deseas que el reloj se reinicie automáticamente, elimina el 'break' anterior

