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
ensalada_mixta  = 12
sopa_de_pescado = 10
dorada_al_horno = 18
arroz_al_curry  = 14
lasaña_de_carne = 15
brownie_de_chocolate = 8
helado = 6
refrescos = 5.5
cafe  = 3.5
total = 0 # Compra es 0 porque no a comprado nada aun..

# Le pedimos cuantos platos va a querer.
cant_ensal  = int(input("Cual es la cantidad de Ensalada mixta que va a pedir?: "))
cant_sopa   = int(input("Cual es la cantidad de Sopa de pescado que va a pedir?: "))
cant_dorada = int(input("Cual es la cantidad de Dorado al horno que va a pedir?: "))
cant_arroz  = int(input("Cual es la cantidad de Arroz al curry que va a pedir?: "))
cant_lasaña = int(input("Cual es la cantidad de Lasaña que va a pedir?: "))
cant_browni = int(input("Cual es la cantidad de Brownie de chocolate que va a pedir?: "))
cant_helado = int(input("Cual es la cantidad de Helado que va a pedir?: "))
cant_refres = int(input("Cual es la cantidad de refrescos que va a pedir?: "))
cant_cafe   = int(input("Cual es la cantidad de café que va a pedir?: "))

# Calculamos el total
total = cant_ensal * ensalada_mixta     + \
    cant_sopa * sopa_de_pescado         + \
    cant_dorada * dorada_al_horno       + \
    cant_arroz * arroz_al_curry         + \
    cant_lasaña * lasaña_de_carne       + \
    cant_browni * brownie_de_chocolate  + \
    cant_helado * helado                + \
    cant_refres * refrescos             + \
    cant_cafe * cafe
print (" La cuenta total es : ", total ,"Euros")