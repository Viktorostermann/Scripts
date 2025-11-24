import random

list = []

for _ in range(5):
    number = random.randint(10, 100) 
    list.append(number)  

print("Contenido de la lista:", list)