# --- Contraseña de usuario correcta
key = "micontraseña123"

# --- Pedimos al usuario la contraseña
password = input("Introduce su copntraseña : ")
print("\n")

# --- Comprobar si contraseña del usuario es correcta, comparamos con nuestra (Key)
if password.lower() == key.lower():
# Si cumple los requisitos (requisitos damos la bienvenida)
    print("Bienvenido! su contraseña es correcta")

else:
# Si no cumple los requisitos (damos un error y volvemos a pedir la contraseña)
    print("Error, la contraseña no es correcta")
    password = input("Introduce su contraseña nuevamente: ")
    if password.lower() == key.lower():
## Si esta vez la contraseña es valida damos la bienvenida
        print("Contraseña correcta, Bienvenido!")
    else:
## Si no coincide damos un error y salimos del programa
        print("\n")
        print("La contraseña no es correcta! ")
        print("Cerrando sistema")
