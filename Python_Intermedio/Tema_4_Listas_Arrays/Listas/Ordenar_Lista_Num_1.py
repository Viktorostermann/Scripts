# Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe -
# imprimir los componentes del número uno a uno por pantalla

# Solucion A:
print("\n")
numero = input ("Introduce un texto mencionando un numero entero mayor a 0 y menor a cinco: ")
print (numero[0])
print (numero[1])
print (numero[2])
print (numero[3])
print ("El numero introducido fue:" ,numero)
print("\n")

# calcula e imprima el número que resulta de leer el número introducido de derecha a izquierda. 
# Por ejemplo si el número introducido es 4532, el output deberá ser 2354. 

# Solucion B:
print ("El numero introducido a la inversa es:")
print (numero[3])
print (numero[2])
print (numero[1])
print (numero[0])