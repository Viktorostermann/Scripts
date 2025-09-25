# --- Pedir al usuario ingrese tres longitudes de lados de un triangulo y determinar si podemos formar un triangulo
# --- Determinar que triangulo es un triangulo equilatero, isosceles o escaleno

# --- Pedir al usuario que ingrese tres longitudes de lados de un triangulo
lado1 = float(input("Ingrese la longitud del primer lado del triangulo: "))
print("\n")
lado2 = float(input("Ingrese la longitud del segundo lado del triangulo: "))
print("\n")
lado3 = float(input("Ingrese la longitud del tercer lado del triangulo: "))
print("\n")

# --- Comprobacion si el triangulo es equilatero, isosceles o escaleno
# longitud 1 + 2 > 3, longitud 1 + 3 > 2, longitud 2 + 3 > 1

if lado1 == 0 or lado2 == 0 or lado3 == 0:
    print("Las longitudes de los lados ingresados no formam un triangulo")
    print("\n")
elif lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print("Las longitudes de los lados ingresados si forman un triangulo")
    print("El triangulo es equilatero")
    print("\n")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Las longitudes de los lados ingresados si forman un triangulo")
    print("El triangulo es isosceles")
    print("\n")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Las longitudes de los lados ingresados si forman un triangulo")
    print("El triangulo es escaleno")
    print("\n")
    print("\n")

# --- End of file ---