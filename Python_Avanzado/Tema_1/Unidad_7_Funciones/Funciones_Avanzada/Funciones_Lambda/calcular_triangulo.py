# Funciones Lambda


def area_triangulo(base,altura):
    # Opcion 1 normal
    # - return (base*altura)/2

    # Opcion 2 lambda
    area_triangulo = (lambda base, altura: (base * altura) / 2) # el return se sustituye por :

triangulo1 = area_triangulo(5,7)
triangulo2 = area_triangulo(9,6)

print(triangulo1, triangulo2)



