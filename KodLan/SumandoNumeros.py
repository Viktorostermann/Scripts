count = 0
while True:
    x = int(input("Ingresa un número:"))
    # Ingresa tu código abajo
    count = count + x
    if x == 0:
        print("La cantidad final de la suma es:", count)
        print("El programa se cierra!")
        break