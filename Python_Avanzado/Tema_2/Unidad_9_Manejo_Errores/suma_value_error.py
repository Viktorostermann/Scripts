'''
Un problema común al solicitar una entrada numérica ocurre cuando las personas ingresan texto en lugar de números. 
Cuando intentas convertir la entrada a un entero (int), obtendrás un ValueError. 
Escribe un programa que solicite dos números. Suma los números y muestra el resultado. 
Captura el ValueError si alguno de los valores de entrada no es un número e imprime un mensaje de error amigable. 
Prueba tu programa ingresando dos números y luego ingresando texto en lugar de un número. 
Envuelve tu código del en un bucle while para que el usuario pueda continuar ingresando números 
incluso si comete un error ingresando texto en lugar de un número.
'''
# Envolver en un bucle while infinito - break para salir
# Pedir dos numeros al usuario
# Controlar el error: ValueError
# Sumar los dos numeros e imprimir el resultado

# Ejemplo_1: 
while True:
    try:
        num1 = int(input("Introduce el primer numero: "))   
        num2 = int(input("Introduce el segundo numero: "))
    except ValueError:
        print("Error: Debes introducir un numero entero, o un numero valido, no texto.")
    else:
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es: {suma}")
    break

# Ejemplo_2:
'''
while True:
    try:
        num1 = int(input("Introduce el primer numero: "))   
        num2 = int(input("Introduce el segundo numero: "))
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es: {suma}")
        break
    except ValueError:
        print("Error: Debes introducir un numero entero, o un numero valido, no texto.")
'''