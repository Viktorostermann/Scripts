import random

# Escribe tu código aquí
print("")
print("***Adivina el numero, es un numero entre 1 y 10***")
print("")

x = random.randint(1, 10)
for i in range(3):
    print("")
    print(i+1," Intento")
    print("")
    y = int(input('Intenta adivinar el numero elegido por la computadora: '))
    if y == x:
        print("Bien hecho!")
        break
    else:
        print("")
        print("Esta vez no acertaste!")
        print("")
else:
    print("No te quedan intentos! El numero era:", x)
    print("")