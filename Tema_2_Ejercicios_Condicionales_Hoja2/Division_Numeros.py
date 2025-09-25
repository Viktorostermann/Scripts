# --- Pedir un numero al usuario
print("\n")
numero_1 = float(input(" Introduce el dividendo: "))
numero_2 = float(input(" Introduce el divisor: "))
print("\n")

# --- Comprobar si el numero es cero
# Si es cero, realizamos la division
if numero_1 == 0.0 or numero_2 == 0.0:
   print("La division entre", numero_1, "y" , numero_2 ,"no es una operación valida, no se puede dividir entre ceros (0)")
   print("\n")

# Si no es cero, indicamos por pantalla el error
else:
   division = numero_1 / numero_2
   print("El resultado de dividir",numero_1 ,"entre" , numero_2, "es" , division)
   print("\n")
   print("\n")
