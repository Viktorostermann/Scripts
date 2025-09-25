#!/bin/bash

# === CONFIGURACIÓN ===

# Ruta al script de captura en WSL
SCRIPT_WSL="/home/vikto/Python_VsCode/Scripts_Personal/capturar_windows.py"

# Carpeta en Windows donde se ejecutará
TEMP_WIN_DIR="/mnt/c/Users/vikto/Documents/wsl_scripts"
TEMP_WIN_SCRIPT="$TEMP_WIN_DIR/capturar_windows.py"

# Imagen esperada en Windows
IMAGEN="/mnt/c/Users/vikto/Pictures/Capturas/imagen_actual.png"
TIEMPO_ESPERA=1

# === INICIO DEL SCRIPT ===

# Crear carpeta temporal en Windows
mkdir -p "$TEMP_WIN_DIR"

# Verificar que existe el script en WSL
if [ ! -f "$SCRIPT_WSL" ]; then
    echo "❌ Error: no se encontró $SCRIPT_WSL"
    exit 1
fi

# Copiar script Python desde WSL a Windows
cp "$SCRIPT_WSL" "$TEMP_WIN_SCRIPT"

# Borrar imagen previa si existe
if [ -f "$IMAGEN" ]; then
    echo "🧹 Borrando imagen anterior..."
    rm "$IMAGEN"
fi

# Ejecutar script desde Python de Windows
echo "🚀 Ejecutando captura en Windows..."
/mnt/c/Users/vikto/AppData/Local/Programs/Python/Python310/python.exe "$TEMP_WIN_SCRIPT" &

# Esperar a que se cree la imagen
echo "⏳ Esperando a que se cree la imagen..."
while [ ! -f "$IMAGEN" ]; do
    sleep $TIEMPO_ESPERA
done

echo "✅ Imagen creada. Procesando desde WSL..."

# Activar entorno virtual y ejecutar procesamiento
source /home/vikto/Python_VsCode/.venv/bin/activate
python3 /home/vikto/Python_VsCode/Scripts_Personal/procesar_en_wsl.py
