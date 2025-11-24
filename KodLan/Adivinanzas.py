# Definimos el acertijo y la respuesta correcta
acertijo = "¿Qué tiene raíces que no son plantas?"
respuesta_correcta = "un río"

# Preguntamos al usuario el acertijo
print("")
print("Adivina el siguiente acertijo:")
print("")
print(acertijo)
print("")
respuesta_usuario = input("Tu respuesta: ").strip().lower()  # Normalizamos la respuesta
print("")

# Comparamos la respuesta del usuario con la respuesta correcta
if respuesta_usuario == respuesta_correcta:
    print("¡La respuesta es correcta!")
else:
    print("La respuesta correcta es:", respuesta_correcta)