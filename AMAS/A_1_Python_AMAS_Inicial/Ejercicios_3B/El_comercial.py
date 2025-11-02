'''Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
programa para realizar un seguimiento de los productos que has vendido y el valor total de las
ventas. Supongamos que hay un total de 10 productos.
Tú has vendido 5 de estos productos en las siguientes cantidades:

Producto 1: 3 unidades
Producto 2: 1 unidad
Producto 5: 7 unidades
Producto 6: 2 unidades
Producto 9 : 4 unidades'''

# --- Lista de productos y precios
# --- Lista de unidades vendidas de cada producto
precio_productos = [30.0, 9.8, 42.5, 35.6, 71.5, 44.0, 21.2, 53.2, 25.3, 57.8]
unidades_producto = [3, 1, 0, 0, 7, 2, 0, 0, 4, 0]
#facturacion_productos=[]

total_ventas = sum(unidades_producto)

# --- Bucle que recorra los productos (precios + unidades vendidas)
dinero_total = 0
for i in range(0, len(precio_productos)):
    dinero_x_producto = precio_productos[i] * unidades_producto[i]
    #facturacion_productos.append(dinero_x_producto)
    dinero_total = dinero_total + dinero_x_producto
    print(f"El dinero facturado por el producto {i+1} es de {dinero_x_producto} euros")

# --- Imprimir resultados
print("El numero total de unidades vendidas es de: ", total_ventas)
print("El dinero total facturado es de: ", dinero_total)

# Output:
# --- Calcular el valor total de las ventas
# --- Calcular el dinero facturado por cada producto
# --- Calcular el dinero total