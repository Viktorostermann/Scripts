# Solicitar al usuario que ingrese el número del mes
mes = int(input('Ingresa el número del mes (1-12): '))

# Verificar si el mes es válido
if mes < 1 or mes > 12:
    print('Error: El mes debe estar entre 1 y 12.')
else:
    # Determinar la estación según el mes
    if mes in [12, 1, 2]:
        estacion_norte = 'invierno'
        estacion_sur = 'verano'
    elif mes in [3, 4, 5]:
        estacion_norte = 'primavera'
        estacion_sur = 'otoño'
    elif mes in [6, 7, 8]:
        estacion_norte = 'verano'
        estacion_sur = 'invierno'
    else:  # meses 9, 10, 11
        estacion_norte = 'otoño'
        estacion_sur = 'primavera'

    # Mostrar el resultado
    print("En el hemisferio norte es", {estacion_norte}, "y en el hemisferio sur es {estacion_sur}.")