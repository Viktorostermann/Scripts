'''
El bucle principal del juego: 
Todos los juegos tienen un bucle principal
que se ejecuta continuamente.
para actualizar y renderizar el juego. 
En Pygame, esto se logra mediante un bucle while:

import pygame # Importamos la librería pygame que nos permite crear juegos (inicializarlos) 

# Bucle principal del juego 
jugando = True 
while jugando: 
       for evento in pygame.event.get(): 
             if evento.type == pygame.QUIT: 
                 jugando = False 
      # Lógica del juego y renderizado aquí  

# Salir del juego 
pygame.quit()'''
import pygame
pygame.init()

# 🖥️ Ventana general
ancho_total, alto_total = 800, 600
ventana = pygame.display.set_mode((ancho_total, alto_total), pygame.RESIZABLE)
pygame.display.set_caption("Separación de Áreas: Rebote + Controles")

# 📦 Área de juego (zona superior)
area_juego = pygame.Rect(0, 0, ancho_total, 450)

# 🎯 Posición inicial del objeto
x, y = 100, 100

# ⚡ Velocidades base con dirección
vel_x, vel_y = -0.8, -0.6
factor_velocidad = 1.0

# 🎚️ Slider en zona inferior
slider_rect = pygame.Rect(150, 520, 500, 10)
handle_rect = pygame.Rect(150, 510, 10, 30)
ajustando = False

# 🔁 Bucle principal
jugando = True
while jugando:
    ventana.fill((30, 30, 30))  # 🌌 Fondo general

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if handle_rect.collidepoint(evento.pos):
                ajustando = True
        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            ajustando = False
        elif evento.type == pygame.MOUSEMOTION and ajustando:
            nuevo_x = max(slider_rect.left, min(slider_rect.right - handle_rect.width, evento.pos[0]))
            handle_rect.x = nuevo_x
            porcentaje = (handle_rect.x - slider_rect.x) / (slider_rect.width - handle_rect.width)
            factor_velocidad = round(porcentaje * 10, 2)

    # 🧮 Velocidad con factor aplicado
    velocidad_aplicada_x = vel_x * factor_velocidad
    velocidad_aplicada_y = vel_y * factor_velocidad

    # 🔄 Movimiento del rectángulo
    x += velocidad_aplicada_x
    y += velocidad_aplicada_y

    # 🧱 Rebote dentro del área de juego
    if x > area_juego.width - 10 or x < 0:
        vel_x *= -1
    if y > area_juego.height - 55 or y < 0:
        vel_y *= -1

    # 🎮 Dibujar objeto de rebote
    pygame.draw.rect(ventana, (255, 0, 0), (x, y, 10, 55))

    # 🧭 Delimitar área de rebote con línea clara
    pygame.draw.rect(ventana, (180, 180, 180), area_juego, 2)  # Borde claro

    # 🧩 Panel de control sombreado
    area_controles = pygame.Rect(0, 470, ancho_total, alto_total - 470)
    pygame.draw.rect(ventana, (50, 50, 50), area_controles)              # Fondo oscuro
    pygame.draw.rect(ventana, (80, 80, 80), area_controles, width=2)     # Borde claro

    # 🎚️ Dibujar slider dentro del panel
    pygame.draw.rect(ventana, (100, 100, 100), slider_rect)              # Barra gris
    pygame.draw.rect(ventana, (200, 200, 200), handle_rect)              # Manija clara

    # 🔢 Mostrar velocidad
    font = pygame.font.SysFont(None, 28)
    texto = font.render(f"Velocidad: {factor_velocidad}", True, (255, 255, 255))
    ventana.blit(texto, (slider_rect.x, slider_rect.y + 20))

    pygame.display.update()


# OTRAS FIGURAS

   # 🔷 Rectángulo rojo
    #pygame.draw.rect(ventana, (255, 0, 0), (100, 100, 80, 60))
    # 🟠 Círculo naranja
    #pygame.draw.circle(ventana, (255, 150, 0), (x, y, 300, 150), 40)
    # 🟣 Elipse morada
    #pygame.draw.ellipse(ventana, (150, 0, 255), (400, 250, 120, 60))
    # 🟩 Polígono (triángulo verde)
    #pygame.draw.polygon(ventana, (0, 200, 0), [(550, 100), (600, 200), (500, 200)])
    # 🟦 Línea azul
    #pygame.draw.line(ventana, (0, 150, 255), (100, 300), (700, 300), 5) 