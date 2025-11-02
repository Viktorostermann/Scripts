''' Evitar crashes de un programa '''
print("")
print(""" Este programa divide dos numeros introducidos por el usuario.
Si alguno de los valores introducido no son numericos o si el segundo valor es cero,
el programa mostrara un mensaje de error y continuara solicitando nuevos datos """)

print("")
print (" Dame dos numeros para dividir: ")
print("")
print (" introduce 's' para salir. ")
print("")

while True:
    numero1 = input ("\nPrimer numero: ")
    if numero1 == 's':
        print("Salida del programa.")
        #if numero1 == 0:
         #   print ("El numero no puede ser cero. Intenta de nuevo.") 
            # break
        break

    numero2 = input ("Segundo numero: ")
    if numero2 == 's':
        print("Salida del programa.")
        break

    else:
        #try-except-else
        try:
            resultado = int(numero1) / int(numero2)
        except ZeroDivisionError:
            print ("No se puede dividir entre cero.")
        else:
            print ("El resultado es: ", resultado)


