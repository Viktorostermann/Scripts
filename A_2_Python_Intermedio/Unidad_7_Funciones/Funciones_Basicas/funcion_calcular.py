'''3. Escribe una función llamada "calcular_area_rectangulo" que tome dos
parámetros "base" y "altura" y calcule el área de un rectángulo.'''

def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    area = base * altura
    print("El área del rectángulo es:", area)

# Llamada a la función
calcular_area_rectangulo(5, 10)
calcular_area_rectangulo(base=7, altura=3) # Argumentos con nombres diferentes