''' Recursividad:

Ejercicio 3:

Problema de Resolución de Laberinto:

Imagina que eres parte de un equipo de desarrollo de IA que se encarga de
crear un sistema para que un robot resuelva laberintos. El laberinto está
representado por una matriz, donde ciertos valores indican caminos permitidos
( 0 ), paredes ( 1 ), y la salida ( 9 ). Tu tarea es implementar una función
recursiva que encuentre la ruta más corta para que el robot salga del laberinto.

Toma en cuenta los siguientes puntos:

1. La matriz representa el laberinto, donde los valores son:
-> 0 : Camino permitido.
-> 1 : Pared, no se puede atravesar.
-> 9 : Salida del laberinto.

2. Debes implementar la función resolver_laberinto que utiliza recursividad
para encontrar la ruta más corta desde una posición inicial hasta la salida.

3. La función debe devolver una lista de coordenadas que representan la ruta
desde la posición inicial hasta la salida.

4. Puedes usar una lista de movimientos posibles: arriba ( (-1, 0) ), abajo( (1,
0) ), izquierda ( (0, -1) ), derecha ( (0, 1) ). 

5. Se debe agregar el color al camino de salida'''


def resolver_laberinto(laberinto, fila, columna, camino=None, color_camino=[(255, 255, 0)]):
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

    
    # Colores RGBY para el camino
    #color_inicio = [(255, 0, 0)]  # Rojo
    #color_salida = [(0, 255, 0)]  # Verde
    #color_pared = [(0, 0, 255)]  # Azul
    color_camino = [(255, 255, 0)]  # Amarillo

def imprimir_laberinto(laberinto, camino, color_camino=(255, 255, 0)):
    amarillo = "\033[93m"   # ANSI escape code para amarillo
    reset = "\033[0m"       # Reset de color: restablece a la configuración predeterminada

    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila, columna) in camino:
                ''' Resaltar el color del camino en amarillo '''
                print(f"{amarillo} ° {reset}", end="")   # camino en amarillo
            else:
                print(f" {laberinto[fila][columna]} ", end="")  # celda normal
        print("")  # salto de línea por fila
        # print("-" * (len(laberinto[0]) * 4))  # línea horizontal separadora



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
