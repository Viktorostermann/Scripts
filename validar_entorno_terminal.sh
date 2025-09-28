#!/bin/bash
# Validación extendida del entorno de terminal VSCode
# Autor: Viktore + Copilot
# Acrónimos: VFT-VSCODE, VSH-ZSH, THEME-P10K, ENV-VSCODE, FONT-FALLBACK

LOG="$HOME/build.log"
FUENTE_OBJETIVO="Hack Nerd Font Mono"
FUENTE_FALLBACK="MesloLGS NF Regular"

{
echo "[VFT-VSCODE] Iniciando validación de fuente para terminal VSCode..."

if fc-list | grep -q "$FUENTE_OBJETIVO"; then
    echo "[VFT-VSCODE] Fuente detectada: $FUENTE_OBJETIVO ✔️"
    ICONOS=$(echo -e "\u2764 \u263A \u26A1 \uF09B")
    echo "[VFT-VSCODE] Prueba de íconos: $ICONOS"
else
    echo "[VFT-VSCODE] Fuente no detectada ❌"
    echo "[FONT-FALLBACK] Activando fallback: $FUENTE_FALLBACK"
    gsettings set org.gnome.desktop.interface monospace-font-name "$FUENTE_FALLBACK 12"
fi

echo "[VFT-VSCODE] Validación de fuente completada ✅"

# Validación de shell activo
SHELL_ACTIVO=$(basename "$SHELL")
if [ "$SHELL_ACTIVO" = "zsh" ]; then
    echo "[VSH-ZSH] Shell activo: Zsh ✔️"
else
    echo "[VSH-ZSH] Shell activo: $SHELL_ACTIVO ❌ (se esperaba Zsh)"
fi

# Validación de tema Powerlevel10k
if grep -q 'powerlevel10k/powerlevel10k' "$HOME/.zshrc"; then
    echo "[THEME-P10K] Tema Powerlevel10k detectado en .zshrc ✔️"
else
    echo "[THEME-P10K] Tema Powerlevel10k no detectado ❌"
fi

# Validación de entorno heredado
if [ -n "$TERM_PROGRAM" ] || [ "$PWD" != "$HOME" ]; then
    echo "[ENV-VSCODE] VSCode lanzado desde terminal ✔️"
else
    echo "[ENV-VSCODE] VSCode podría no estar heredando entorno ❌"
fi

echo "[ENV-OK] Validación extendida completada ✅"
} | tee -a "$LOG"
