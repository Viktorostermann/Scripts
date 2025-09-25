import random

acum = 0
for i in range(10):
    x = random.randint(1, 6)
    if x >= 5:
        print(x, "¡Escapaste de los monstruos!")
        acum = acum + 1
    else:
        print(x, "Esta vez no pudiste escapar, los monstruos te han atrapado...")
print("Lograste escapar de los monstruos", acum, "veces")