# Validación de entorno .env
echo "[ENVCHK] Verificando archivo .env y clave STRIPE_SECRET_KEY..." >> build.log

if [ -f .env ]; then
    if grep -q "^STRIPE_SECRET_KEY=" .env; then
        echo "[ENVCHK] ✔ STRIPE_SECRET_KEY detectada en .env." >> build.log
    else
        echo "[ENVCHK] ⚠ STRIPE_SECRET_KEY no encontrada en .env." >> build.log
    fi
else
    echo "[ENVCHK] ⚠ Archivo .env no encontrado." >> build.log
fi
