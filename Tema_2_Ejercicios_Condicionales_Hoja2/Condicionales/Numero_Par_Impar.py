# --- Pedir un numero al usuario
print("\n")
numero = input(" Introduce un numero entero: ") # <--- recordar que esta linea es un string hay que convertir a numero
numero = int(numero) # <--- se cconvierte a numero el sting anterior
print("\n")

# --- Comprobar si el numero es par o impar o multiplo de 2

# Si es multiplo, indicamos por pantalla si es par
# Si No es multiplo, indicamos por pantalla no es par
if numero % 2 == 0:
   print("El numero", numero, "es multiplo de 2 y es par ") 
   print ("\n")
# Si no es, indicamos por pantalla que npo es par

else:
   print("El numero", numero, "no es multiplo de 2 es impar ")
   print("\n")