import os
from datetime import datetime

# 📍 Ruta raíz del proyecto (donde está Main.py)
RUTA_PROYECTO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 📁 Rutas fijas para guardar archivos
RUTA_AUDIOS = os.path.join(RUTA_PROYECTO, "Archivos", "Audios")
RUTA_TEXTOS = os.path.join(RUTA_PROYECTO, "Archivos", "Textos")

# 🛡️ Crear carpetas si no existen
os.makedirs(RUTA_AUDIOS, exist_ok=True)
os.makedirs(RUTA_TEXTOS, exist_ok=True)

def guardar_en_archivos(nombre_base, contenido, extension, script_origen="Desconocido", carpeta=None):
    """
    Guarda contenido en carpeta según tipo (.txt → Textos, .mp3 → Audios).
    Agrega pie de auditoría en archivos de texto. Retorna ruta absoluta.
    """
    # 📁 Carpeta destino
    if carpeta is None:
        carpeta = RUTA_AUDIOS if extension == ".mp3" else RUTA_TEXTOS

    modo = "wb" if extension == ".mp3" else "w"
    os.makedirs(carpeta, exist_ok=True)
    ruta_completa = os.path.abspath(os.path.join(carpeta, f"{nombre_base}{extension}"))

    # 🧾 Pie de auditoría para texto
    if modo == "w":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if extension == ".html":
            pie_auditoria = f'''
<footer style="margin-top:2em; padding:1em; background:#f0f0f0; font-size:0.9em; border-top:1px solid #ccc;">
  <strong>🧾 Auditoría técnica</strong><br>
  📅 Fecha: {timestamp}<br>
  📄 Script generador: {script_origen}<br>
  📁 Ruta: {ruta_completa}
</footer>
'''
            if "</body>" in contenido:
                contenido = contenido.replace("</body>", pie_auditoria + "\n</body>")
            else:
                contenido += pie_auditoria
        else:
            pie_auditoria = (
                "\n\n---\n"
                f"🧾 Auditoría técnica\n"
                f"📅 Fecha: {timestamp}\n"
                f"📄 Script generador: {script_origen}\n"
                f"📁 Ruta: {ruta_completa}\n"
            )
            contenido += pie_auditoria

    with open(ruta_completa, modo, encoding=None if modo == "wb" else "utf-8") as f:
        f.write(contenido)

    print(f"✅ Archivo guardado en: {ruta_completa}")
    return ruta_completa
