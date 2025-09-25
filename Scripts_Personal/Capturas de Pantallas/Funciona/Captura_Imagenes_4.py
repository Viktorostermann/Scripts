# -*- coding: utf-8 -*-
import os
from shutil import move
import time
import pyautogui

def capture_screen():
    try:
        # Capturar pantalla
        image = pyautogui.screenshot()
        # Usar el timestamp para el nombre, reemplazando el punto para evitar problemas en el nombre del archivo
        timestamp = str(time.time()).replace('.', '')
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
        print(f"Archivo movido: {src} -> {dst}")
    except FileNotFoundError:
        print(f"Error: El archivo {src} no existe")
    except Exception as e:
        print(f"An error occurred: {e}")

# Configurar la carpeta de destino (asegúrate de definir una carpeta, no un archivo)
destination_folder = "C:\Capturas"

# Crear la carpeta de destino si no existe
create_folder(destination_folder)

# Capturar pantalla
captura = capture_screen()

if captura:
    # Construir la ruta final uniendo la carpeta destino con el nombre del archivo capturado
    destination_path = os.path.join(destination_folder, os.path.basename(captura))
    move_file(captura, destination_path)
    
    # Generar un registro con un nombre único basado en el timestamp, limpiando el valor del timestamp para evitar problemas
    timestamp = str(time.time()).replace('.', '')
    registro_filename = f"registro_{timestamp}.txt"
    with open(registro_filename, 'w') as f:
        f.write(f"Registro de captura: {timestamp}")
    print(f"Archivo de registro creado: {registro_filename}")
else:
    print("No se pudo realizar la captura de pantalla.")