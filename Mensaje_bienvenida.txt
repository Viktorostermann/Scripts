# El objetivo de este ejercicio es que crees un script que dado un nombre de usuario de la -
# bienvenida con su nombre en el formato correcto

# Otra opcion es :
# mensaje = ("¿Como te llamas?")
# nombre = input ()

#---- Pedimos el input al usuario ----
print("\n")
nombre = input("¿Como tellamas? : ") # Los inputs son tipo string
nombre = nombre.title()

#---- Reformatear nombre ----
nombre = nombre.replace(".","")

#---- Escribimos mensaje en una variable ----
lenguaje = 'Python'
mensaje = "Hola," + nombre.title() + ", estás usando " + lenguaje.title() + "!"

#---- Escribimos el mensaje en una variable ----
mensaje = "¡Hola, " + nombre.title() +", estas usando Python!"
print("\n")

#---- Escribimos el mensaje imprimimos el mensaje por pantalla ----
print(mensaje)
print("\n")