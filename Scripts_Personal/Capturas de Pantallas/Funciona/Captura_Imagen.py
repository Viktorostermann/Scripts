import os

ruta_carpeta = "/mnt/c/Capturas"
ruta_archivo = os.path.join(ruta_carpeta, "captura_prueba.png")

if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)
    print(f"Carpeta creada: {ruta_carpeta}")

# Ejecuta el comando scrot para capturar la pantalla
os.system(f"scrot {ruta_archivo}")
print(f"¡Captura guardada en: {ruta_archivo}!")
