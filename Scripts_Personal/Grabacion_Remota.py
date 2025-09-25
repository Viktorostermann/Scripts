import os
import pyaudio
import wave
from pydub import AudioSegment
from datetime import datetime

# Definir la carpeta de almacenamiento
DIRECTORIO_AUDIOS = "C:\\Users\\vikto\\Audios"
os.makedirs(DIRECTORIO_AUDIOS, exist_ok=True)

# Configuración de grabación
FORMATO = pyaudio.paInt16
CANALES = 2  # Mono: 1 | Estéreo: 2
FRECUENCIA = 44100  # Frecuencia estándar (puedes probar 48000)
BUFFER_SIZE = 1024  # Ajustar para evitar interferencias
DURACION = 5  # Duración en segundos

# Verificar disponibilidad de dispositivos de audio
def verificar_dispositivos():
    audio = pyaudio.PyAudio()
    print("Dispositivos disponibles:")
    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        print(f"{i}: {info['name']}")
    audio.terminate()

# Generar nombre único para cada grabación
def generar_nombre():
    return datetime.now().strftime("audio_%Y%m%d_%H%M%S")

# Función para grabar audio con detección de errores
def grabar_audio():
    try:
        nombre_archivo_mp3 = os.path.join(DIRECTORIO_AUDIOS, f"{generar_nombre()}.mp3")
        nombre_archivo_wav = nombre_archivo_mp3.replace(".mp3", ".wav")

        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMATO, channels=CANALES,
                            rate=FRECUENCIA, input=True,
                            frames_per_buffer=BUFFER_SIZE)

        print("Grabando audio...")
        frames = []
        for _ in range(int(FRECUENCIA / BUFFER_SIZE * DURACION)):
            frames.append(stream.read(BUFFER_SIZE))

        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Guardar en formato WAV
        with wave.open(nombre_archivo_wav, 'wb') as archivo:
            archivo.setnchannels(CANALES)
            archivo.setsampwidth(audio.get_sample_size(FORMATO))
            archivo.setframerate(FRECUENCIA)
            archivo.writeframes(b''.join(frames))

        # Convertir a MP3 directamente
        audio_wav = AudioSegment.from_wav(nombre_archivo_wav)
        audio_wav.export(nombre_archivo_mp3, format="mp3", bitrate="192k")

        print(f"Audio guardado correctamente en MP3: {nombre_archivo_mp3}")
        return nombre_archivo_mp3

    except Exception as e:
        print(f"Error en la grabación: {e}")
        return None

# **Ejecutar verificaciones y la grabación**
verificar_dispositivos()  # Lista los micrófonos disponibles
grabar_audio()
