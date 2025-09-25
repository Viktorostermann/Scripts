''' Realizar un programa que pida el radio de un 
circulo y devuelva por pantalla el valor del area y su perimetro 
de dicho circulo'''

# --- Definimos las variables y declaramos las variables


# --- Pedimos el input al usuario que ingrese el radio del circulo ----
radio = float(input("Ingrese el radio del circulo: "))
print(" ")

# --- Calculamos el valor del perimetro ----
Perimetro = 2 * 3.14 * radio

# --- Calculamos el valor del area ----
Area = 3.14 * (radio ** 2)

# --- Mostramos el valor del Área y el perimetro del circulo ----
print("El area del circulo es: " ,Area , "Y el valor del Perimetro es:" ,Perimetro)
