import random

# Escribe tu código aquí
x = random.randint(1, 20)
y = random.randint(1, 20)
suma = x + y
print(x, '+', y)
respuesta = int(input("Cual es la respuesta de esta suma?:"))
if respuesta == x + y:
    print("Buen trabajo!")
else:
    print("Error! La respuesta correcta es:", suma)