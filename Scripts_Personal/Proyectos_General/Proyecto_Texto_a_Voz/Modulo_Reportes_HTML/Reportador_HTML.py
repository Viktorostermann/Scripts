# 📁 Modulo_Reportes_HTML/Reportador_HTML.py
import os

def generar_reporte_html(nombre_base, contenido, extension=".html", carpeta=None):
    """
    Guarda el contenido HTML en la carpeta especificada.
    """
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    else:
        carpeta = "."

    ruta_completa = os.path.join(carpeta, f"{nombre_base}{extension}")

    with open(ruta_completa, "w", encoding="utf-8") as f:
        f.write(contenido)

    return ruta_completa