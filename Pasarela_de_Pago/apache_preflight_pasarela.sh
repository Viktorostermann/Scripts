# A.L.V.A. – Apache License Validation Automática para pasarela.py
echo "[A.L.V.A.] Validando licencia Apache en pasarela.py..." >> build.log

SCRIPT_PATH="./pasarela.py"
LICENSE_PATTERN="Licensed under the Apache License, Version 2.0"
CURRENT_YEAR=$(date +%Y)
AUTHOR="Viktore"

# Verificar si el aviso ya está presente
if grep -q "$LICENSE_PATTERN" "$SCRIPT_PATH"; then
    echo "[A.L.V.A.] ✔ Licencia Apache detectada en pasarela.py." >> build.log
else
    echo "[A.L.V.A.] ⚠ Licencia Apache NO detectada. Insertando aviso estándar..." >> build.log

    sed -i "1i# Copyright $CURRENT_YEAR $AUTHOR\n# Licensed under the Apache License, Version 2.0 (http://www.apache.org/licenses/LICENSE-2.0)\n# Distributed on an \"AS IS\" basis, without warranties or conditions of any kind.\n" "$SCRIPT_PATH"

    echo "[A.L.V.A.] ➕ Aviso insertado en pasarela.py." >> build.log
fi
