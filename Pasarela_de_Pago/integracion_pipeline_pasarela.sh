#!/bin/bash

# Preflight (opcional)
bash scripts/apache_preflight_pasarela.sh

# Ejecución principal
python3 pasarela.py

# Postflight
bash scripts/apache_postflight_pasarela.sh
