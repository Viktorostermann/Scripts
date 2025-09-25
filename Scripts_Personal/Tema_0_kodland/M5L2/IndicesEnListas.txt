list = ["cero", "primero", "segundo", "tercero"]
print(list[0])

for i in range(4):
    print(i, list[i])
    # I = 0, (La primera vez que se repite el bucle)
    # Despues que el bucle for termine, I += 1
    # Despues imprimira el valor de i, (La primera vez q se repite:)
    # 0 <---- Valor de i la primera vez
    # list = "["cero", "primero", "segundo", "tercero"]
    #          ^^^^^^^  ^^^^^^^     ^^^^^^^   ^^^^^^^^
    #         Indice 0, Indice 1,  Indice 2,  Indice 3