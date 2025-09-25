
''' Juego Original tomado de Pseint ConquerBlocks y Adaptadoa a Python por Victor Miletic" '''

# 🚢 Hundir la Flotaimport tkinter as tk

import tkinter as tk
from tkinter import ttk, messagebox
import random

# 🔧 Crear tablero vacío
def crear_tablero(tamano):
    return [['~' for _ in range(tamano)] for _ in range(tamano)]

# 🚢 Colocar barcos aleatoriamente
def colocar_barcos(tablero, num_barcos):
    tamano = len(tablero)
    barcos_colocados = 0
    while barcos_colocados < num_barcos:
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)
        if tablero[fila][columna] == '~':
            tablero[fila][columna] = 'B'
            barcos_colocados += 1

# ⚙️ Configurar dificultad
def configurar_dificultad(dificultad, tamano):
    niveles = {
        "Fácil":    {'num_barcos': tamano * tamano // 6, 'intentos_maximos': tamano * 3, 'pista_cada_n_intentos': 3},
        "Medio":    {'num_barcos': tamano * tamano // 5, 'intentos_maximos': tamano * 2, 'pista_cada_n_intentos': 5},
        "Difícil":  {'num_barcos': tamano * tamano // 4, 'intentos_maximos': tamano,     'pista_cada_n_intentos': 7},
    }
    return niveles[dificultad]

# 🧭 Dar pista técnica
def dar_pista(tablero):
    tamano = len(tablero)
    for fila in range(tamano):
        for columna in range(tamano):
            if tablero[fila][columna] == 'B':
                return f"💡 Hay un barco cerca de la fila {fila}"
    return "🔍 No se encontraron barcos visibles"

# 🪄 Popup de fin de juego
def mostrar_popup_fin(mensaje):
    respuesta = messagebox.askquestion("Fin del juego", f"{mensaje}\n¿Deseas volver a jugar?")
    if respuesta == "yes":
        iniciar_juego()
    else:
        root.quit()

# 🚀 Iniciar el juego
def iniciar_juego():
    global tablero_frame, botones

    dificultad = dificultad_var.get()
    tamano = int(tamano_var.get())
    config = configurar_dificultad(dificultad, tamano)

    tablero = crear_tablero(tamano)
    colocar_barcos(tablero, config['num_barcos'])

    intentos = 0
    barcos_hundidos = 0
    juego_activo = True

    # 🧼 Limpiar tablero anterior
    for widget in tablero_frame.winfo_children():
        widget.destroy()

    botones = []

    # 🎯 Manejador de clics
    def manejar_click(fila, columna):
        nonlocal intentos, barcos_hundidos, juego_activo
        if not juego_activo:
            return

        celda = tablero[fila][columna]
        boton = botones[fila][columna]

        if celda == 'B':
            boton.config(bg="red", text="💥")
            tablero[fila][columna] = 'X'
            barcos_hundidos += 1
        elif celda == '~':
            boton.config(bg="blue", text="🌊")
            tablero[fila][columna] = 'O'
            intentos += 1
            if intentos % config['pista_cada_n_intentos'] == 0:
                pista_label.config(text=dar_pista(tablero))
        else:
            return  # Ya fue clickeado

        # 🔄 Actualizar estado
        estado_label.config(
            text=f"Intentos: {intentos}/{config['intentos_maximos']} - Barcos hundidos: {barcos_hundidos}/{config['num_barcos']}"
        )

        # 🏁 Fin del juego
        if barcos_hundidos == config['num_barcos']:
            estado_label.config(text="🏆 ¡Has ganado!")
            juego_activo = False
            mostrar_popup_fin("🏆 ¡Has ganado!")
        elif intentos == config['intentos_maximos']:
            estado_label.config(text="💀 ¡Has perdido!")
            juego_activo = False
            mostrar_popup_fin("💀 ¡Has perdido!")

    # 🧩 Crear botones del tablero
    for fila in range(tamano):
        fila_botones = []
        for columna in range(tamano):
            boton = tk.Button(tablero_frame, text="~", width=4, height=2,
                              command=lambda f=fila, c=columna: manejar_click(f, c))
            boton.grid(row=fila, column=columna)
            fila_botones.append(boton)
        botones.append(fila_botones)

    # 🧾 Estado inicial
    estado_label.config(
        text=f"Intentos: {intentos}/{config['intentos_maximos']} - Barcos hundidos: {barcos_hundidos}/{config['num_barcos']}"
    )
    pista_label.config(text="")

# 🪟 Crear ventana principal
root = tk.Tk()
root.title("🚢 Hundir Flota For: CON'QUERBLOCKS")

# 🧲 Contenedor central autoajustable
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
container_frame = tk.Frame(root)
container_frame.grid(row=0, column=0, sticky="nsew")
container_frame.grid_columnconfigure(0, weight=1)
container_frame.grid_columnconfigure(1, weight=1)

# 🎛️ Variables
dificultad_var = tk.StringVar()
tamano_var = tk.StringVar(value="5")

# 🎚️ Widgets de configuración
tk.Label(container_frame, text="Seleccione el nivel de dificultad:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
dificultad_combobox = ttk.Combobox(container_frame, textvariable=dificultad_var)
dificultad_combobox['values'] = ("Fácil", "Medio", "Difícil")
dificultad_combobox.current(0)
dificultad_combobox.grid(row=0, column=1, sticky="w", padx=5)

tk.Label(container_frame, text="Ingrese el tamaño del tablero:").grid(row=1, column=0, sticky="e", padx=5)
tk.Entry(container_frame, textvariable=tamano_var).grid(row=1, column=1, sticky="w", padx=5)

tk.Button(container_frame, text="Iniciar Juego", command=iniciar_juego).grid(row=2, column=0, columnspan=2, pady=10)

# 🧾 Labels de estado
estado_label = tk.Label(container_frame, text="")
estado_label.grid(row=3, column=0, columnspan=2)

pista_label = tk.Label(container_frame, text="")
pista_label.grid(row=4, column=0, columnspan=2)

# 📦 Frame para tablero
tablero_frame = tk.Frame(container_frame)
tablero_frame.grid(row=5, column=0, columnspan=2, pady=10)

# ▶️ Loop principal
root.mainloop()
