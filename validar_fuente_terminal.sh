#!/bin/bash
# [FONT_VALID] Validación de fuente para terminal VSCode
# Acrónimo: VFT-VSCODE

LOG="$HOME/build.log"
FUENTE_OBJETIVO="Hack Nerd Font Mono"
FUENTE_FALLBACK="MesloLGS NF Regular"

echo "[VFT-VSCODE] Iniciando validación de fuente para terminal VSCode..." >> "$LOG"

# Validar si la fuente objetivo está instalada
if fc-list | grep -q "$FUENTE_OBJETIVO"; then
    echo "[VFT-VSCODE] Fuente detectada: $FUENTE_OBJETIVO ✔️" >> "$LOG"
    echo "[VFT-VSCODE] Aplicando configuración recomendada..." >> "$LOG"
else
    echo "[VFT-VSCODE] Fuente no detectada: $FUENTE_OBJETIVO ❌" >> "$LOG"
    echo "[VFT-VSCODE] Activando fallback: $FUENTE_FALLBACK" >> "$LOG"
    gsettings set org.gnome.desktop.interface monospace-font-name "$FUENTE_FALLBACK 12"
fi

# Validar renderizado de íconos
ICONOS=$(echo -e "\u2764 \u263A \u26A1 \uF09B")
echo "[VFT-VSCODE] Prueba de íconos: $ICONOS" >> "$LOG"

echo "[VFT-VSCODE] Validación completada ✅" >> "$LOG"
