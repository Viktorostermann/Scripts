# --- Pedir al usuario ingrese un numero entero ---

num = int(input("Introduzca el ancho de fila (numero entero): "))
#num = 5
# --- Validar que el numero sea un entero ---
for i in range(1, num + 1):
    print("*" *i + " " * (num+i))

# --- Bucle descendente ---
    for i in range(num - 1,0,-1):
        print("*" *i + " " * (num-i))