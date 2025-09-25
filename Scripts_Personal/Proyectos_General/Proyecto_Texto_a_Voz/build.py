import os, shutil, subprocess
import sys
import os

EXPECTED_FOLDER = "Proyecto_Texto_a_Voz"
current_folder = os.path.basename(os.getcwd())

if current_folder != EXPECTED_FOLDER:
    print(f"❌ Este script debe ejecutarse desde la carpeta '{EXPECTED_FOLDER}'.")
    sys.exit(1)

# 📍 Ruta base del proyecto
RUTA_PROYECTO = os.path.abspath(os.path.dirname(__file__))
RUTA_DIST = os.path.join(RUTA_PROYECTO, "Proyecto_Texto_a_Voz")  # ✅


# 🧹 Limpieza previa
def limpiar_pycache():
    for carpeta, _, archivos in os.walk(RUTA_PROYECTO):
        for archivo in archivos:
            if archivo.endswith(".pyc"):
                os.remove(os.path.join(carpeta, archivo))
        if "__pycache__" in carpeta:
            shutil.rmtree(carpeta, ignore_errors=True)

# 🏗️ Construcción con PyInstaller
def construir_exe():
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--name", "Extractor_URLs",
        "--distpath", RUTA_DIST,
        "--workpath", os.path.join(RUTA_PROYECTO, "build"),
        "--specpath", os.path.join(RUTA_PROYECTO, "spec"),
        "Main.py"
    ])

# 📁 Copiar carpetas necesarias
def copiar_recursos():
    carpetas = [
        "Archivos",
        os.path.join("Modulo_Reportes_HTML", "Reportes_Imprimir")
    ]
    for carpeta in carpetas:
        origen = os.path.join(RUTA_PROYECTO, carpeta)
        destino = os.path.join(RUTA_DIST, carpeta)
        if os.path.exists(destino):
            shutil.rmtree(destino)
        shutil.copytree(origen, destino)

# 🚀 Ejecutar todo
if __name__ == "__main__":
    print("🧹 Limpiando archivos temporales...")
    limpiar_pycache()
    print("⚙️ Generando ejecutable...")
    construir_exe()
    print("📁 Copiando recursos...")
    copiar_recursos()
    print("✅ Distribución lista en:", RUTA_DIST)

def generar_readme():
    contenido = """🧠 Proyecto: Extractor de Texto a Voz desde URLs
📦 Carpeta: Proyecto_Texto_a_Voz

Este ejecutable permite:
- Validar URLs y extraer contenido confiable
- Convertir texto en audio (.mp3)
- Generar reportes HTML y TXT con pie de auditoría

📁 Estructura de carpetas:
├── Archivos/
│   ├── Audios/       → Audios generados (.mp3)
│   └── Textos/       → Textos extraídos (.txt)
├── Modulo_Reportes_HTML/
│   └── Reportes_Imprimir/ → Reportes HTML y TXT con timestamp

🖥️ Ejecutable:
- Archivo: Extractor_URLs.exe
- Doble clic para iniciar el proceso
- Requiere conexión a internet para validar URLs

🧾 Auditoría:
- Cada ejecución genera reportes con timestamp
- Los archivos se guardan en carpetas fijas y auditables

📌 Recomendaciones:
- No mover el .exe fuera de esta carpeta
- No borrar las carpetas Archivos/ ni Reportes_Imprimir/
"""
    ruta_readme = os.path.join(RUTA_DIST, "README.txt")
    with open(ruta_readme, "w", encoding="utf-8") as f:
        f.write(contenido)

# Agrega esta línea al final del script principal
generar_readme()
