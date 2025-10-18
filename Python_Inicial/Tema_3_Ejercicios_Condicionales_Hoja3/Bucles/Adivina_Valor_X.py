import random

count = 0
while True:
    x = random.randint(0, 100)
    # Escribe tu código debajo
    print("El valor de x... :", x)
    count += 1
    if x == 73:
        print("El programa se detiene! X es igual a 73!")
        break 
print("Cuantas veces se cambio el valor de x:")
print(count)