import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from Modulo_Reportes_HTML.Utilidades_Archivos import guardar_en_archivos

def texto_a_voz(nombre, texto):
    try:
        mp3_path = f"{nombre}_article.mp3"
        speech = gTTS(texto, lang="en", slow=False)
        temp_path = f"temp_{nombre}.mp3"
        speech.save(temp_path)

        final_path = guardar_en_archivos(nombre + "_article", open(temp_path, "rb").read(), ".mp3")
        os.remove(temp_path)

        return final_path, None
    except Exception as e:
        print(f"[AUDIO ERROR] {nombre}: {type(e).__name__} - {e}")
        return None, f"[{nombre}] Error: {e}"
    
    except Exception as e:
        print(f"[AUDIO ERROR] {nombre}: {type(e).__name__} - {e}")
        return None, f"[{nombre}] Error: {e}"
