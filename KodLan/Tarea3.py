nombre = input("Ingrese su nombre: ")
edad = int(input("¿Cuál es su edad? "))
superpoder = input("¿Su superpoder es volar? (Si/No): ").strip().lower()

if edad >= 18 and superpoder == "si":
    print("El nombre del superhéroe adulto es:", nombre, "y es un héroe real.")
    print("El superpoder del superhéroe es: volar.")
elif edad < 18 and superpoder == "si":
    print("El nombre del superhéroe joven es:", nombre, "y es un aspirante a héroe.")
    print("El superpoder del superhéroe es: volar.")