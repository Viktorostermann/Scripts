'''
Configurar el entorno de desarrollo: 
Antes de comenzar a desarrollar juegos simples en Python
es importante configurar tu entorno de desarrollo. 
segúrate de tener Python instalado en tu ordenador 
y luego instala la biblioteca Pygame utilizando pip: pip install pygame

🧱 instalador_librerias.py — con soporte para rutas personalizadas (--target) y dry-run técnico
'''

import argparse
import subprocess
import logging
import json
import sys
from pathlib import Path

# 📦 Carga lista de librerías desde archivo .txt o .json
def cargar_librerias_desde_archivo(ruta_archivo):
    ruta = Path(ruta_archivo)

    if not ruta.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")

    if ruta.suffix == ".json":
        with open(ruta) as f:
            pkgs = json.load(f)
    else:
        with open(ruta) as f:
            pkgs = [line.strip() for line in f if line.strip()]

    return list(set(pkgs))  # Elimina duplicados


# 🛠 Instalación defensiva de paquetes, compatible con --target y dry-run
def instalar_paquete(pkg, dry_run=False, target=None):
    comando = [sys.executable, "-m", "pip", "install", pkg]

    # 📍 Añadir ubicación personalizada si se especifica
    if target:
        comando.extend(["--target", str(target)])

    if dry_run:
        logging.info(f"[dry-run] Simulado: {' '.join(comando)}")
        return

    try:
        result = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            logging.info(f"[ok] '{pkg}' instalado correctamente")
        else:
            logging.warning(f"[error] '{pkg}' falló: {result.stderr.strip()}")

    except Exception as e:
        logging.error(f"[except] Error inesperado con '{pkg}': {e}")


# 🚪 Punto de entrada principal
def main():
    parser = argparse.ArgumentParser(description="Instalador batch de librerías")
    parser.add_argument("--pkgs", type=str, help="Lista de paquetes separados por espacio")
    parser.add_argument("--file", type=str, help="Archivo .txt o .json con paquetes")
    parser.add_argument("--target", type=str, help="Ruta personalizada para instalación (--target de pip)")
    parser.add_argument("--dry-run", action="store_true", help="Simula sin instalar")
    parser.add_argument("--log", type=str, default="logs/install.log", help="Ruta del log técnico")
    args = parser.parse_args()

    # 📁 Asegura carpeta del log
    Path(args.log).parent.mkdir(parents=True, exist_ok=True)

    # 🧾 Inicializa logging técnico
    logging.basicConfig(filename=args.log, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    logging.info("=== INICIO DE EJECUCIÓN ===")

    paquetes = []

    # ✳️ Desde línea de comandos
    if args.pkgs:
        paquetes.extend(args.pkgs.strip().split())

    # 📂 Desde archivo externo
    if args.file:
        try:
            paquetes.extend(cargar_librerias_desde_archivo(args.file))
        except Exception as e:
            logging.error(f"Error leyendo archivo: {e}")
            print(f"❌ Error procesando archivo: {e}")
            sys.exit(1)

    # 🧹 Elimina duplicados
    paquetes = list(set(paquetes))

    if not paquetes:
        logging.warning("No se especificaron paquetes")
        print("⚠️ No se encontraron paquetes para instalar.")
        sys.exit(0)

    # 📍 Validación defensiva de ruta personalizada (si se usa --target)
    if args.target:
        target_path = Path(args.target)
        target_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"[setup] Ruta de instalación verificada: {target_path}")

    # 🚀 Instalación por lote
    for pkg in paquetes:
        instalar_paquete(pkg, dry_run=args.dry_run, target=args.target)

    logging.info("=== FIN DE EJECUCIÓN ===")

if __name__ == "__main__":
    main()

'''
🧪 Ejemplos de ejecución
Modo: Comando de ejemplo
CLI directa	python instalador_librerias.py --pkgs "numpy pandas flask"
Desde archivo	python instalador_librerias.py --file "./conf/librerias.txt"
Instalación local	python instalador_librerias.py --file librerias.txt --target "./envs/libs_local"
Simulación dry-run	python instalador_librerias.py --pkgs "requests" --dry-run
'''