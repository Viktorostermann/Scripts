# Solicitar al usuario que ingrese tres números enteros
numero1 = int(input('Ingresa el primer número: '))
numero2 = int(input('Ingresa el segundo número: '))
numero3 = int(input('Ingresa el tercer número: '))

# Determinar cuál es el infiltrado
if numero1 == numero2:
    infiltrado = numero3
elif numero1 == numero3:
    infiltrado = numero2
else:
    infiltrado = numero1

# Mostrar el resultado
print("El infiltrado es:", {infiltrado})