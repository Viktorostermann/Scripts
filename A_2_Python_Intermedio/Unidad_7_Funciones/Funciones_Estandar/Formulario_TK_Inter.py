import tkinter as tk
 
# Crear la ventana principal
ventana = tk.Tk()
 
# Definir la función que se ejecutará cuando se haga clic en el botón
def enviar_datos():
    print(" Nombre:", nombre.get())
    print("Edad:", edad.get())
    print("Email:", email.get())
 
# Crear los widgets del formulario
tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
nombre = tk.Entry(ventana)
nombre.grid(row=0, column=1)
 
tk.Label(ventana, text="Edad:").grid(row=1, column=0)
edad = tk.Entry(ventana)
edad.grid(row=1, column=1)
 
tk.Label(ventana, text="Email:").grid(row=2, column=0)
email = tk.Entry(ventana)
email.grid(row=2, column=1)
 
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.grid(row=3, column=0, columnspan=2)
 
# Mostrar la ventana
ventana.mainloop()