import tkinter as tk
from tkinter import ttk
import random

# Función para crear el tablero inicial
def crear_tablero(tamano): 
    return [['~' for _ in range(tamano)] for _ in range(tamano)]

# Colocar barcos aleatoriamente en el tablero
def colocar_barcos(tablero, num_barcos): 
    tamano = len(tablero)
    barcos_colocados = 0
    while barcos_colocados < num_barcos: 
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)  
        if tablero[fila][columna] == '~':
            tablero[fila][columna] = 'B'
            barcos_colocados += 1

# Configurar dificultad según el nivel seleccionado
def configurar_dificultad(dificultad, tamano): 
    if dificultad == 1:  # Fácil
        return {'num_barcos': tamano * tamano // 6, 'intentos_maximos': tamano * 3, 'pista_cada_n_intentos': 3}
    elif dificultad == 2:  # Medio
        return {'num_barcos': tamano * tamano // 5, 'intentos_maximos': tamano * 2, 'pista_cada_n_intentos': 5}
    else:  # Difícil
        return {'num_barcos': tamano * tamano // 4, 'intentos_maximos': tamano, 'pista_cada_n_intentos': 7}

# Mostrar pista al usuario
def dar_pista(tablero):
    tamano = len(tablero)
    for fila in range(tamano):
        for columna in range(tamano):
            if tablero[fila][columna] == 'B':
                return f"Hay un barco cerca de la fila {fila}"
    return "No se encontraron barcos"

# Crear la interfaz gráfica
def iniciar_juego():
    dificultad = dificultad_var.get()
    tamano = int(tamano_var.get())
    if dificultad == "Fácil":
        config = configurar_dificultad(1, tamano)
    elif dificultad == "Medio":
        config = configurar_dificultad(2, tamano)
    else:  # Difícil
        config = configurar_dificultad(3, tamano)
    
    tablero = crear_tablero(tamano)
    colocar_barcos(tablero, config['num_barcos'])

    intentos = 0
    barcos_hundidos = 0

    # Manejador de clics en el tablero
    def manejar_click(fila, columna):
        nonlocal intentos, barcos_hundidos
        if tablero[fila][columna] == 'B':  # Si es un barco
            botones[fila][columna].config(bg="red", text="💥")
            tablero[fila][columna] = 'X'
            barcos_hundidos += 1
            estado_label.config(text=f"Intentos: {intentos}/{config['intentos_maximos']} - Barcos hundidos: {barcos_hundidos}/{config['num_barcos']}")
            if barcos_hundidos == config['num_barcos']:
                estado_label.config(text="¡Has ganado!")
        elif tablero[fila][columna] == '~':  # Si es agua
            botones[fila][columna].config(bg="blue", text="🌊")
            tablero[fila][columna] = 'O'
            intentos += 1
            estado_label.config(text=f"Intentos: {intentos}/{config['intentos_maximos']} - Barcos hundidos: {barcos_hundidos}/{config['num_barcos']}")
            if intentos > 0 and intentos % config['pista_cada_n_intentos'] == 0:
                pista_label.config(text=dar_pista(tablero))
            if intentos == config['intentos_maximos']:
                estado_label.config(text="¡Has perdido!")
        else:
            print("Ya has disparado aquí.")

    # Crear la ventana del tablero
    tablero_frame = tk.Frame(root)
    tablero_frame.grid(row=3, column=0, columnspan=2)

    botones = []
    for fila in range(tamano):
        fila_botones = []
        for columna in range(tamano):
            boton = tk.Button(tablero_frame, text="~", width=4, height=2,
                              command=lambda f=fila, c=columna: manejar_click(f, c))
            boton.grid(row=fila, column=columna)
            fila_botones.append(boton)
        botones.append(fila_botones)

    estado_label.config(text=f"Intentos: {intentos}/{config['intentos_maximos']} - Barcos hundidos: {barcos_hundidos}/{config['num_barcos']}")
    pista_label.config(text="")

# Crear ventana principal
root = tk.Tk()
root.title("Juego Hundir la Flota")

# Variables para configuración inicial
dificultad_var = tk.StringVar()
tamano_var = tk.StringVar()
tamano_var.set("5")  # Tamaño por defecto

# Crear widgets para configuración inicial
tk.Label(root, text="Seleccione el nivel de dificultad:").grid(row=0, column=0)
dificultad_combobox = ttk.Combobox(root, textvariable=dificultad_var)
dificultad_combobox['values'] = ("Fácil", "Medio", "Difícil")
dificultad_combobox.grid(row=0, column=1)
dificultad_combobox.current(0)

tk.Label(root, text="Ingrese el tamaño del tablero:").grid(row=1, column=0)
tamano_entry = tk.Entry(root, textvariable=tamano_var)
tamano_entry.grid(row=1, column=1)

tk.Button(root, text="Iniciar Juego", command=iniciar_juego).grid(row=2, column=0, columnspan=2)

# Labels para estado del juego
estado_label = tk.Label(root, text="")
estado_label.grid(row=4, column=0, columnspan=2)

pista_label = tk.Label(root, text="")
pista_label.grid(row=5, column=0, columnspan=2)

root.mainloop()