count_n = 0
count_p = 0

while True:
    print("")
    x = int(input("Ingresa un número:"))
    if x > 0:
        print("")
        print("Este es un numero positivo")
        count_p = count_p + 1 
        
    elif x < 0:
        print("")
        print("Este es un numero negativo")
        count_n = count_n + 1
        
    else:
        print("Esto es cero")

    print("Numeros positivos: ", count_p, ". Numeros negativos: ", count_n)
    print("")