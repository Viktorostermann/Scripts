def min_val(a, b):
    """Retorna el valor mínimo entre a y b."""
    return a if a < b else b

def max_val(a, b):
    """Retorna el valor máximo entre a y b."""
    return a if a > b else b

# Ejemplo de uso
num1 = 15
num2 = 30

print(min_val(num1, num2))  # Imprimirá 15
print(max_val(num1, num2))  # Imprimirá 30