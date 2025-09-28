#!/bin/bash
# [VFT-VSCODE] Validación de fuente para terminal VSCode
# Acrónimo: VFT-VSCODE

LOG="$HOME/build.log"
FUENTE_OBJETIVO="Hack Nerd Font Mono"
FUENTE_FALLBACK="MesloLGS NF Regular"

{
echo "[VFT-VSCODE] Iniciando validación de fuente para terminal VSCode..."

if fc-list | grep -q "$FUENTE_OBJETIVO"; then
    echo "[VFT-VSCODE] Fuente detectada: $FUENTE_OBJETIVO ✔️"
    echo "[VFT-VSCODE] Aplicando configuración recomendada..."
    ICONOS=$(echo -e "\u2764 \u263A \u26A1 \uF09B")
    echo "[VFT-VSCODE] Prueba de íconos: $ICONOS"
else
    echo "[VFT-VSCODE] Fuente no detectada ❌ → Activando fallback: $FUENTE_FALLBACK"
    gsettings set org.gnome.desktop.interface monospace-font-name "$FUENTE_FALLBACK 12"
fi

echo "[VFT-VSCODE] Validación completada ✅"
} | tee -a "$LOG"
