import tkinter as tk
from tkinter import filedialog, messagebox, font

#Crear archive
def nuevo_archivo():
    texto.delete("1.0", tk.END)

#Abrir archive
def abrir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            texto.delete("1.0", tk.END)
            texto.insert(tk.END, contenido)

# Guardar archive
def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(texto.get("1.0", tk.END))
        messagebox.showinfo("Guardado", "Archivo guardado correctamente.")

#Salir pues :p
def salir():
    ventana.destroy()

#Cambiar fuente (Tamaño letra)
def cambiar_fuente(tamano):
    fuente.config(size=tamano)

#Tamaño de la ventana
ventana = tk.Tk()
ventana.title("Editor de Texto")
ventana.geometry("600x400")

#Fuente predeterminada, Arial y tamaño pequeño.
fuente = font.Font(family="Arial", size=12)

menu = tk.Menu(ventana)
ventana.config(menu=menu)

#Labels (Guardar / Nuevo / Abrir / Salir)
archivo_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Nuevo", command=nuevo_archivo)
archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_command(label="Guardar", command=guardar_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir)

# Fuentes ( Tamaño de letra, Grande / Mediana / Pequeña)
fuente_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Fuente", menu=fuente_menu)
fuente_menu.add_command(label="Pequeña", command=lambda: cambiar_fuente(10))
fuente_menu.add_command(label="Mediana", command=lambda: cambiar_fuente(12))
fuente_menu.add_command(label="Grande", command=lambda: cambiar_fuente(16))

texto = tk.Text(ventana, wrap="word", font=fuente)
texto.pack(expand=1, fill="both")

#Loop principal
ventana.mainloop()
