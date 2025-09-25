import subprocess
import os

exe_path = os.path.join("dist", "Proyecto_Texto_a_Voz.exe")

if not os.path.exists(exe_path):
    print(f"[ERROR] No se encontró el ejecutable en: {exe_path}")
else:
    print(f"[INFO] Ejecutando: {exe_path}")
    subprocess.run([exe_path], shell=True)
