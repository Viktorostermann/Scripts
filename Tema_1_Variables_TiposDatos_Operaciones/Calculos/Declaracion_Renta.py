# --- Pedir datos al usuario
## Edad

edad = int(input("Ingrese su edad: "))
print("\n")
## Ingresos
ingresos = float(input("Ingrese sus ingresos mensuales: "))
print("\n")


# --- Comprobar si debe aplicar el impuesto y cual es el importe
## Comprombar si la persona es mayor de edad y su nivel de ingresos
if edad >= 18 and ingresos > 1000:

    # --- Calcular la renta anual
    renta_anual = ingresos * 12
    print(f"Su renta anual es: {renta_anual}")
    print("\n")
    # --- Comprobar en que tramo se encuentra
    if renta_anual <= 15000:
        print("No tiene obligacion tributaria")
    elif renta_anual <= 15000 and renta_anual < 25000:
        print("Debe pagar un 5% de impuestos")
    elif renta_anual <= 25000 and renta_anual < 35000:
        print("Debe pagar un 15% de impuestos")
    elif renta_anual <= 35000 and renta_anual < 600000:
        print("Debe pagar un 20% de impuestos")
    else:
        print("Debe pagar un 45% de impuestos")
# Si el usuario no esta en rango de edad o ingresos, no se aplica impuesto.
## Imprimir que no tiene obligacion tributaria
else:
    print("No tiene obligacion tributaria")
    print("\n")
# --- End of file ---
