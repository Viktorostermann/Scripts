'''9. Escribe una función llamada "calcular_edad" que tome dos parámetros:
"año_actual" y "año_nacimiento" y calcule la edad de una persona.'''

print("\n")
def calcular_edad(año_actual, año_nacimiento):
    edad = año_actual - año_nacimiento
    return edad

# --- Ejemplo de uso de la función
año_actual = 2025
año_nacimiento = 1980
edad = calcular_edad(año_actual, año_nacimiento)
print(f"Si naciste en {año_nacimiento}, en el año {año_actual} tienes {edad} años.")
print("\n")