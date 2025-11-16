aficiones = {
    "Juan": "Fútbol",
    "Ana": "Lectura",
    "Carlos": "Ciclismo",
    "María": "Cocina",
    "Pedro": "Videojuegos"
}
letra = input('¿Qué nombre de compañero quieres consultar? ')

if letra in aficiones:
    print(letra + " tiene como afición: " + aficiones[letra])
else:
    print("No se encontró ese nombre en la lista.")