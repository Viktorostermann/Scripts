import random

suma = 0

for _ in range(5):
    numero = random.randint(1, 100)  
    print("Número generado:", numero)
    suma += numero  

# Mostrar la suma final
print("La suma total de los números generados es:", suma)