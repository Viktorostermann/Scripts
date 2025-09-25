'''
Cargar y mostrar sprites: Los sprites son objetos gráficos que representan personajes, objetos y elementos en tu juego. Puedes cargar imágenes como sprites y mostrarlos en la ventana de juego. 
Aquí hay un ejemplo de cómo cargar y mostrar un sprite:

'''
import pygame
import os
import json
from Paso_3_Crear_ventana_juego_config import VENTANA, sprite_path

# ✅ 1. Definir la función primero
def inicializar_posiciones(ventana, sprite_path, x=100, y=150, dry_run=False, debug=False):
    # ... [todo tu código original de la función acá]
    pass  # ← reemplazá esto con el cuerpo completo que ya tenés

# ✅ 2. Ejecutar la función después de definirla
resultado = inicializar_posiciones(VENTANA, sprite_path, x=100, y=150, debug=True)

# ✅ 3. Mantener ventana abierta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
