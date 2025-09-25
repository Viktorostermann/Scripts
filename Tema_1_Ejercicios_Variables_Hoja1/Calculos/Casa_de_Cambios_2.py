#---- Pedimos el input al usuario que ingrese la cantidad EUROS ----
euros = input ("Ingres la cantidad de euros que deseas convertir")

#---- Convertir la cantidad de EUROS ingresada en float ----
euros = float (euros)

#---- Convertir la cantidad de EUROS en USD ----
dolares = euros * 1.2

#---- Calculamos la cantidad con la cual se queda la casa de cambios ----
tasas_gestion = dolares * 0.1

#---- Calculamos la cantidad de dolares que recibe el usurio ----
dolares_recibidos = dolares - tasas_gestion

#----Muestra la cantidad de EUROS en USD ----
print(" ")
print ("Monto ingresado:" , euros, "Euros")
print(" ")
print ("Conversión en EUR --> USD:" , dolares, "Dólares")
print(" ")
print ("Tasa de gestion en Dólares:" , tasas_gestion, "Dólares")
print(" ")
print ("Total monto a recibir:" , dolares_recibidos, "Dólares")
print(" ")