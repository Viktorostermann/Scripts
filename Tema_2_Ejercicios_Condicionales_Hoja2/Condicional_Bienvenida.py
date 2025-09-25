# --- Ingrese su nombre
print("")
nombre = input("Introduce tu nombre: ")

# --- Nombre del administrador
print("")
administrador = "victor"

# --- Comprueba si el nombre es igual que el nombre del administrador
# Si es igual, le damos bienvenida personalizada
print("")
if nombre.lower() == administrador: # case insensitive
    print("Bienvenido : ", nombre.title(), "!" )

# Si no, bnienvenida generica
else: 
    print("Bienvenido invitado!")
    print("")
    print("")