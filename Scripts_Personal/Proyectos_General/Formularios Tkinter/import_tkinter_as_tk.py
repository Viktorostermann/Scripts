import tkinter as tk

# Crear una ventana simple
root = tk.Tk()
root.title("Ejemplo con Tkinter")

label = tk.Label(root, text="¡Hola, Tkinter!")
label.pack(padx=20, pady=20)

root.mainloop()