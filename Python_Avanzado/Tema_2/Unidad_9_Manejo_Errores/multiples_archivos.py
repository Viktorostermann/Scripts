# -*- coding: utf-8 -*-
import os
print("")

def contar_palabras(filename):
    if not os.path.isfile(filename):
        print(f"[ERR] El archivo '{filename}' no existe.\n")
        return False

    try:
        with open(filename, encoding='utf-8', mode='r') as f:
            contenido = f.read()
    except Exception as e:
        print(f"\n[ERR] No se pudo leer el archivo '{filename}': {e}\n")
        return False

    palabras = contenido.split()
    num_palabras = len(palabras)
    print(f"\n[OK] El archivo '{filename}' contiene aproximadamente {num_palabras} palabras:")
    print(palabras)
    print("")
    return True

# 🧩 Lista de archivos internos
archivos_predeterminados = [
    'alice.txt',
    'siddhartha.txt',
    'moby_dick.txt',
    'little_women.txt',
    'metamorphosis.txt'
]

# 🔍 Intentar abrir archivos internos
encontrado = False
for archivo in archivos_predeterminados:
    print(f"[BUS] Buscando archivo interno: {archivo}")
    if contar_palabras(archivo):
        encontrado = True
        print("[OK] Archivo interno encontrado y abierto correctamente.")
        break  # Salir si se encuentra un archivo válido

# ❌ Si no se encontró ninguno, ofrecer búsqueda manual
if not encontrado:
    print("")
    print("[WARN] No se encontró ningún archivo interno válido.\n")
    respuesta = input("¿Desea intentar abrir otro archivo con extensión .txt? (S/N): ").strip().upper()
    print("")
    if respuesta == "S":
        nuevo_archivo = input("Ingrese el nombre del archivo con extensión .txt que desea abrir: ").strip()
        contar_palabras(nuevo_archivo)
    else:
        print("")
        print("\nGracias por su visita, hasta pronto!\n")
        print("")
contar_palabras
