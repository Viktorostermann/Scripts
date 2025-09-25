import json
import os

# Definir la ruta específica del archivo JSON
#ruta_especifica = os.path.join("C:\\Users\\vikto\\Documentos", "archivo.json")
ruta_especifica = os.path.join(os.getcwd(), "Archivos_Jason", "archivo.json")

# Verificar si la carpeta existe, si no, crearla
if not os.path.exists(os.path.dirname(ruta_especifica)):
    os.makedirs(os.path.dirname(ruta_especifica))

try:
    # Intentar cargar el contenido del archivo JSON
    with open(ruta_especifica, "r") as f:
        datos = json.load(f)
except FileNotFoundError:
    print(f"El archivo no existe en {ruta_especifica}, creando uno nuevo.")
    datos = {}
except json.JSONDecodeError:
    print(f"Error en el formato del JSON en {ruta_especifica}. Creando un archivo limpio.")
    datos = {}

# Nuevo dato a agregar
nuevo_dato = {"nombre": "Victor", "edad": 25}

# Fusionar datos existentes con el nuevo dato
datos.update(nuevo_dato)

# Guardar los datos actualizados en la ruta específica
with open(ruta_especifica, "w") as f:
    json.dump(datos, f, indent=4)

print(f"Datos guardados correctamente en {ruta_especifica}")
