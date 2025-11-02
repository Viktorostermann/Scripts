# Paso 1 ---- Pedimos al usuario que ingrese los tiempos de los participantes de las olimpiadas ----
tiempo_hannah = input ("Ingrese el tiempo de Hannah Neise (Fomrato: minutos segundos centésimas:")
tiempo_jackie = input ("Ingrese el tiempo de Hannah Neise (Fomrato: minutos segundos centésimas:")
tiempo_Kimberley = input ("Ingrese el tiempo de Hannah Neise (Fomrato: minutos segundos centésimas:")

# Paso 2 ---- Conversion de los tiempos de los competidores ---- Opcion: (1) 
#minutos_hanna = input ("Ingrese los minutos para Hannah")
#segundos_hanna = input ("Ingrese los minutos para Hannah")
#entesimas_hanna = input ("Ingrese los minutos para Hannah")

# Paso 3 ---- Extraer minutos segundos y centésimas ---- Opcion: (2) 
minutos_hannah, segundos_hannah, centesimas_hannah = tiempo_hannah.split(" ")
minutos_jackie, segundos_jackie, centesimas_jackie = tiempo_jackie.split(" ")
minutos_Kimberley, segundos_Kimberley, centesimas_Kimberley = tiempo_Kimberley.split(" ")

# Paso 3.1 ---- Conversion de los tiempos de los competidores ----
tiempo_hannah = float(minutos_hannah) * 60 + float(segundos_hannah) + float(centesimas_hannah) * 0.01
tiempo_Kimberley = float(minutos_Kimberley) * 60 + float(segundos_Kimberley) + float(centesimas_Kimberley) * 0.01
tiempo_jackie = float(minutos_jackie) * 60 + float(segundos_jackie) + float(centesimas_jackie) * 0.01

# Paso 4 ---- Calculamos la velocidad media ----
velocidad_hannah = 100.0/tiempo_hannah
velocidad_jackie = 100.0/tiempo_jackie
velocidad_kimberley = 100.0/tiempo_Kimberley

# Paso 5 ---- Imprime los resultados por pantalla ----
print(" ")
print(" La velocidad media de Hannah Neise fue es",  velocidad_hannah , "metros por segundo")
print(" ")
print(" La velocidad media de Jackie Narracott es", velocidad_jackie , "metros por segundo")
print(" ")
print(" La velocidad media de Kimberley Bos es", velocidad_kimberley , "metros por segundo")
print(" ")