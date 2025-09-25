# Inicializar PyAudio
import pyaudio
# Obtener el objeto PyAudio
p = pyaudio.PyAudio()

# Listar dispositivos de audio disponibles
print("Dispositivos de entrada disponibles:")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"ID {i}: {info['name']} - Entrada: {info['maxInputChannels']} canales")

p.terminate()