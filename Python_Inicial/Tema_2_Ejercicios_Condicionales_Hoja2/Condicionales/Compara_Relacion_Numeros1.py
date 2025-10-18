# Pedir Usuario ingrese 3 numeros sumar y comparar para indicar que suma es igual a otro numero.

# --- Pedir al usuario que ingrese 3 numeros
numero1 = int(input("Ingrese el primer numero: "))
print(f"El numero ingresado es: {numero1}")
numero2 = int(input("Ingrese el segundo numero: "))
print(f"El numero ingresado es: {numero2}")
numero3 = int(input("Ingrese el tercer numero: "))
print(f"El numero ingresado es: {numero3}")
suma = 0

# --- Comprobacion si alguno de los numeros ingresados es igual a la suma de los otros dos
# --- Ejemplo: if (x==y+z): print("El primer numero es la suma de los otros dos") / if (y==x+z): print("El segundo numero es la suma de los otros dos") / if (z==x+y): print("El tercer numero es la suma de los otros dos") / else: print("La suma de los numeros ingresados no es igual a ningun numero ingresado")  
suma= numero1 + numero2 or numero1 + numero3 or numero2 + numero3
if numero1 + numero2 == numero3: 
    print(f" La suma de los numeros ingresados: {numero1} + {numero2} es igual a {numero3}")    
if numero1 + numero3 == numero2:
    print(f" La suma de los numeros ingresados: {numero1} + {numero3} es igual a {numero2}") 
if numero3 + numero2 == numero1: 
    print(f" La suma de los numeros ingresados: {numero3} + {numero2} es igual a {numero1}")
if suma != numero1 and suma != numero2 and suma != numero3:
    print(f" La suma de los numeros ingresados no es igual a ningun numero ingresado")
# --- End of file --
