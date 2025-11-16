import random
count = 0

while True:
    print("--- Bienvenido al juego de adivinanzas ---")
    print("Nivel 1: Adivina un número entre 1 y 10 (1 punto)")
    print("Nivel 2: Adivina un número entre 1 y 15 (2 puntos)")
    nivel = input("Escribe '1' para Nivel 1 o '2' para Nivel 2: ")
    if nivel == "1":
        x = random.randint(1, 10)  
        puntos = 1
        
    elif nivel == "2":
        x = random.randint(1, 15)
        puntos = 2
        
    else:
        print("Opción no válida. Jugarás en el Nivel 1.")
        x = random.randint(1, 10)
        puntos = 1

    answer = int(input("Adivina el número: "))

    if answer == x:
        count = count + puntos
        print("¡Correcto! Ganaste", puntos, "punto(s).")
    else:
        print("Más suerte la próxima. El número era", x)

    continuar = input("¿Quieres seguir jugando? (si/no): ").strip().lower()
    if continuar == "no":
        break

print("Juego terminado. Puntaje final:", count)