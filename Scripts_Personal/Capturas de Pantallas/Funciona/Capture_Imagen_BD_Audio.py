import os
import mss
import cv2
import pyaudio
import wave
import numpy as np
import sqlite3
import threading
from datetime import datetime

# Definir rutas
DIRECTORIO_IMAGENES = "C:\\Users\\vikto\\Pruebas_VsCode\\Pictures\\VsCode_Screen_Shots"
DIRECTORIO_VIDEOS = "C:\\Users\\vikto\\Pruebas_VsCode\\Videos"
DIRECTORIO_AUDIOS = "C:\\Users\\vikto\\Pruebas_VsCode\\Audios"
DB_PATH = "C:\\Users\\vikto\\Pruebas_VsCode\\Datos\\navegacion.db"

# Asegurar la existencia de los directorios
for ruta in [DIRECTORIO_IMAGENES, DIRECTORIO_VIDEOS, DIRECTORIO_AUDIOS]:
    os.makedirs(ruta, exist_ok=True)

# Función para generar nombres únicos con timestamp
def generar_nombre():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# Detectar movimiento en video
def detectar_movimiento(umbral=50):
    cap = cv2.VideoCapture(0)
    _, frame_anterior = cap.read()

    while True:
        _, frame_actual = cap.read()
        diferencia = cv2.absdiff(cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY),
                                 cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY))
        
        if np.sum(diferencia) > umbral * 1000:
            cap.release()
            return True  # Movimiento detectado
        
        frame_anterior = frame_actual
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Presionar 'q' para salir
            cap.release()
            return False

# Detectar sonido en el ambiente
def detectar_sonido(umbral=500):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=44100, input=True,
                        frames_per_buffer=1024)

    for _ in range(30):
        datos = np.frombuffer(stream.read(1024), dtype=np.int16)
        if np.max(np.abs(datos)) > umbral:
            stream.stop_stream()
            stream.close()
            audio.terminate()
            return True  # Sonido detectado

    stream.stop_stream()
    stream.close()
    audio.terminate()
    return False

# Grabar video si hay movimiento
def capturar_video(duracion=10):
    if detectar_movimiento():
        nombre = f"video_{generar_nombre()}.mp4"
        ruta_video = os.path.join(DIRECTORIO_VIDEOS, nombre)
        cap = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(ruta_video, fourcc, 20.0, (640, 480))

        tiempo_inicio = datetime.now()
        while (datetime.now() - tiempo_inicio).seconds < duracion:
            _, frame = cap.read()
            out.write(frame)

        cap.release()
        out.release()
        print(f"Video guardado: {ruta_video}")
        return nombre
    return None

# Grabar audio si hay sonido
def capturar_audio(duracion=10):
    if detectar_sonido():
        nombre = f"audio_{generar_nombre()}.wav"
        ruta_audio = os.path.join(DIRECTORIO_AUDIOS, nombre)
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1,
                            rate=44100, input=True,
                            frames_per_buffer=1024)

        frames = []
        for _ in range(int(44100 / 1024 * duracion)):
            frames.append(stream.read(1024))

        stream.stop_stream()
        stream.close()
        audio.terminate()

        with wave.open(ruta_audio, 'wb') as archivo:
            archivo.setnchannels(1)
            archivo.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            archivo.setframerate(44100)
            archivo.writeframes(b''.join(frames))

        print(f"Audio guardado: {ruta_audio}")
        return nombre
    return None

# Guardar registros en la base de datos sin sobreescribir
def create_table():
    with sqlite3.connect(DB_PATH) as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS registros
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           tipo TEXT NOT NULL,
                           nombre_archivo TEXT NOT NULL,
                           timestamp DATETIME NOT NULL)''')
        db.commit()

# Agregar nuevo registro a la BD
def guardar_en_bd(tipo, nombre_archivo):
    if nombre_archivo:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect(DB_PATH) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO registros (tipo, nombre_archivo, timestamp) VALUES (?, ?, ?)",
                           (tipo, nombre_archivo, timestamp))
            db.commit()
            print(f"Guardado en la base de datos: {nombre_archivo}")

# Inicializar la base de datos
create_table()

# **MONITOREO CONTINUO**
print("\nSistema iniciado. Presiona 'q' en la ventana de video para apagarlo.")

while True:
    # Capturar imagen
    nombre_imagen = f"captura_{generar_nombre()}.png"
    ruta_imagen = os.path.join(DIRECTORIO_IMAGENES, nombre_imagen)
    with mss.mss() as captura:
        captura.shot(output=ruta_imagen)
    print(f"Imagen guardada: {ruta_imagen}")
    guardar_en_bd("imagen", nombre_imagen)

    # Capturar video si hay movimiento
    thread_video = threading.Thread(target=lambda: guardar_en_bd("video", capturar_video(5)))
    thread_video.start()

    # Capturar audio si hay sonido
    thread_audio = threading.Thread(target=lambda: guardar_en_bd("audio", capturar_audio(5)))
    thread_audio.start()

    # Permitir apagar el sistema manualmente con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\nSistema apagado.")
        break

print("Captura finalizada.")
