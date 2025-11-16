import random
# Variables:
lolx = random.randint(1, 6) #    <--- Numero aleatorio (numero x)
print("*El numero del dado es:", lolx, "*") # <--- Imprimir el numero de la variable. (lolx)
# Condiciones!!!
if lolx >= 5:
    print("¡Escapaste de los monstruos!")  # <---- Si esque el numero es 5 o 6.
else:
    print("Esta vez no pudiste escapar, fuiste atrapado por los monstruos…") # <--- Si es que el numero es menor que 4 o igual.