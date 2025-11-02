# Damos la bienvenida y mostramos el menu con unos prints(menu)
print("Bienvenido a el restaurante Dobar Tek!")
print("")
print("Menu: ")
print("")
print("Ensalada mixta  -------------- 12  EU")
print("Sopa de pescado -------------- 10  EU")
print("Dorada al horno -------------- 18  EU")
print("Arroz al curry --------------- 14  EU")
print("Lasaña de carne -------------- 15  EU")
print("Brownie de chocolate --------- 8,0 EU")
print("Helado ----------------------- 6,0 EU")
print("Refrescos -------------------- 5,5 EU")
print("Café ------------------------- 3,5 EU")
print("")

# Variables de las opciones del menu.
ensalada_mixta  = 12 # 1
sopa_de_pescado = 10 # 2
dorada_al_horno = 18 # 3
arroz_al_curry  = 14 # 4
lasaña_de_carne = 15 # 5
brownie_de_chocolate = 8 # 6
helado    = 6      # 7
refrescos = 5,5    # 8
cafe      = 3,5    # 9
compra    = 0      # Compra es 0 porque no a comprado nada aun..

# Le pedimos cuantos platos va a querer.
platos = int(input("Cual es la cantidad de platos que va a pedir?: "))

# Si platos es 0 imprimimos "Hasta luego!", pues no va a querer nada.
if platos == 0:
    print("Entonces hasta luego!")

print("")
# For i in range(platos), platos es la cantidad que se va a repitir el bucle.
for i in range(platos):

    # Condiciones para sumar a la variable "compra", el valor de cada plato (1 = ensalada_mixta) (ensalada_mixta = 12 EU)
    numero_plato = int(input("Ingrese el numero de su plato: "))
    if numero_plato == 1:
        compra = compra + 12
    elif numero_plato == 2:
         compra = compra + 10
    elif numero_plato == 3:
         compra = compra + 18
    elif numero_plato == 4:
         compra = compra + 14
    elif numero_plato == 5:
         compra = compra + 15
    elif numero_plato == 6:
         compra = compra + 8
    elif numero_plato == 7:
         compra = compra + 6
    elif numero_plato == 8:
         compra = compra + 5.5
    elif numero_plato == 9:
         compra = compra + 3.5

# Conversion de euro a dolares. Un dolar es 0.95 euros.
euro = 1
dolar_vs_euro = 0.95
conversion = euro / dolar_vs_euro

# Mensaje final.
print("")        
print("Numero de platos:", platos)
print("") 
print("Cuenta:", compra, "EU")
print("") 
print("El costo de su pedido en dolares es:", compra / dolar_vs_euro)
print("")