# --- Crear un script para identificar que tipo de Haburguesa desea el cliente
# --- El cliente puede elegir Clasica o Vegetariana
hamburguesa = input("¿Qué tipo de hamburguesa desea? (Clasica o Vegetariana): ")

# --- Comprobar que tipo de hamburguesa desea el cliente
#  -- Si ha elegido la clasica
if hamburguesa.lower() == "clasica" or hamburguesa.lower() == "Clasica":
    ## -- Se ofrece opcion de elegir ingredientes extras: Queso, Bacon, Huevo
    ingrediente_extra = input("¿Desea algún ingrediente extra? (Queso, Bacon, Huevo): ")
    ## -- Imprimeremos que tipos de Hmaburguesa ha elegido
    if ingrediente_extra.lower() == "Queso" or ingrediente_extra.lower() == "queso":
        print(f"Ha elegido una hamburguesa clasica con Queso")
    elif ingrediente_extra.lower() == "Bacon" or ingrediente_extra.lower() == "bacon":
        print(f"Ha elegido una hamburguesa clasica con Bacon")
    elif ingrediente_extra.lower() == "Huevo" or ingrediente_extra.lower() == "huevo":
        print(f"Ha elegido una hamburguesa clasica con Huevo")
    else:
        print("La hamburguesa de este tipo, no esta disponible")
        print("Inicia tu pedido de nuevo")

# -- Si ha elegido la vegetariana
elif hamburguesa.lower() == "vegana" or hamburguesa.lower() == "Vegana":
    print("Ha elegido una hamburguesa clasica")
    ## -- Se ofrece opcion de elegir ingredientes extras: Tofu, Cebolla caramelizada
    ingrediente_extra = input(
        "¿Desea algún ingrediente extra? (Tofu, Cebolla caramelizada)."
    )
    ## -- Imprimeremos que tipos de Hmaburguesa ha elegido
    if ingrediente_extra.lower() == "Tofu" or ingrediente_extra.lower() == "tofu":
        print("Ha elegido una hamburguesa Vegana con Tofu")
    elif (
        ingrediente_extra.lower() == "Cebolla caramelizada"
        or ingrediente_extra.lower() == "cebolla caramelizada"
    ):
        print("Ha elegido una hamburguesa Vegana con Cebolla caramelizada")
    else:
        print("La hamburguesa de este tipo, no esta disponible")
        print("Inicia tu pedido de nuevo")
# -- Si ha elegido una opcion incorrecta
else:
    print("La hamburguesa no esta disponible")
## -- Imprimir que la hamburguesa no esta disponible
