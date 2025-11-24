contador = 0
chicos = 0
chicas = 0

# Escribe tu código aquí:
for i in range(5):
    edad = int(input("¿Cuál es tu edad?: "))
    genero = input("¿Cuál es tu género? (Chico/Chica): ").strip().lower()

    if edad >= 10 and edad <= 12:
        print("¡Felicitaciones, fuiste admitido al equipo!")
        contador += 1
        if genero == "chico":
            chicos += 1
        elif genero == "chica":
            chicas += 1
        else:
            print("Género no reconocido, no se contará en las estadísticas de género.")
    else:
        print("Lamentablemente, no cumples los requisitos.")


print("Reclutamiento finalizado. ¡Hemos evaluado a", contador, "personas!")
print("Chicos aceptados:", chicos)
print("Chicas aceptadas:", chicas)