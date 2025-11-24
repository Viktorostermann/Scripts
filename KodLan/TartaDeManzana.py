count = 0  # Inicializamos el contador de manzanas añadidas
while True:
    x = int(input("¿Cuántas manzanas debería agregar?: "))

    if count + x < 12:
        count += x  # Sumar la cantidad ingresada al contador
        print("Has agregado", count, "manzanas. Faltan ", 12 - count, "manzanas.")
    elif count + x == 12:
        count += x
        print("¡Perfecto! Has añadido exactamente 12 manzanas.")
        break  # Salimos del bucle porque ya se alcanzó el número necesario
    else:
        print("No puedes agregar", x, "manzanas. Te pasas del total necesario.")
        print("Has agregado hasta ahora", count, "manzanas. Faltan", 12 - count, "manzanas. Inténtalo de nuevo.")