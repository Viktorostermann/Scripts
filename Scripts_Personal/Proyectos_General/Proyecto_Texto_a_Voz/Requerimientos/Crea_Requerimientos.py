''' # 🧪 Ejecución: 

Desde tu terminal en VSCode:

bash: python generar_log_requerimientos.py '''

import os
from datetime import datetime

# 📁 Ruta base: carpeta donde está el script
script_dir = os.path.dirname(os.path.abspath(__file__))
CARPETA_LOGS = os.path.join(script_dir, "Logs_GUI", "Requerimientos")

# 📄 Archivos
ARCHIVO_TXT = os.path.join(CARPETA_LOGS, "requirements.txt")
ARCHIVO_HTML = os.path.join(CARPETA_LOGS, "requerimientos.html")

# 📂 Asegura carpeta
os.makedirs(CARPETA_LOGS, exist_ok=True)

# 📦 Verifica existencia de TXT
if not os.path.exists(ARCHIVO_TXT):
    print("❌ No se encontró requirements.txt")
    exit()
else:
    print("✅ Se encontró requirements.txt")

# 📖 Lee requerimientos
with open(ARCHIVO_TXT, "r") as f:
    lineas = [line.strip() for line in f if line.strip()]

# 🧾 Genera HTML
html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Requerimientos Python</title>
    <style>
        body {{ font-family: Arial; background-color: #f4f4f4; }}
        h1 {{ color: #333; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 8px; border: 1px solid #ccc; text-align: left; }}
        th {{ background-color: #444; color: white; }}
        tr:nth-child(even) {{ background-color: #eee; }}
    </style>
</head>
<body>
    <h1>📦 Requerimientos del entorno</h1>
    <p>Generado: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p>Total de paquetes: <strong>{len(lineas)}</strong></p>
    <table>
        <tr><th>#</th><th>Paquete</th><th>Versión</th></tr>
"""

for i, linea in enumerate(lineas, 1):
    if "==" in linea:
        pkg, ver = linea.split("==")
    else:
        pkg, ver = linea, "?"
    html += f"<tr><td>{i}</td><td>{pkg}</td><td>{ver}</td></tr>\n"

html += """
    </table>
</body>
</html>
"""

# 💾 Guarda HTML
with open(ARCHIVO_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Log HTML generado en: {ARCHIVO_HTML}")
