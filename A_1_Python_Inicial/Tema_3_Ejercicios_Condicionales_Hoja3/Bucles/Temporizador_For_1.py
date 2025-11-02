import time # Cargador de datos
print()

temporizador = int(input("Ingrese el tiempo en segundos para el temporizador: "))
print()
print("El temporizador comenzara a contar desde: ", temporizador, "segundos")
for i in range(-1,temporizador): # ---- Bucle para contar el tiempo de inicio regresivo finaliza en 1 segundo
    print()
    print('Quedan', temporizador, 'segundos')
    # ---- Pausa de 1 segundo 
    time.sleep(1)
    temporizador = temporizador - 1
print()
print("El temporizador ha finalizado")
print()