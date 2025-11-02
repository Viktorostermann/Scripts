# Escribe un programa que pida al usuario dos números enteros y muestre por pantalla los números de entrada, el cociente y el resto.
print("")
numero_1 = int (input ("Introduce un numero entero: "))
print("")
numero_2 = int (input ("Introduce otro numero entero: "))
print("")

# Calculamos el cociente
cociente = numero_1 // numero_2

# Calculamos el residuo 
residuo = numero_1 % numero_2
print (" ")
print ("Los numeros de entrada son ", numero_1 , "Y", numero_2)
print (" ")
print ("El cociente de los numeros de entrada en una operacion es: ", cociente)
print (" ")
print ("El residuo de los numeros de entrada en una operacion es: ", residuo)
print ("\n")