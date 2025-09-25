import pyaudio
from geolite import GeoLite2

def record_audio(duration=5):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)
    audio_data = []
    for _ in range(0, int(stream.get_sample_rate() * duration)):
        data = stream.read(1024)
        audio_data.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()

    with open("grabado_de_audio.wav", "wb") as file:
        file.write(b''.join(audio_data))

record_audio()

