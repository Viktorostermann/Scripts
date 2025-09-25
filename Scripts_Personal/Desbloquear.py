import subprocess


def desbloquear_archivo(ruta_windows):
    # Comando PowerShell para desbloquear archivo
    comando = f'Unblock-File -Path "{ruta_windows}"'

    # Ejecutar PowerShell desde WSL/bash
    resultado = subprocess.run(
        ["powershell.exe", "-Command", comando],
        capture_output=True,
        text=True
    )
    # Verificar si el comando se ejecutó correctamente
    if resultado.returncode == 0:
        print(f"✅ Archivo desbloqueado: {ruta_windows}")
    else:
        print(f"❌ Error al desbloquear archivo:\n{resultado.stderr}")

if __name__ == "__main__":
    ruta = r"C:\Users\vikto\Documents\wsl_scripts\capturar_windows.py"
    desbloquear_archivo(ruta)
