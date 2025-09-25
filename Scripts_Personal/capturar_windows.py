import subprocess
import time
import os
from datetime import datetime

# Ruta donde se guardará la captura en WSL
ruta_carpeta = "/mnt/c/Capturas"
ruta_archivo = os.path.join(ruta_carpeta, "captura_prueba.png")

def llamar_captura():
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(f"📂 Carpeta creada: {ruta_carpeta}")

    print("🚀 Ejecutando captura con scrot en WSL...")
    resultado = subprocess.run(
        f"scrot {ruta_archivo}",
        shell=True,
        capture_output=True,
        text=True
    )
    print(resultado.stdout)
    if resultado.returncode != 0:
        print("❌ Error al ejecutar captura:")
        print(resultado.stderr)
        return False
    return True

def esperar_imagen(max_wait=10):
    print(f"⏳ Esperando a que se cree la imagen en {ruta_archivo} ...")
    tiempo_esperado = 0
    while tiempo_esperado < max_wait:
        if os.path.isfile(ruta_archivo):
            print(f"✅ Imagen encontrada: {ruta_archivo}")
            return True
        time.sleep(1)
        tiempo_esperado += 1
    print("❌ No se encontró ninguna imagen en el tiempo esperado.")
    return False

def procesar_imagen():
    mod_time = os.path.getmtime(ruta_archivo)
    mod_dt = datetime.fromtimestamp(mod_time)
    print(f"📅 Fecha de última modificación: {mod_dt}")

if __name__ == "__main__":
    if llamar_captura():
        if esperar_imagen():
            procesar_imagen()
        else:
            print("❌ No se pudo encontrar la imagen.")
    else:
        print("❌ No se pudo realizar la captura.")