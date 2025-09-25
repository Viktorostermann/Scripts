import time # Cargador de datos
print()

temporizador = int(input("Ingrese el tiempo en segundos para el temporizador: "))
print()
print("El temporizador comenzara a contar desde: ", temporizador, "segundos")
for i in range(temporizador,0,-1): # ---- Bucle para contar hacia atras
    print()
    print('Quedan', i, 'segundos')
    # ---- Pausa de 1 segundo 
    time.sleep(1)
print()
print("El temporizador ha finalizado")
print()