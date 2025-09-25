# Pedir Usuario ingrese 4 numeros para indicar cual es numero mayor
numero1 = float(input("Ingrese el primer numero: "))
print("\n")
numero2 = float(input("Ingrese el segundo numero: "))
print("\n")
numero3 = float(input("Ingrese el tercer numero: "))
print("\n")
numero4 = float(input("Ingrese el cuarto numero: "))
print("\n")

# --- Comparar los 4 numeros para indicar cual es el mayor y menor
print("\n")
if numero1 > numero2 and numero1 > numero3 and numero1 > numero4:
    print(f"El numero mayor es: {numero1}")
elif numero1 < numero2 and numero1 < numero3 and numero1 < numero4:
    print(f"El numero menor es: {numero1}")
    print("\n")
if numero2 > numero1 and numero2 > numero3 and numero2 > numero4:
    print(f"El numero mayor es: {numero2}")
elif numero2 < numero1 and numero2 < numero3 and numero2 < numero4:
    print(f"El numero menor es: {numero2}")
    print("\n")
if numero3 > numero1 and numero3 > numero2 and numero3 > numero4:
    print(f"El numero mayor es: {numero3}")
elif numero3 < numero1 and numero3 < numero2 and numero3 < numero4:
    print(f"El numero menor es: {numero3}")
    print("\n")
if numero4 > numero1 and numero4 > numero2 and numero4 > numero3:
    print(f"El numero mayor es: {numero4}")
elif numero4 < numero1 and numero4 < numero2 and numero4 < numero3:
    print(f"El numero menor es: {numero4}")
    print("\n")
else:
    print(f"No hay numero mayor o menor, los numeros ingresados son iguales")
print("\n")
print("\n")


# --- End of file ---
