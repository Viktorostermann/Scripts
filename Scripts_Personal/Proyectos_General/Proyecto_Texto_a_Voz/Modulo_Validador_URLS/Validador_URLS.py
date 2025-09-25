import requests
from newspaper import Article
from newspaper.article import ArticleException

# 🔐 Sesión HTTP con headers y cookies
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "es-ES,es;q=0.9",
})
# Puedes agregar cookies específicas si el sitio lo requiere
# session.cookies.set("cookie_name", "valor_cookie")

# ✅ Validación defensiva de URL
def url_valida(url):
    try:
        response = session.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200
    except Exception as e:
        print(f"[VALIDACIÓN URL] Error: {e}")
        return False

# 📰 Extracción de artículo con trazabilidad
def extraer_articulo(nombre, url):
    print(f"\n🔍 Procesando fuente: {nombre} → {url}")
    try:
        # newspaper3k no acepta sesión directamente, así que descargamos manualmente
        response = session.get(url, timeout=10)
        if response.status_code != 200:
            raise ArticleException(f"Status code: {response.status_code}")

        article = Article(url)
        article.set_html(response.text)
        article.parse()

        title = article.title or "[Sin título]"
        text  = article.text or "[Sin contenido]"

        print(f"📌 Título: {title}")
        print(f"📝 Texto (primeros 500 caracteres):\n{text[:500]}")
        return text, None

    except ArticleException as e:
        print(f"[ERROR] No se pudo descargar/parsing: {e}")
        return None, f"[{nombre}] Error: {e}"

    except Exception as e:
        print(f"[ERROR] Fallo inesperado: {e}")
        return None, f"[{nombre}] Error inesperado: {e}"
