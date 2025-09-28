'''1. Crea una función llamada "saludar" que tome un parámetro "nombre"
y muestre un saludo personalizado.'''

print("")
def saludar(nombre):
    """Saluda al usuario por su nombre."""
    nombre = input("Ingresa tu nombre: ")
    print(f"¡Hola", nombre + "!" " Bienvenido.")
    print("\n")
saludar("nombre")