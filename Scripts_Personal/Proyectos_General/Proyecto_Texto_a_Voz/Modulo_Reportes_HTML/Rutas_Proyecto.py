import os

# 📍 Ruta raíz del proyecto
RUTA_PROYECTO = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))

# 📁 Carpetas fijas
RUTA_ARCHIVOS = os.path.join(RUTA_PROYECTO, "Archivos")
RUTA_AUDIOS   = os.path.join(RUTA_ARCHIVOS, "Audios")
RUTA_TEXTOS   = os.path.join(RUTA_ARCHIVOS, "Textos")
RUTA_REPORTES = os.path.join(RUTA_ARCHIVOS, "Reportes")  # opcional

# 🧪 Validación defensiva
for carpeta in [RUTA_AUDIOS, RUTA_TEXTOS, RUTA_REPORTES]:
    os.makedirs(carpeta, exist_ok=True)
