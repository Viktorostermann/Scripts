from PIL import ImageGrab
import os

# Ruta de la carpeta en Windows (accesible desde WSL)
ruta_carpeta = "/mnt/c/Capturas"
ruta_archivo = os.path.join(ruta_carpeta, "captura_prueba.png")

# Verifica si la carpeta existe, si no, la crea
if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)
    print(f"Carpeta creada: {ruta_carpeta}")

# Captura la pantalla y guarda la imagen
try:
    imagen = ImageGrab.grab()
    imagen.save(ruta_archivo)
    print(f"¡Captura guardada correctamente en: {ruta_archivo}!")
except Exception as e:
    print(f"Error al capturar pantalla: {e}")




