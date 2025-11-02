# --- Ingrese su nombre
print("")
nombre = input("Introduce tu nombre: ")

# --- Solucionar si el usuario ingresa mal el nombre de usuario ingresa un punto ( . )
nombre = nombre.replace(".", "") or nombre.replace(",", "")

# --- Solucionar si el usuario ingresa mal el nombre de usuario ingresa almohadilla ( # )
nombre = nombre.replace("#", "") or nombre.replace(" ", "")

# --- Variables con los Nombres de usuarios
print("")
usuario_1 = "alejandro"
usuario_2 = "naomi"
usuario_3 = "sergio"
administrador = "victor"

# --- Comprueba si el nombre es igual o coincide que el nombre del administrador o usuarios
# Si es igual, le damos bienvenida personalizada
print("")
if (
    nombre.lower() == usuario_1
    or nombre.lower() == usuario_2
    or nombre.lower() == usuario_3
):  # case insensitive
    print("Bienvenido Usuario: ", nombre.title(), "!")

print("")
if (
    nombre.lower() != administrador
    or nombre.lower() != usuario_1
    or nombre.lower() != usuario_2
    or nombre.lower() != usuario_3
):  # case insensitive
    print("Bienvenido usuario invitado")

# Si no, bnienvenida generica
else:
    print("Bienvenido administrador ", administrador)
    print("")
