# --- Añadir Numeros pares e Impares a la lista, ejemplo sintaxis: Nombre_Variable(list_range_Numeros)) ---
print("------------------------------------------------------------------------------------------")
print("-----Añadir Numeros pares e Impares-----")
Num_Pares = list(range(2,12,2)) # Esta instruccion se lee que el indice va de numero 2 hasta 10 con paso de dos en dos.
Num_Impar = list(range(1,13,2)) # Esta instruccion se lee que el indice va de numero 1 hasta 11 con paso de dos en dos.

for i in Num_Impar:
    if i %2 != 0:
        print("Hemos pasado el numero Par " , i )
    i = i + 1
else:
     for y in Num_Pares:
        if y %2 == 0:
            print("Hemos pasado el numero Impar " , y) 
            y = y + 1

print("----------------------------------------------------------------------------------------------------------")
print("\n")