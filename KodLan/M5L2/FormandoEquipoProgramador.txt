count = 0
while True:
    print("--- Evaluación de Candidato ---")
    age = int(input("Ingresa tu edad: "))
    pr = input("¿Te gusta programar? (Si/No): ").strip().lower()
    exp = int(input("¿Cuántos años de experiencia laboral tienes? "))
    
    # Verificando los CRITERIOSSSS
    if age >= 12 and age <= 17 and pr == "si" and exp > 2:
        print("¡Estás dentro del equipo! :D")
        count += 1
        if count == 5: # SI Se recluto 5 ppl
            break
    else:
        print("No cumples con los requisitos para estar en el equipo... :c")
# Fin.
print("El reclutamiento de programadores ha finalizado.")
print("El equipo ha reclutado", count, "personas.")