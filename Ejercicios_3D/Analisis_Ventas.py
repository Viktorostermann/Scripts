''' Eres el propietario de una tienda en linea, 
y tienes una lista de ventas de los utimos 30 dias. 
Quieres analizar las ventas por dia de la semana, 
para idenftificar patrones y tendencias de mayor venta.
'''

# Lista con las ventas del mes
ventas = [100, 200, 150, 300, 250, 400, 350,]

# Lista con los dias de la semana
dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Lista donde guardar las ventas por dia de la semana
ventas_totales = [0, 0, 0, 0, 0, 0, 0]

# Lista de ventas totales del mes
ventas_totales_mes = [0, 0, 0, 0, 0, 0, 0]

# Recorrer la lista de ventas con bucle
dia_venta = 0
for venta in ventas:
    # Sumar la venta a la lista de ventas por dia de la semana
    ventas_totales [dia_venta] = ventas_totales[dia_venta] + venta
    # Incrementar el dia de la semana
    dia_venta = dia_venta + 1
    # Si el dia de la semana es 7, volver a 0
    if dia_venta == 7:
        dia_venta = 0
    # Imprimir las ventas realizadas para cada dia de la semana
    print(f"La venta del dia {dia_venta} es de {venta}")
   
## Imprimir las ventas realizadas para cada dia de la semana
print("\n")
for i in range(len(dias_semana)):
    print(f"Las ventas del dia {dias_semana[i]} son {ventas_totales[i]}")

# Imprimir las ventas totales en el año 
print("Ventas totales en el año:", sum(ventas_totales))

# imporimir el dia de la semana con mayor venta
dia_max = ventas_totales.index(max(ventas_totales))
print("El dia de la semana con mayor venta es:", dias_semana[dia_max])

## a lo largo del mes