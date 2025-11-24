print("-----------------------------------------")
print("| MAS ACELERACION! = 100 monedas        |")
print("| MAS ATAQUE = 50 monedas               |")
print("-----------------------------------------")

monedas = int(input("¿Cuántas monedas tienes?: "))

if monedas >= 100:
    print("Puedes comprar el power up de aceleración!")
    monedas -= 100  # Restar las monedas después de la compra
    print("Te quedan", monedas, "monedas.")

    respuesta = input("¿Quieres comprar un power up de ataque? (Si/No): ")
    if respuesta.lower() == "si":
        if monedas >= 50:
            monedas -= 50  # Restar las monedas por la compra del ataque
            print("¡Pudiste comprar todos los power ups! :D")
            print("Te quedan", monedas, "monedas.")
        else:
            print("No puedes comprar el power up de ataque :c")
    elif respuesta.lower() == "no":
        print("¡Ok! Saliste de la tienda! :D")
else:
    print("No tienes suficientes monedas para comprar el power up de aceleración.")