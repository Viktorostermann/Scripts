import tkinter as tk # Importar el módulo tkinter para crear la interfaz gráfica de usuario (GUI)
import pandas as pd

# importar modulos restantes
from tkinter import * # Todos los modulos disponibles de TkInter.
from tkinter import messagebox # Modulo de mensajes para eventos
from tkinter import ttk # Control de estilos de widgets, ComboBox, etc.

#class FormularioClientes:

# Crear y definir la ventana principal
Registro = tk.Tk()
Registro.geometry("400x300")
Registro.title("Formulario de Registro de Clientes")

# Definir la función que se ejecutará cuando se haga clic en el botón
def enviar_datos():
 try: # Permite generar un mensaje de error en caso de que el usuario no ingrese un valor en el campo de texto 
    print("Nombre:", nombre.get())
    print("Edad:", edad.get())
    print("Email:", email.get())
    print("Sexo:", Sexo.get())
    groupBox = LabelFrame() # --- Permite crear un grupo de Labels y Frames con editores de formulario
 except ValueError as error: # --- Captura el error y lo imprime en pantalla cierre de (Try:) 
    messagebox.showerror("Error {}".format(error)) # --- Muestra un mensaje de error en pantalla

# Crear los widgets del formulario
tk.Label(Registro , text="Nombre:", width=13,font=("arial",12)).grid(row=0, column=0)
nombre = tk.Entry(Registro )
nombre.grid(row=0, column=1)

tk.Label(Registro , text="Edad:", width=13,font=("arial",12)).grid(row=1, column=0)
edad = tk.Entry(Registro )
edad.grid(row=1, column=1)

tk.Label(Registro , text="Email:", width=13,font=("arial",12)).grid(row=2, column=0)
email = tk.Entry(Registro )
email.grid(row=2, column=1)

tk.Label(Registro , text="Sexo:", width=13,font=("arial",12)).grid(row=3, column=0)
Sexo = tk.Entry(Registro )
combo = ttk.Combobox(values=["Masculino" , "Femenino"],textvariable=Sexo)
combo.grid(row=3, column=1) 

#Enviar_Datos = tk.Entry(Registro)
boton_enviar = tk.Button(Registro , text="Enviar", width=13,font=("arial",8) ,command=enviar_datos)
boton_enviar.grid(row=5, rowspan=3, column=0, columnspan=1)

#Actualizar_Datos = tk.Entry(Registro)
def get_datos():
   boton_Agregar = tk.Button(Registro , text="Actualizar", width=13,font=("arial",8) ,command=get_datos)
   boton_Agregar.grid(row=6, rowspan=4, column=1, columnspan=1)


# Mostrar la ventana
Registro.mainloop()