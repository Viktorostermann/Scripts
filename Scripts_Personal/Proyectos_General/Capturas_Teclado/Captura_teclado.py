from pynput import keyboard
from time import sleep  
import time

# Configuración inicial
last_time = time.time()
def capture_keyboard_events():
    global last_time
    while True:
        event = keyboard.Events().get()
        if event and event.type == 'keydown' and event.key in ['Ctrl', 'Shift']:
            # Manejar teclas especiales
            pass
        elif event.type == 'keypress':
            current_time = time.time()
            duration = current_time - last_time
            last_time = current_time
            print(f"Tecla pressionada: {event.key}, Duración: {duration} segundos")
            
# Ejecutar la captura
capture_keyboard_events()