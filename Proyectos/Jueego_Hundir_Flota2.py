# Se importa la libreria randomized y tkinter se cambia la función crear_tablero para que sea más eficiente. 
import random
import tkinter as tk

def crear_tablero(tamano): # Funcion para crear el tablero del juego
    return [['~' for _ in range(tamano)] for _ in range(tamano)] # Crear un tablero con el caracter '~' en cada celda para recerar el Mar

# Colocar barcos en el tablero
def colocar_barcos(tablero, num_barcos): # Funcion para colocar los barcos en el tablero
    tamano = len(tablero) # Obtener el tamaño del tablero
    barcos_colocados = 0 # El tablero no tiene barcos colocados

    # Colocar barcos aleatoriamente en el tablero del juego
    while barcos_colocados < num_barcos: # El tablero no tiene barcos colocados
        fila = random.randint(0, tamano-1) # Colocar barcos aleatoriamente en las filas del tablero del juego
        columna = random.randint(0, tamano-1) # Colocar barcos aleatoriamente en las columnas del tablero del juego  
        if tablero[fila][columna] == '~': # Se asgina los valores de cada posicion de la tablero para olas
            tablero[fila][columna] = 'B' # Se asgina los valores de cada posicion de la tablero para barcos
            barcos_colocados += 1 # Es el contador de los barcos colocados en el tablero

# Muestra el tablero del juego y se ocultan los barcos con una mascara de la tablero con el caracter '~' en forma de hola de mar 
def mostrar_tablero(tablero, ocultar_barcos=True): # Funcion para mostrar el tablero del juego con barcos ocultos  
    for fila in tablero: # recorrer cada fila del tablero
        fila_mostrar = [] # lista para almacenar las celdas de la fila del tablero
        for celda in fila: # recorrer cada celda de las filas del tablero     
            if ocultar_barcos and celda == 'B': # ocultar los barcos del tablero que tienen los barcos asignados   
                fila_mostrar.append('~') # oculta los barcos del tablero con el caracter '~'
            else:
                fila_mostrar.append(celda) # Mostrar las celdas del tablero  
        print(' '.join(fila_mostrar))   # Mostrar la fila del tablero       

# Verificar si se ha ganado el juego
def verificar_victoria(tablero):
    for fila in tablero: # recorrer cada fila del tablero
        if 'B' in fila: # se encontró un barco en la fila 
            return False # no se han hundido todos los barcos 
        return True # se han hundido todos los barcos   

# Se pide al usuario seleccione el nivel de dificultad del Juego
def seleccionar_dificultad():
    print("\nSeleccione nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    
    # Bucle de validacion para elegir nivel dificultad correcto para el juego con validacion de entrada de dato
    while True: 
        try:
            dificultad = int(input("Ingrese el número de dificultad (1-3): "))
            if 1 <= dificultad <= 3: 
                return dificultad
            print("Por favor, seleccione un número entre 1 y 3.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Asignacion de los objetos al juego segun la dificultad del juego seleccionada
def configurar_dificultad(dificultad, tamano): 
    if dificultad == 1:  # Fácil
        return {
            'num_barcos': tamano * tamano // 6,
            'intentos_maximos': tamano * 3,
            'pista_cada_n_intentos': 3
        }
    elif dificultad == 2:  # Medio
        return {
            'num_barcos': tamano * tamano // 5,
            'intentos_maximos': tamano * 2,
            'pista_cada_n_intentos': 5
        }
    else:  # Difícil
        return {
            'num_barcos': tamano * tamano // 4,
            'intentos_maximos': tamano,
            'pista_cada_n_intentos': 7
        }

 # Pista del juego para hacerlo más fácil 
def dar_pista(tablero):
    tamano = len(tablero)
    for fila in range(tamano):
        for columna in range(tamano):
            if tablero[fila][columna] == 'B':
                return f"Hay un barco cerca de la fila {fila}"
    return "No se encontraron barcos"

# Inicio del Juego Hundir el barco
def juego_hundir_la_flota(): 
    print('¡Bienvenido al juego de Hundir Barcos!')
    
    # Configuración inicial, eleccion del tamaño del tablero del juego
    tamano = int(input('Ingrese el tamaño del tablero (entre 5 y 10): '))
    while tamano < 5 or tamano > 10:
        print('Tamaño inválido. Intente de nuevo.')
        tamano = int(input('Ingrese el tamaño del tablero (entre 5 y 10): '))
    
    # Selección de dificultad
    dificultad = seleccionar_dificultad()
    config = configurar_dificultad(dificultad, tamano)

    # Inicializacion de variables del tablero y los objetos (tablero y barcos).
    tablero = crear_tablero(tamano)
    colocar_barcos(tablero, config['num_barcos'])
    intentos = 0
    barcos_hundidos = 0
    
    # Los inputs para pedir al usuario como desea configurar su juego
    print(f"\nConfiguración del juego:")
    print(f"Nivel de dificultad: {'Fácil' if dificultad == 1 else 'Medio' if dificultad == 2 else 'Difícil'}")
    print(f"Número de barcos: {config['num_barcos']}")
    print(f"Intentos máximos: {config['intentos_maximos']}")
    
    # Bucle principal del juego
    while intentos < config['intentos_maximos']:
        print(f'\nIntentos realizados: {intentos}/{config["intentos_maximos"]}')
        print(f'Barcos hundidos: {barcos_hundidos}/{config["num_barcos"]}')
        mostrar_tablero(tablero)
        
        # Dar pista según la dificultad
        if intentos > 0 and intentos % config['pista_cada_n_intentos'] == 0:
            print("\n¡PISTA!:", dar_pista(tablero))
        
        try: # Bucle de validacion para disparar en el tablero del juego con validacion de entrada
            print('\nTurno jugador:')
            fila = int(input(f'Ingrese la fila (entre 0 y {tamano - 1}): '))
            columna = int(input(f'Ingrese la columna (entre 0 y {tamano - 1}): '))
            
            if fila < 0 or fila >= tamano or columna < 0 or columna >= tamano:
                print('¡Coordenadas fuera del tablero! Intente de nuevo.')
                continue
                
            if tablero[fila][columna] == 'B':
                tablero[fila][columna] = 'X'
                barcos_hundidos += 1
                print('¡Acertaste un barco!')
                if barcos_hundidos == config['num_barcos']:
                    print('\n¡Has ganado! ¡Encontraste todos los barcos!')
                    mostrar_tablero(tablero, False)
                    return
            elif tablero[fila][columna] in ['X', 'O']:
                print('¡Ya has disparado en esa posición! Intenta de nuevo.')
                continue
            else:
                tablero[fila][columna] = 'O'
                print('¡Agua!')
                intentos += 1
                
        except ValueError:
            print('¡Entrada inválida! Por favor ingrese números.')
            continue
            
    print('\n¡Has perdido! Se acabaron los intentos.')
    print('Posición de los barcos:')
    mostrar_tablero(tablero, False)

if __name__ == "__main__":
    juego_hundir_la_flota()