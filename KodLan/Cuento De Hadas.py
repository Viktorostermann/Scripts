print("¡Bienvenido al cuento de hadas!")
eleccion = input("¿Hacia dónde deseas seguir el camino? (izquierda, derecha, recto): ").lower()

if eleccion == "izquierda":
    print("El viajero encuentra un misterioso bosque lleno de criaturas mágicas.")
elif eleccion == "derecha":
    print("El viajero llega a un hermoso castillo donde vive un rey generoso.")
elif eleccion == "recto":
    print("El viajero continúa su camino y llega a Kodland, un lugar lleno de aventuras.")
else:
    print("Esa no es una dirección válida. ¡Elige entre izquierda, derecha o recto!")