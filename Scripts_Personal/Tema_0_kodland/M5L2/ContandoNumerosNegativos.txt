contador = 0

for i in range(5):
    numero = int(input("Ingresa un número: "))
    if numero < 0:
        contador += 1

print("Cantidad de números negativos ingresados: " + str(contador))