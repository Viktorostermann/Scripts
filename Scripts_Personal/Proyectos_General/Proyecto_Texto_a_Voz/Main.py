import requests
import sys, os
from Modulo_Validador_URLS.Validador_URLS import extraer_articulo
from Modulo_Texto_a_Voz.Texto_a_Voz import texto_a_voz
from Modulo_Reportes_HTML.Utilidades_Archivos import guardar_en_archivos as guardar_html
from Modulo_Reportes_HTML.Reporte_HTML import imprimir_resumen, generar_reporte_html

# 📍 Ruta raíz del proyecto
RUTA_PROYECTO = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, RUTA_PROYECTO)

# 👇 Ahora los imports funcionarán
from Modulo_Texto_a_Voz.Texto_a_Voz import texto_a_voz

# ✅ Validación defensiva de URL
def url_valida(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except Exception as e:
        print(f"[VALIDACIÓN URL] Error: {e}")
        return False

# 🌐 Diccionario de fuentes
urls = {
    "Nasa":       "https://www.npr.org/2023/09/01/1196631583/new-mars-images-from-nasa", 
    "BBC":        "https://www.bbc.com/news/world-us-canada-66376930",
    "CNN":        "https://edition.cnn.com/2024/06/10/tech/apple-wwdc-ai-announcements/index.html",
    "Nature":     "https://www.nature.com/articles/d41586-024-01885-1",
    "Reuters":    "https://www.reuters.com/world/us/us-supreme-court-rules-trump-has-some-immunity-2024-07-01/",
    "TechCrunch": "https://techcrunch.com/2024/07/01/apple-ai-announcements-wwdc/",
    "NationalGeographic" : "https://www.nationalgeographic.com/",
    "ScientificAmerican":  "https://www.scientificamerican.com/article/how-ai-is-changing-scientific-research/",
}

# 📦 Inicialización de listas
nombres   = list(urls.keys())
textos    = []
errores   = []
mp3s      = []

# 🔄 Procesamiento por fuente
for nombre in nombres:
    url = urls[nombre]

    if not url_valida(url):
        print(f"[SKIP] URL inválida o inaccesible: {url}")
        textos.append(None)
        errores.append("URL inválida o inaccesible")
        mp3s.append(None)
        continue

    texto, error = extraer_articulo(nombre, url)
    textos.append(texto)
    errores.append(error)

    if texto:
        mp3, err_audio = texto_a_voz(nombre, texto)
        mp3s.append(mp3)
        if err_audio:
            errores[-1] = err_audio
    else:
        mp3s.append(None)

# 📋 Resumen en consola
imprimir_resumen(nombres, textos, mp3s, errores)

# 🧾 Generación de reporte HTML
generar_reporte_html(nombres, textos, mp3s, errores)
