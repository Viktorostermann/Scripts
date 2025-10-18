'''8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un
parámetro "fahrenheit" y devuelva su equivalente en grados Celsius.'''

print("\n")
def convertir_fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

# --- Ejemplo de uso de la función
temp_fahrenheit = 100
temp_celsius = convertir_fahrenheit_a_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit} grados Fahrenheit son {temp_celsius:.2f} grados Celsius.")

print("\n")
