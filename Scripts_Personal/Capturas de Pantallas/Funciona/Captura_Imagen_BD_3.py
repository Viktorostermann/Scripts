import os
import mss
import sqlite3
from datetime import datetime

def capturar_guardar(ruta, nombre):
    # Verifica si la carpeta existe; si no, la crea
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        print(f"Se ha creado la carpeta: {ruta}")

    # Usa mss para capturar la pantalla
    with mss.mss() as captura:
        ruta_completa = os.path.join(ruta, f"{nombre}.png")
        imagen = captura.shot(output=ruta_completa)
        print("\n")
        print(f"Imagen guardada en: {ruta_completa}")
        

# Ejemplo de uso:
ruta = "C:\\Users\\vikto\\Pruebas_VsCode\\Pictures\\VsCode_Screen_Shots"
ruta = os.path.normpath(ruta)  # Normaliza la ruta para evitar problemas de formato
# Asegúrate de que la ruta sea válida 
nombre = "Danny Mariposa"
capturar_guardar(ruta, nombre)


# Configurar base de datos
def create_table():
    db = sqlite3.connect("C:\\Users\\vikto\\Pruebas_VsCode\\Datos\\navegacion.db")
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS navegacion
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      url TEXT NOT NULL,
                      timestamp DATETIME NOT NULL)''') # Instruccion en SQL que cambia el nombre de la tabla y los campos según tus necesidades
    db.commit()
    db.close()

 # Función para guardar la navegación
def salva_navegacion(url):
    try:
        db = sqlite3.connect("C:\\Users\\vikto\\Pruebas_VsCode\\Datos\\navegacion.db")
        cursor = db.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO navegacion (url, timestamp) VALUES (?, ?)", (url, timestamp))
        db.commit()
        print("\n")
        print(f"Salvada la navegación: {url}")
    except Exception as e:
        print(f"Error saving navigation: {e}")
    finally:
        db.close()

# Inicializar la base de datos
create_table()

# Ejemplo de uso
salva_navegacion("https://www.ejemplo.com")
print("\n")
# capture_social_media() function is not defined, so this line is removed or commented out.
# capture_social_media()