''' 🧩 Versión con bucle de vida funcional
python'''


import os
import pygame

def verificar_sprite(sprite_path, ventana_tamano=(640, 480)):
    pygame.init()
    ventana = pygame.display.set_mode(ventana_tamano)
    pygame.display.set_caption("Verificación de Sprite")

    if not os.path.exists(sprite_path):
        print(f"❌ Archivo no existe: {sprite_path}")
        pygame.quit()
        return

    try:
        sprite = pygame.image.load(sprite_path)
    except Exception as e:
        print(f"❌ Error al cargar sprite: {e}")
        pygame.quit()
        return

    ventana.fill((50, 50, 50))  # Fondo gris oscuro
    ventana.blit(sprite, (50, 50))  # Posicionamos el sprite en coordenadas visibles
    pygame.display.update()
    print("✅ Sprite cargado y mostrado. Cierra la ventana para finalizar.")

    # 🧠 Mantener la ventana abierta hasta cierre manual
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()