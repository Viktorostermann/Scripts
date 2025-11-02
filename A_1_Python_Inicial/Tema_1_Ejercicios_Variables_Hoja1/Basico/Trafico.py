
edad = int(input('¿Cuantos años tienes?'))
    # Determinar la información sobre el viaje
if edad < 7:
    #  Yo le añadi una variable para no usar print tan repetidamente...(no necesario).
    mensaje = "Debes viajar atrás en un asiento de seguridad para niños."
elif 7 == edad < 12:
    mensaje = "Puedes viajar en la parte de atrás sin asiento de seguridad."
elif 12 <= edad < 18:
    mensaje = "Puedes viajar en el asiento de adelante."
else:
    mensaje = "Puedes manejar un automóvil"

#  Imprimimos el mensaje :)))
print(mensaje)