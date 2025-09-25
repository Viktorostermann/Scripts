# --- Añadir Numeros pares e Impares a la lista, ejemplo sintaxis: Nombre_Variable(list_range_Numeros)) ---

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Definimos el número máximo
num_max = 10

print("------------------------------------------------------------------------------------------")
print("----- Añadir Números Pares, Impares y Primos -----")

# Imprimir números desde 1 hasta num_max, identificando su tipo
for num in range(1, num_max + 1):
    if es_primo(num):
        print(f"Hemos pasado el número {num} (Primo)")
    elif num % 2 == 0:
        print(f"Hemos pasado el número {num} (Par)")
    else:
        print(f"Hemos pasado el número {num} (Impar)")

print("----------------------------------------------------------------------------------------------------------")
print("\n")
