import os
import shutil

def cambiar_extension_y_mover(origen, destino, extension_actual, nueva_extension):
    """
    Cambia la extensión de los archivos dentro de una carpeta y los mueve a otra carpeta.
    
    Parámetros:
    origen (str): Carpeta donde están los archivos originales.
    destino (str): Carpeta destino donde se moverán los archivos.
    extension_actual (str): Extensión actual de los archivos (ejemplo: '.txt').
    nueva_extension (str): Nueva extensión deseada (ejemplo: '.py').
    """
    # Validación preflight: verificar que las carpetas existen
    if not os.path.isdir(origen):
        print(f"❌ La carpeta origen {origen} no existe.")
        return
    if not os.path.isdir(destino):
        print(f"❌ La carpeta destino {destino} no existe.")
        return
    
    for archivo in os.listdir(origen):
        if archivo.endswith(extension_actual):
            ruta_vieja = os.path.join(origen, archivo)
            nombre_base = os.path.splitext(archivo)[0]  # nombre sin extensión
            nuevo_nombre = nombre_base + nueva_extension
            ruta_final = os.path.join(destino, nuevo_nombre)

            # Mover y renombrar en un solo paso
            shutil.move(ruta_vieja, ruta_final)

            print(f"✅ {archivo} → {ruta_final}")

# Ejemplo de uso
if __name__ == "__main__":
    origen = "/home/viktore/Documentos/2-Python/KodLan/M5L2"
    destino = "/home/viktore/Documentos/2-Python/KodLan"
    cambiar_extension_y_mover(origen, destino, ".txt", ".py")
