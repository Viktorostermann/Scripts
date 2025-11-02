# Paso 1 ---- Pedimos al usuario que ingrese los precios de venta correspondientes a los vehiculos ----
auto_rbm_Serie_1 = input ("Introduzca el precio de venta correspondiente al RBM Serie 1")
auto_rbm_Serie_Plus = input ("Introduzca el precio de venta correspondiente al RBM Plus")
auto_rbm_Serie_All_Terrain = input ("Introduzca el precio de venta correspondiente al All Terrain")

# Paso 2 ---- Asignamos el precio de venta a las variables de los vehiculos ----
precio_venta_serie_1 = 20000
precio_venta_serie_plus = 35000
precio_venta_serie_all_terrain = 60000

# Paso 3 ---- Comisiones por Venta de vehiculos ----
comision_serie_1 = float (precio_venta_serie_1) * 3 / 100.00
comision_serie_plus = float (precio_venta_serie_plus) * 5 / 100.00
comision_serie_all_terrain = float (precio_venta_serie_all_terrain) * 7 / 100.00

# Paso 4 ---- Pedir Cantidad de vehiculos vendidos en el mes ----
venta_serie_1 = input ("Cuantos vehiculos Serie 1 se vendieron?:")
mes_venta_serie_1 = input ("Introduzca el mes de venta Vehiculos Serie 1:")
venta_rbm_Plus = input ("Cuantos vehiculos RBM Plus se vendieron en el mes?:")
mes_venta_Plus = input ("Introduzca el mes de venta Vehiculos Plus:")
venta_All_Terrain = input ("Cuantos vehiculos Serie 1 se vendieron en el mes?:")
mes_venta_All_Terrain = input ("Introduzca el mes de venta Vehiculos All Terrain:")

# Paso 5 ---- Imprimir reportes vehiculos vendidos en el mes ----
print (" ")
print ("La cantidad de vehiculos RBM Serie_1 vendidos durante el mes:", mes_venta_serie_1 + "son", venta_serie_1 + "y la comison es" ,comision_serie_1)
print (" ")
print ("La cantidad de vehiculos RBM Plus vendidos durante el mes:", mes_venta_Plus + "son", venta_rbm_Plus + "y la comision es" ,comision_serie_plus)
print (" ")
print ("La cantidad de vehiculos All Terrain vendidos durante el mes:", mes_venta_All_Terrain + "son", venta_All_Terrain + "y la comision es" ,comision_serie_plus)









