resultados = {}

continuar = True

while continuar:
    print("1. Registrar voto")
    print("2. Mostrar lista de candidatos y votos")
    print("3. Encontrar candidato ganador")
    print("4. Calcular porcentaje de votos por candidato")
    print("5. Salir")    
    opcion = input("Ingrese una opción: ")

    # Registrar voto
    if opcion == "1":
        # Pedimos el nombre del candidato
        candidato = input("Ingrese el nombre del candidato: ")

        # comprobamos si el candidato ya existe en el diccionario
        if candidato in resultados:
            # sumamos el voto
            resultados[candidato] = resultados[candidato] + 1
        # si no existe, creamos una nueva entrada en el diccionario
        else:
            # añadimos el voto
            resultados[candidato] = 1

        print("Voto registrado exitosamente.")

    # Mostrar lista de candidatos y votos
    elif opcion == "2":
        # Mostramos el nombre de cada candidato y el número de votos que ha recibido
        for candidato, votos in resultados.items():
            # Imprimimos el nombre del candidato    
            print(f"{candidato}: {votos} votos")  # Imprimimos el nombre del candidato, resultados[candidato])

    # Encontrar candidato ganador
    elif opcion == "3":
        # Comprobamos si hay candidatos que hayan votado
        # Si no
        if len(resultados) == 0:
            print("No se han registrado votos.")
        # Si hay votaciones registradas
        else:
            # Extraemos la clave asociada al numero de votos más alto
            ganador = max(resultados, key=resultados.get)
            # Imprimimos el nombre
            print(f"El candidato ganador es {ganador} con {resultados[ganador]} votos.")

    # Encontramos el candidato con el mayor numero de votos
    elif opcion == "4":
        # Comprobamos si hay candidatos que hayan votado
        total_votos = sum(resultados.values())
        print("Total de votos")
        for candidato, votos in resultados.items():
            porcentaje = (votos / total_votos) * 100
            print(f"{candidato}: {porcentaje:.2f}%")

    # Cerrar Script
    elif opcion == "5":
        print("Cerrando votaciones")
        continuar = False
        break
    # Si la opción no es válida
    else:
        print("Opción inválida. Por favor, elija una opción válida.")