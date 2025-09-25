import tkinter as tk
import random
import timeit

# Frases de prueba
frases = [
    "La práctica hace al maestro.",
    "Python es un lenguaje poderoso y fácil de aprender.",
    "El conocimiento es poder.",
    "Una mente en calma trae fuerza interior.",
    "El éxito es la suma de pequeños esfuerzos repetidos cada día."
]

# Variables globales
frase_actual = ""
tiempo_inicio = 0

# Funciones
def iniciar_prueba():
    global frase_actual, tiempo_inicio
    frase_actual = random.choice(frases)
    etiqueta_frase.config(text=frase_actual)
    entrada_texto.delete(0, tk.END)
    resultado.config(text="")
    entrada_texto.config(state="normal")
    entrada_texto.focus()
    tiempo_inicio = timeit.default_timer()

def finalizar_prueba():
    tiempo_final = timeit.default_timer()
    entrada = entrada_texto.get().strip()
    entrada_texto.config(state="disabled")
    if entrada == frase_actual:
        tiempo_total = tiempo_final - tiempo_inicio
        resultado.config(text=f"✅ Correcto. Tiempo: {tiempo_total:.2f} segundos", fg="green")
    else:
        resultado.config(text="❌ La frase no coincide. Intenta de nuevo.", fg="red")

# GUI
ventana = tk.Tk()
ventana.title("Prueba de Escritura Veloz")
ventana.geometry("600x250")
ventana.resizable(False, False)

# Widgets
instrucciones = tk.Label(ventana, text="Presiona 'Iniciar' para comenzar. Escribe exactamente la frase mostrada.")
instrucciones.pack(pady=10)

etiqueta_frase = tk.Label(ventana, text="", font=("Helvetica", 14), wraplength=550, fg="blue")
etiqueta_frase.pack(pady=10)

entrada_texto = tk.Entry(ventana, width=80, font=("Helvetica", 12), state="disabled")
entrada_texto.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_iniciar = tk.Button(frame_botones, text="Iniciar", command=iniciar_prueba)
boton_iniciar.pack(side="left", padx=10)

boton_finalizar = tk.Button(frame_botones, text="Finalizar", command=finalizar_prueba)
boton_finalizar.pack(side="left", padx=10)

# Resultado
resultado = tk.Label(ventana, text="", font=("Helvetica", 12))
resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
