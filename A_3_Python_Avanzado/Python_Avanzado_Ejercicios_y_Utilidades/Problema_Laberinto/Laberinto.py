''' Desarrolla un scipt que permita salir de un laberinto'''
def resolver_laberinto(laberinto, fila, columna, camino=None):
    if camino is None:
        camino = []

    # Validaciones
    if not (0 <= fila < len(laberinto)) or not (0 <= columna < len(laberinto[0])) \
       or laberinto[fila][columna] == 1 or (fila, columna) in camino:
        return None

    camino.append((fila, columna))

    # Caso base: salida encontrada
    if laberinto[fila][columna] == 9:
        return camino

    # Movimientos posibles: arriba, izquierda, abajo, derecha
    movimientos = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    for movimiento in movimientos:
        nueva_fila, nueva_columna = fila + movimiento[0], columna + movimiento[1]
        resultado = resolver_laberinto(laberinto, nueva_fila, nueva_columna, camino.copy())
        if resultado:
            return resultado

    return None


def imprimir_laberinto(laberinto, camino):
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila, columna) in camino:
                print(" * ", end="")  # más separación para el camino
            else:
                print(f" {laberinto[fila][columna]} ", end="")  # celda con espacios
        print("")  # salto de línea por fila



laberinto = [
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 9]
]

camino_solucion = resolver_laberinto(laberinto, 0, 0)

if camino_solucion:
    print("")
    print("El Camino para salir del laberinto es:")
    print("")
    imprimir_laberinto(laberinto, camino_solucion)
    print("")
else:
    print("No existe solucion")
