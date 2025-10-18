# --- Pedimos un precio al usuario y lo guardamos en la variable precio
precio = float(input("Ingrese el precio: "))

# --- Comprobar el precio y ver si debemos comprar, holdear o vender
# --- Si el precio es menor a 1000, comprar
if precio <= 100.0:
    print("Es hora de Comprar")
elif precio < 100.0 and precio <= 200.0:
    print("Es hora de Holdear")
else: 
    print("Es hora de Vender")
    
# --- End of file ---



