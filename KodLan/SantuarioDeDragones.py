import time
import random

# Función para hacer pausas con un mensaje
def espera(mensaje, tiempo):
    print(mensaje)
    time.sleep(tiempo)

# Introducción de la historia
print("Después de una larga travesía, llegas a un sitio donde hay dos cuevas...")
espera("En una de ellas hay un dragón amistoso que va a compartir sus tesoros contigo...", 2)
espera("En la otra cueva vive otro dragón codicioso y hambriento. ¡Si te ve, te comerá!", 2)
print()

# Pregunta al jugador a qué cueva desea ir
eleccion = input("¿A qué cueva deseas ir? (1 o 2): ")

# Generamos aleatoriamente dónde está el dragón amistoso
cueva_amigable = random.randint(1, 2)

# Mensajes de suspenso antes de la elección
print()
espera("Te vas acercando lentamente a la cueva...", 2)
espera("Se ve oscura y escalofriante...", 2)
print()

# Mensaje después de elegir la cueva
print("¡De repente, un enorme dragón aparece en frente tuyo! Comienza a abrir su boca y...")
espera("", 1)

# Resultado de la elección
if int(eleccion) == cueva_amigable:
    espera("¡Felicidades! El dragón amistoso te invita a entrar y compartir sus tesoros.", 2)
    print("¡Has ganado una gran fortuna! Fin de la historia.")
else:
    espera("¡Oh no! El dragón codicioso te ve y comienza a rugir ferozmente...", 2)
    espera("¡Corre! ¡Debes escapar antes de que te atrape!", 2)
    print("¡Te ha alcanzado! Fin de la historia.")