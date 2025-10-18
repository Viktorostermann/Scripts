'''Escribir un programa que almacene la cadena de caracteres, 
contraseña en una variable, pregunte al usuario por la contraseña 
hasta que introduzca la contraseña.'''

# ---- Contraseña guardada
password = "secreto"

# ---- Variable para almacenar la contraseña introducida por el usuario
password_entrada = ""

# ---- Bucle para pedir la contraseña
# ---- out: contraseña sea correcta
while True:
    password_entrada = input("Introduce tu contraseña: ")
    if  password_entrada == password:
        print("Contraseña correcta")
        break
    else:
        print("Acceso Permitido")
