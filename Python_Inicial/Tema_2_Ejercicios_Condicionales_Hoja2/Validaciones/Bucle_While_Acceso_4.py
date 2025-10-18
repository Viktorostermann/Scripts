'''Escribir un programa que almacene la cadena de caracteres, 
contraseña en una variable, pregunte al usuario por la contraseña 
hasta que introduzca la contraseña.'''

# ---- Contraseña guardada
password = "secreto"
password_entrada = " "

# ---- Bucle para pedir la contraseña
# ---- out: contraseña sea correcta

contador = 0
while True:
     password_entrada = input("Introduce tu contraseña, debe ser la correcta: ")
     if password_entrada != password:
       contador = contador + 1
     if contador == 1:
        print("Acceso Denegado, quedan 2 intentos")
     elif contador == 2:
        print("Acceso Denegado, quedan 1 intentos")
     elif contador == 3:
        print("Acceso Denegado, Adios!")
        break
     if password_entrada == "":
        print("Campo vacio, intente de nuevo")
        continue
     elif password_entrada == password:
        print("Acceso permitido, Bienvenido")
        break