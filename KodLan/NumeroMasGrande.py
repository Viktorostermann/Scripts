max = 0
for i in range(5):
    numero = int(input("Ingresa un número: "))
    if numero > max:
        max = numero

print("El número más grande ingresado es: " + str(max))