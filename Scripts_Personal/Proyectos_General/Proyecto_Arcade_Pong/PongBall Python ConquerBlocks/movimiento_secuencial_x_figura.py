import pygame
pygame.init()

# 🖥️ Crear ventana
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Movimiento Secuencial de Figuras")

# ⏱️ Control de tiempo
tiempo_por_figura = 5000  # milisegundos
inicio = pygame.time.get_ticks()
indice_figura = 0

# 📍 Posiciones iniciales
posiciones = {
    "rect": [100, 100],
    "circ": [300, 150],
    "elip": [400, 250],
    "poly": [(550, 100), (600, 200), (500, 200)]
}

# 🧭 Velocidades
velocidad = -0.5

jugando = True
while jugando:
    ventana.fill((30, 30, 30))

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - inicio >= tiempo_por_figura:
        inicio = tiempo_actual
        indice_figura = (indice_figura + 1) % 4  # rotar entre 0–3

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # 🔄 Movimiento de la figura actual
    if indice_figura == 0:
        posiciones["rect"][0] += velocidad
        pygame.draw.rect(ventana, (255, 0, 0), (*posiciones["rect"], 80, 60))
    elif indice_figura == 1:
        posiciones["circ"][1] += velocidad
        pygame.draw.circle(ventana, (255, 150, 0), posiciones["circ"], 40)
    elif indice_figura == 2:
        posiciones["elip"][0] -= velocidad
        pygame.draw.ellipse(ventana, (150, 0, 255), (*posiciones["elip"], 120, 60))
    elif indice_figura == 3:
        posiciones["poly"] = [(x, y + velocidad) for x, y in posiciones["poly"]]
        pygame.draw.polygon(ventana, (0, 200, 0), posiciones["poly"])

    pygame.display.update()

pygame.quit()
