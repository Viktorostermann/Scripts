# --- Pedir un numero al usuario
numero = input(" Introduce un numero entero")
numero = int(numero)


# --- Comprobar si el numero es multiplo de 3
# Si es multiplo, indicamos por pantalla

if numero % 3 == 0:
   print("Este numero ", numero, " es multiplo de 3")

# Si no es, indicamos por pantalla
else:
   print("Este numero ", numero, " no es multiplo de 3")