# P.A.G.O. – Postflight de Aplicación con Gestión de Operaciones
echo "[P.A.G.O.] Iniciando postflight de pasarela.py..." >> build.log

# Validar ejecución exitosa
if python3 pasarela.py > pasarela_output.log 2>&1; then
    echo "[P.A.G.O.] ✔ pasarela.py ejecutado correctamente." >> build.log
else
    echo "[P.A.G.O.] ❌ Error en ejecución de pasarela.py. Revisar pasarela_output.log." >> build.log
    exit 1
fi

# Validar carga de STRIPE_SECRET_KEY
if grep -q "STRIPE_SECRET_KEY cargada" pasarela_output.log; then
    echo "[P.A.G.O.] ✔ Clave STRIPE cargada correctamente." >> build.log
else
    echo "[P.A.G.O.] ⚠ Clave STRIPE no detectada en salida. Validar entorno .env." >> build.log
fi

# Validar respuesta de Stripe (mock o real)
if grep -q "Stripe response:" pasarela_output.log; then
    echo "[P.A.G.O.] ✔ Respuesta de Stripe registrada." >> build.log
else
    echo "[P.A.G.O.] ⚠ No se detectó respuesta de Stripe. Validar conexión o modo sandbox." >> build.log
fi

echo "[P.A.G.O.] Postflight completado para pasarela.py." >> build.log
