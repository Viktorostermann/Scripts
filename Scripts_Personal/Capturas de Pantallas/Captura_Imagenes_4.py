import os
from shutil import move
import time
import pyautogui
#import pyscreeze

def capture_screen():
    try:
        # Capturar pantalla
        image = pyautogui.screenshot()
        # Guardar la captura con un nombre basado en el timestamp
        timestamp = str(time.time())
        filename = f"captura_{timestamp}.png"
        image.save(filename)
        print(f"Captura guardada como: {filename}")
        return filename
    except Exception as e:
        print(f"Error al capturar pantalla: {e}")
        return None

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder created: {path}")

def move_file(src, dst):
    try:
        move(src, dst)
        print(f"File moved: {src} -> {dst}")
    except FileNotFoundError:
        print(f"Error: The file {src} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

# Configurar rutas
destination_folder = "C:\\Capturas"

# Capturar pantalla
captura = capture_screen()

if captura:
    # Mover archivo a la carpeta de destino
    move_file(captura, destination_folder)
    
    # Generar nombre unico basado en timestamp
    timestamp = str(time.time())
    filename = f"registro_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(f"Registro de captura: {timestamp}")
    print(f"File created: {filename}")
else:
    print("No se pudo realizar la captura de pantalla.")
