'''
En la clase de hoy aprendimos sobre los bucles for y while
su estructura algunas funciones, e hicimos un ejercicio incluyendo lo aprendido
'''
import time
import keyboard  # Necesitarás instalar la librería 'keyboard' para detectar la barra espaciadora
import threading # Necesitarás instalar la librería 'keyboard' para detectar la barra espaciadora
import sys

# Ejercicio para crear un reloj digital que muestre las horas, minutos y segundos por consola 
# y que se detenga cuando precione barra espaciadora

#    
for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
            time.sleep(1) 
            #if keyboard.is_pressed('space'):
                #print("Deteniendo el reloj")
                #sys.exit()
            # Limpiar la consola (opcional, para que parezca un reloj real)
            if segundo != 59 or minuto != 59 or hora != 23:
                print("\033c", end="")
                time.sleep(1)
                # time.sleep(1)  # Esperar 1 segundo
            else:
                print("El reloj ha terminado su ciclo de 24 horas.")
                break
                sys.exit()