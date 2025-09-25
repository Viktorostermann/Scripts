import os
import webbrowser
from datetime import datetime
from Modulo_Reportes_HTML.Utilidades_Archivos import guardar_en_archivos as guardar_html

print("[DEBUG] Reporte_HTML.py cargado correctamente")


# 📁 Carpeta fija para reportes
RUTA_REPORTES = os.path.join(os.path.dirname(__file__), "Reportes_Imprimir")

def generar_nombre_reporte(base="reporte"):
    """
    Genera un nombre de archivo con timestamp para trazabilidad.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{base}_{timestamp}"

def generar_reporte_html(nombres, textos, mp3s, errores):
    """
    Genera un reporte HTML visual con resumen estadístico, detalle por fuente y pie de auditoría.
    """
    assert len(nombres) == len(textos) == len(mp3s) == len(errores), "[ERROR] Listas desalineadas"

    total     = len(nombres)
    exitosos  = sum(1 for e in errores if not e)
    fallidos  = total - exitosos
    audios    = sum(1 for m in mp3s if m)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = "<html><head><meta charset='utf-8'><title>Reporte</title>"
    html += """
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            padding: 30px;
            background: #f0f4f8;
            line-height: 1.6;
        }
        h1, h2 {
            color: #333;
        }
        .ok { color: green; }
        .error { color: red; }
        .critico {
            font-weight: bold;
            background: #ffe6e6;
            border-left: 6px solid red;
            padding: 10px;
            margin-top: 10px;
            border-radius: 6px;
        }
        .bloque {
            margin-bottom: 40px;
            padding: 20px;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            border-left: 4px solid #ccc;
        }
        .bloque h2 {
            margin-top: 0;
        }
        .resumen {
            background: #e0ecff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 40px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        .resumen ul {
            padding-left: 20px;
        }
        .resumen li {
            margin-bottom: 8px;
        }
        em {
            color: #666;
        }
        a {
            color: #007acc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        footer {
            margin-top: 60px;
            font-size: 0.9em;
            color: #555;
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid #ccc;
        }
        code {
            background: #eee;
            padding: 2px 6px;
            border-radius: 4px;
        }
    </style>
    </head><body>
    """

    html += "<h1>📊 Reporte de Artículos</h1>"

    # 🧮 Resumen estadístico
    html += "<div class='resumen'>"
    html += "<h2>📈 Resumen General</h2><ul>"
    html += f"<li>🔹 Total fuentes procesadas: <strong>{total}</strong></li>"
    html += f"<li>✅ Procesadas con éxito: <strong class='ok'>{exitosos}</strong></li>"
    html += f"<li>❌ Con errores: <strong class='error'>{fallidos}</strong></li>"
    html += f"<li>🔊 Audios generados: <strong>{audios}</strong></li>"
    html += "</ul></div>"

    # 🔍 Detalle por fuente
    for i, nombre in enumerate(nombres):
        html += "<div class='bloque'>"
        html += f"<h2>🔹 Fuente: <strong>{nombre}</strong></h2>"

        if errores[i]:
            clase_error = "critico" if "inaccesible" in errores[i].lower() else "error"
            html += f"<div class='{clase_error}'>⚠️ <strong>Error:</strong> {errores[i]}</div>"
        else:
            html += "<p class='ok'>✅ Procesado correctamente</p>"

        if textos[i]:
            resumen = textos[i][:500].replace("\n", "<br>")
            html += f"<p><strong>📝 Fragmento:</strong><br>{resumen}...</p>"
        else:
            html += "<p><em>No se extrajo texto.</em></p>"

        if mp3s[i]:
            html += f"<p>🔊 <a href='../{mp3s[i]}' target='_blank'>Escuchar MP3</a></p>"
        else:
            html += "<p><em>No se generó audio.</em></p>"

        html += "</div>"

    # 🧾 Pie de auditoría
    nombre_reporte = generar_nombre_reporte()
    ruta_relativa  = os.path.join("Reportes_Imprimir", f"{nombre_reporte}.html")
    html += f"<footer>🕒 Generado el {timestamp} | 📁 Ruta: <code>{ruta_relativa}</code> | ⚙️ Script: <code>Main.py</code></footer>"

    html += "</body></html>"

    # 💾 Guardar y abrir
    ruta = guardar_html(nombre_reporte, html, ".html", carpeta=RUTA_REPORTES)
    print(f"\n📁 Reporte generado: {ruta}")
    webbrowser.open(ruta)

    

def imprimir_resumen(nombres, textos, mp3s, errores):
    """
    Imprime resumen estadístico y detalle técnico en consola.
    También guarda el resumen en un archivo .txt para auditoría y lo abre automáticamente.
    """
    total    = len(nombres)
    exitosos = sum(1 for e in errores if not e)
    fallidos = total - exitosos
    audios   = sum(1 for m in mp3s if m)

    resumen_txt = []
    resumen_txt.append("📋 Resumen:")
    resumen_txt.append("────────────────────────────────────────────")
    resumen_txt.append(f"🔹 Total fuentes procesadas: {total}")
    resumen_txt.append(f"✅ Procesadas con éxito:     {exitosos}")
    resumen_txt.append(f"❌ Con errores:              {fallidos}")
    resumen_txt.append(f"🔊 Audios generados:         {audios}")
    resumen_txt.append("────────────────────────────────────────────\n")

    # 🔊 Archivos MP3 generados
    resumen_txt.append("🔊 Archivos MP3 generados:")
    for i, mp3 in enumerate(mp3s):
        if mp3:
            resumen_txt.append(f"  - {nombres[i]} → {mp3}")
    resumen_txt.append("")

    # 📝 Artículos con texto extraído
    resumen_txt.append("📝 Artículos con texto extraído:")
    for i, texto in enumerate(textos):
        if texto:
            resumen = texto[:80].replace("\n", " ").strip()
            resumen_txt.append(f"  - {nombres[i]} → \"{resumen}...\"")
    resumen_txt.append("")

    # ⚠️ URLs con error
    resumen_txt.append("⚠️ URLs con error:")
    for i, error in enumerate(errores):
        if error:
            resumen_txt.append(f"  - {nombres[i]} → {error}")
    resumen_txt.append("")

    # 📤 Imprimir en consola
    print("\n".join(resumen_txt))

    # 💾 Guardar en archivo .txt
    nombre_txt = generar_nombre_reporte("resumen_consola")
    contenido  = "\n".join(resumen_txt)
    ruta       = guardar_html(nombre_txt, contenido, ".txt", carpeta=RUTA_REPORTES)
    print(f"\n📝 Resumen guardado en: {ruta}")

    # 🪟 Abrir automáticamente en Windows
    try:
        os.startfile(ruta)
    except Exception as e:
        print(f"[WARN] No se pudo abrir el archivo automáticamente: {e}")
