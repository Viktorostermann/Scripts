# --- Creando una lista numerica de cuadrados
print("----Cuadrados del 1 al 11----")
print("\n")
List_Num_Scuare = list()
for valor in range(0,12): # ira del 0 al 10
    print(List_Num_Scuare)
    cuadrado = valor**2
    List_Num_Scuare.append(cuadrado)
print("\n")
print("Lista total de numeros cuadrados de: " , range(0,12))
print("------------------------------------------------------------------------------------------")
print("\n")

# --- Creando otra lista numerica pero de cuadrados comprimida
print("----Numeros Cuadrados----")
print("\n")
List_Num_Scuare = [valor**2 for valor in range(0,11)]
for i in List_Num_Scuare:
    print("El cuadrado de:", i ,"Es" , i **2 )
print("\n")
print("------------------------------------------------------------------------------------------")
print("\n")