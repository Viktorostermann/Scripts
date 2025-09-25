import mss
import os

def capturar_guardar(ruta, nombre):
    # Usa mss para capturar la pantalla
    with mss.mss() as captura:
        imagen = captura.shot(output=os.path.join(ruta, f"{nombre}.png"))
        print(f"Imagen guardada en: {imagen}")

# Ejemplo de uso:
ruta = "C:\\Users\\vikto\\Pictures\\VsCode_Screen_Shots"  # Cambia esta ruta según tu preferencia
nombre = "El tigere de la selva"  # Cambia el nombre según tu preferencia
capturar_guardar(ruta, nombre)
