import cv2
import numpy as np
import os
import time
import mss


def capturar_guardar_si_cambia(ruta, nombre_base, intervalo=1):
    # Verifica si la carpeta existe; si no, la crea
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Se ha creado la carpeta: {ruta}")

    ultima_imagen = None
    contador = 1

    while True:
        # Captura la pantalla completa usando MSS
        with mss.mss() as captura:
            frame = np.array(captura.grab(captura.monitors[0]))
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Convierte a formato RGB

        # Convierte la imagen actual a escala de grises para comparación
        imagen_actual = cv2.cvtColor(frame_rgb, cv2.COLOR_BGR2GRAY)

        # Compara con la última imagen capturada
        if ultima_imagen is None or not np.array_equal(ultima_imagen, imagen_actual):
            # Guarda la nueva imagen si hay un cambio
            ruta_completa = os.path.join(ruta, f"{nombre_base}_{contador}.png")
            cv2.imwrite(ruta_completa, frame_rgb)
            print(f"Cambio detectado. Imagen guardada en: {ruta_completa}")
            contador += 1

        # Actualiza la última imagen
        ultima_imagen = imagen_actual

        # Espera antes de la próxima captura
        time.sleep(intervalo)

# Ejemplo de uso:
ruta = "C:\\Users\\vikto\\Pictures\\VsCode_Screen_Shots"
nombre_base = "captura_evento_opencv"
capturar_guardar_si_cambia(ruta, nombre_base, intervalo=1)
