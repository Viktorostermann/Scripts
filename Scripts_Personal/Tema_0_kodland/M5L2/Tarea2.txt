# Variables
nombre = input("Ingrese el nombre de la película: ")
genero = input("¿Cuál es el género de su película? (terror, comedia, acción): ").strip().lower()
edad = int(input("Ingrese su edad: "))

# Condiciones:
# Terror:
if genero == "terror" and edad <= 13:
    print("No puedes ver la película.")
    
# Comedia:
elif genero == "comedia" and edad <= 14:
    print("No puedes ver la película.")
# Accion:
elif genero == "accion" and edad <= 16:
    print("No puedes ver la pelicula.")
else:
    print("Tienes permiso para ver", nombre, ".")