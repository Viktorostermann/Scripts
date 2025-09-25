import pygame
pygame.init()

# 🖥️ Configuración de ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rebote de Círculo")

# ⚙️ Parámetros del círculo
x, y = 100, 100
radio = 40
vx, vy = 3, 4  # velocidad por eje

reloj = pygame.time.Clock()
jugando = True
while jugando:
    ventana.fill((30, 30, 30))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # 🔁 Movimiento
    x += vx
    y += vy

    # 🧱 Rebote horizontal
    if x - radio <= 0 or x + radio >= ANCHO:
        vx *= -1

    # 🧱 Rebote vertical
    if y - radio <= 0 or y + radio >= ALTO:
        vy *= -1

    # 🎯 Dibujar círculo
    pygame.draw.circle(ventana, (255, 150, 0), (x, y), radio)

    pygame.display.update()
    reloj.tick(60)

pygame.quit()
