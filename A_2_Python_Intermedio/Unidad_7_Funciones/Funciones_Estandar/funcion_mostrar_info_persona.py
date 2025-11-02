'''11. Crea una función llamada "mostrar_info_persona" que tome tres
argumentos de palabra clave: "nombre", "edad" y "ciudad". La función
debe imprimir en la consola la información de una persona en un
formato legible.'''


# Ejemplo_1 Forma básica de hacerlo:
print("")
def mostrar_info_persona(*, nombre, edad, ciudad):
    """Muestra la información de una persona."""

    #nombre = str(input("Introduce tu nombre: "))
    print(f"Nombre: {nombre}")
    #edad = int(input("Introduce tu edad: "))
    print(f"Edad: {edad}")
    #ciudad = str(input("Introduce tu ciudad: "))
    print(f"Ciudad: {ciudad}")

    print("\n")

# Llamada a la función con argumentos de palabra clave
mostrar_info_persona(nombre="Victor", edad=45, ciudad="Lima")

# Ejemplo_2 Forma con inputs:
print("")
def mostrar_info_persona(*, nombre, edad, ciudad):
    """Muestra la información de una persona."""

    nombre = str(input("Introduce tu nombre: "))
    print(f"Nombre: {nombre}")
    edad = int(input("Introduce tu edad: "))
    print(f"Edad: {edad}")
    ciudad = str(input("Introduce tu ciudad: "))
    print(f"Ciudad: {ciudad}")

    print("\n")
# Llamada a la función con argumentos de palabra clave
mostrar_info_persona(nombre="Ana", edad=30, ciudad="Madrid")