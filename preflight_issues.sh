#!/usr/bin/env bash
# Preflight Script: Validación de IgnoredSecurityIssues
# Acrónimo: ISSUE-IGN
# Autor: Viktore
# Fecha: $(date +"%Y-%m-%d")

CONFIG_FILE="./amazonq_config.json"
LOG_FILE="./build.log"

echo "[ISSUE-IGN] Preflight iniciado: $(date)" >> "$LOG_FILE"

# Validar existencia del archivo de configuración
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "[ISSUE-IGN] ERROR: No se encontró $CONFIG_FILE" | tee -a "$LOG_FILE"
    exit 1
fi

# Extraer lista de issues ignorados
IGNORED=$(jq -r '.IgnoredSecurityIssues[]?' "$CONFIG_FILE")

if [[ -z "$IGNORED" ]]; then
    echo "[ISSUE-IGN] Advertencia: No hay issues ignorados configurados." | tee -a "$LOG_FILE"
else
    echo "[ISSUE-IGN] Issues ignorados detectados:" | tee -a "$LOG_FILE"
    for issue in $IGNORED; do
        echo "[ISSUE-IGN] $issue → Validado manualmente" | tee -a "$LOG_FILE"
    done
fi

echo "[ISSUE-IGN] Preflight finalizado: $(date)" >> "$LOG_FILE"
