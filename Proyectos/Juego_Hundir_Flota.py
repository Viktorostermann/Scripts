
# Juego hundir la flota ---
import random

#Algoritmo hundir la flota
def crear_tablero(tamano):
    return [['~'] * tamano for _ in range(tamano)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))

def colocar_barcos(tablero, num_barcos):
    tamano = len(tablero)
    for _ in range(num_barcos):
        while True:
            orientacion = random.choice(['H', 'V'])
            fila = random.randint(0, tamano - 1)
            columna = random.randint(0, tamano - 1)
            if orientacion == 'H' and columna + 1 < tamano and tablero[fila][columna] == '~' and tablero[fila][columna + 1] == '~':
                tablero[fila][columna] = 'B'
                tablero[fila][columna + 1] = 'B'
                break
            elif orientacion == 'V' and fila + 1 < tamano and tablero[fila][columna] == '~' and tablero[fila + 1][columna] == '~':
                tablero[fila][columna] = 'B'
                tablero[fila + 1][columna] = 'B'
                break

def disparar(tablero, fila, columna):
    if tablero[fila][columna] == 'B':
        tablero[fila][columna] = 'X'
        return True
    elif tablero[fila][columna] == '~':
        tablero[fila][columna] = 'O'
        return False
    return None

def juego_hundir_la_flota(dificultad):
    if dificultad == 'facil':
        tamano = 5
        num_barcos = 3
    elif dificultad == 'medio':
        tamano = 7
        num_barcos = 5
    elif dificultad == 'dificil':
        tamano = 10
        num_barcos = 7
    else:
        print("Dificultad no válida")
        return

    tablero = crear_tablero(tamano)
    colocar_barcos(tablero, num_barcos)
    intentos = tamano * 2

    while intentos > 0:
        imprimir_tablero(tablero)
        fila = int(input("Introduce la fila: "))
        columna = int(input("Introduce la columna: "))
        if disparar(tablero, fila, columna):
            print("¡Hundido!")
        else:
            print("Agua")
        intentos -= 1
        print("Juego terminado")
        imprimir_tablero(tablero)

# Ejemplo de uso
juego_hundir_la_flota('medio')