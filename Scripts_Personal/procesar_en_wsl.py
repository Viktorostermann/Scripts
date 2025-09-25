import subprocess
import time
import os
from datetime import datetime

# Ruta al ejecutable Python Windows
python_windows = r"C:\Users\vikto\AppData\Local\Programs\Python\Python310\python.exe"
# Ruta al script de captura en Windows
script_captura = r"C:\Users\vikto\Documents\wsl_scripts\capturar_windows.py"

# Carpeta destino y ruta imagen en formato Windows para evitar problemas
carpeta_capturas = r"C:\Users\vikto\Documents\Capturas_WSL"
nombre_imagen = "imagen_actual.png"
ruta_imagen = os.path.join(carpeta_capturas, nombre_imagen)

def llamar_captura():
    print("🚀 Ejecutando captura con Python Windows...")
    resultado = subprocess.run(
        ["/mnt/c/Users/vikto/AppData/Local/Programs/Python/Python310/python.exe", 
         "/mnt/c/Users/vikto/Documents/wsl_scripts/capturar_windows.py"],
        capture_output=True,
        text=True
    )
    print("🚀 Resultado de la captura:")
    print(resultado.stdout)
    if resultado.returncode != 0:
        print("❌ Error al ejecutar captura:")
        print(resultado.stderr)
        return False
    return True


def esperar_imagen(max_wait=10):
    print(f"⏳ Esperando a que se cree la imagen en {ruta_imagen} ...")
    tiempo_esperado = 0
    while tiempo_esperado < max_wait:
        if os.path.isfile(ruta_imagen):
            print(f"✅ Imagen encontrada: {ruta_imagen}")
            return True
        time.sleep(1)
        tiempo_esperado += 1
    print("❌ No se encontró ninguna imagen en el tiempo esperado.")
    return False

def procesar_imagen():
    mod_time = os.path.getmtime(ruta_imagen)
    mod_dt = datetime.fromtimestamp(mod_time)
    print(f"Fecha de última modificación: {mod_dt}")

if __name__ == "__main__":
    if llamar_captura():
        if esperar_imagen():
            procesar_imagen()
        else:
            print("❌ No se pudo encontrar la imagen.")
    else:
        print("❌ No se pudo ejecutar la captura.")
#Scripts_Personal/capturar_windows.py