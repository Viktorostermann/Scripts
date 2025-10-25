'''
Revisa los ejercicios del modulo “Python para Principiantes”. 
¿Hay algún ejercicio que pudiese dividirse en funciones? 
¿Y alguno que podría optimizarse usando bloques try-except? 
Si es así reescríbelos usando estas estructuras.
'''

import os

# 📁 ACR: BASE_DIR (Absolute Current Route)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CLAVES = "claves.txt"

# 🔐 FUN: Enmascarar tarjeta
def enmascarar_tarjeta(numero):
    '''Convierte todos los caracteres en asteriscos, conservando espacios o guiones.'''
    return ''.join('*' if c.isdigit() else c for c in numero)

# 🔍 FUN: Buscar tarjeta en archivo
def buscar_tarjeta_en_archivo(ruta_archivo, tarjeta):
    '''Busca la tarjeta en el archivo y devuelve el número de ocurrencias.'''
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            contenido = file.read()
        return contenido.count(tarjeta)
    except FileNotFoundError:
        print(f"[ERR] No se encontró el archivo '{ruta_archivo}'.")
        return None
    except Exception as e:
        print(f"[ERR] Error al leer '{ruta_archivo}': {e}")
        return None

# 🧾 FUN: Validar formato básico
def validar_tarjeta(tarjeta):
    '''Valida que la tarjeta tenga 16 dígitos y separadores válidos.'''
    limpia = ''.join(filter(str.isdigit, tarjeta))
    return len(limpia) == 16

# 🚀 MAIN: Flujo principal
def main():
    tarjeta = input("🔐 Ingresa el número de tarjeta de crédito: ").strip()
    
    if not validar_tarjeta(tarjeta):
        print("[ERR] Formato inválido. Asegúrate de ingresar 16 dígitos.")
        return

    ruta = os.path.join(BASE_DIR, ARCHIVO_CLAVES)
    ocurrencias = buscar_tarjeta_en_archivo(ruta, tarjeta)

    if ocurrencias is not None:
        print(f"[OK] Tarjeta encontrada {ocurrencias} veces en '{ARCHIVO_CLAVES}'.")
        print(f"[VIS] Tarjeta enmascarada: {enmascarar_tarjeta(tarjeta)}")
    else:
        print("[WARN] No se pudo verificar la tarjeta.")

if __name__ == "__main__":
    main()
