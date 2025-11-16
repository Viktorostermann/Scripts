import time
import random

# Escribe tu código aquí
print("BIENVENIDO AL GENERADOR DE CONTRASEÑAS 3000™")
while True:
    registro = input('Ingresa tu nombre de usuario:')
    contrasena = random.randint(1000, 10000)
    print("Espere, su contraseña esta siendo generada...")
    time.sleep(5)
    print("Su contraseña es!:", contrasena)