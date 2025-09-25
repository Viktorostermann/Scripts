import mss
import os

def capturar_guardar(ruta, nombre):
    # Verifica si la carpeta existe; si no, la crea
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Se ha creado la carpeta: {ruta}")

    # Usa mss para capturar la pantalla
    with mss.mss() as captura:
        ruta_completa = os.path.join(ruta, f"{nombre}.png")
        imagen = captura.shot(output=ruta_completa)
        print(f"Imagen guardada en: {ruta_completa}")

# Ejemplo de uso:
ruta = "C:\\Users\\vikto\\Pictures\\VsCode_Screen_Shots"
nombre = "captura_mss_mejorada_2"
capturar_guardar(ruta, nombre)
