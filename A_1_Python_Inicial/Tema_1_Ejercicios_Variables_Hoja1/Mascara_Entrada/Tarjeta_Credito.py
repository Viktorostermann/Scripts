# Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos los caracteres en forma de asterisco
print("")
num_tarjeta = input("Ingrese un numero de tarjeta de credito (16) digitos. Ejemplo: 1234-2345-3456-5678 ") 

# Opcion: B
# Determina longitud de los numeros de la tarjeta
longitud = len(num_tarjeta)
print("\n")

# El output deberá ser **** **** **** 5678 Los 4 ultimos digitos.
print("")
print ("*" * (longitud-4) + num_tarjeta [longitud-4:longitud])
print("")