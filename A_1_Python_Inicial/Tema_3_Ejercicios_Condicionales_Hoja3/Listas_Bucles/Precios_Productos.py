''' Analisis de precio
Escribir un programa en Python que analice una lista de precios
mas altos, el precio mas bajo y el precio promedio de la lista.
Solucione el ejercicio sin utilizar la funcion max() o min().
'''
print("\n")
print("------------------------------------------------------------------------------------------")
# --- Definicion de lista de precios
#precios = [13.99, 12.99, 14.99, 13.76, 12.50, 11.98]
precios = [13.99, 13.99, 13.99, 13.99, 13.99, 13.99]
precio_total = 0
precio_max = 0.0
precio_min = float('inf')

# --- Bucle para recorrer la lista de precios
for precio in precios:
# --- IF Statement para determinar el precio mas alto y el precio mas bajo
## Comprobamos si el precio es mayor que el precio anterior
    if precio > precio_max:
       precio_max = precio    
## Comprobamos si el precio es menor que el precio anterior
    if precio < precio_min:
       precio_min = precio

## Sumamos los valores de la lista
    precio_total += precio

#print(precio_max)
#print(precio_min)
#print(precio_total)

# --- Calcular el precio promedio
precio_promedio = precio_total / len(precios)

# --- Imprimir por pantalla el resultado
print("Precio más alto:", precio_max)
print("Precio más bajo:", precio_min)
print("Precio promedio:", precio_promedio)

if precio_max == precio_min:
    print("Todos los precios son iguales")
else:
    print("Los precios son diferentes")

print("\n")
print("------------------------------------------------------------------------------------------")