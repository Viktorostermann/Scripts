# Pedir Usuario ingrese 3 numeros sumar y comparar para indicar que suma es igual a otro numero.

# --- Pedir al usuario que ingrese 3 numeros
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))

# --- Comprobacion si alguno de los numeros ingresados es igual a la suma de los otros dos
# --- Ejemplo: if (x==y+z): print("El primer numero es la suma de los otros dos") / if (y==x+z): print("El segundo numero es la suma de los otros dos") / if (z==x+y): print("El tercer numero es la suma de los otros dos") / else: print("La suma de los numeros ingresados no es igual a ningun numero ingresado")  
print()
if numero1 == numero2+numero3 or numero2 == numero3+numero1 or numero3 == numero1+numero2:

    print(f"La suma de los numeros ingresados es igual a otro numero de los numeros ingresado")
else:
    print(f"El resultado de la suma y comparacion de los numeros ingresados no son iguales entre si")
# --- End of file --
