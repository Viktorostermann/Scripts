menu = ["Pizza", "Pasta", "Burrito", "Hamburguesa"]
prod = input("Escribe tu plato favorito: ")

encontrado = False 

for item in menu:
    if prod.lower() == item.lower():
        encontrado = True
        break

if encontrado:
    print("¡Este plato está en el menú!")
else:
    print("Lo siento, este plato no está en el menú.")