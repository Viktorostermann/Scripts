import time

# Escribe tu código aquí
num = int(input("¿Desde que numero deseas comenzar el conteo?"))
for i in range(num, 0, -1):
    print("---------------")
    print(i)
    time.sleep(1)
print("Conteo regresivo terminado!")