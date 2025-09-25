import tkinter as tk
from tkinter import messagebox
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException

def detectar_idioma():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor, escribe algún texto.")
        return

    try:
        idioma = detect(texto)
        probabilidades = detect_langs(texto)
        etiqueta_resultado.config(
            text=f"🌍 Idioma detectado: {idioma}\n🔎 Probabilidades: {probabilidades}",
            fg="blue"
        )
    except LangDetectException:
        etiqueta_resultado.config(text="❌ No se pudo detectar el idioma (texto insuficiente).", fg="red")

ventana = tk.Tk()
ventana.title("Detector de Idioma")
ventana.geometry("500x300")
ventana.resizable(False, False)

etiqueta_instrucciones = tk.Label(ventana, text="Escribe un texto para detectar su idioma:")
etiqueta_instrucciones.pack(pady=10)

entrada_texto = tk.Text(ventana, height=6, width=60, font=("Helvetica", 12))
entrada_texto.pack(pady=5)

boton_detectar = tk.Button(ventana, text="Detectar Idioma", command=detectar_idioma)
boton_detectar.pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="", font=("Helvetica", 12))
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
