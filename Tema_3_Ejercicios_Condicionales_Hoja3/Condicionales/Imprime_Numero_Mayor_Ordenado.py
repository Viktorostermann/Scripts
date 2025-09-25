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
# --- Ejemplo: if (a>b): a, b = b, a / if (b>c): b, c = c, b / if (c>d): c, d = d, c / print(f"El numero mayor es: {d}") print(f"El orden de los numeros es: ", {a}, {b}, {c}, {d})
print("\n")
if (numero1>numero2): # Utilizamos una tecnica de intercambio de valores entre variables
    numero1, numero2, = numero2, numero1
print("\n")
if (numero2>numero3):
    numero2, numero3 = numero3, numero2
print("\n")
if (numero3>numero4):
    numero3, numero4 = numero4, numero3
print("\n")
print(f"El numero mayor de los cuatro es: {numero4}") 
print("\n")
print(f"El orden de los numeros es: ", {numero1}, {numero2}, {numero3}, {numero4})
print("\n")
print("\n")
# --- End of file ---
