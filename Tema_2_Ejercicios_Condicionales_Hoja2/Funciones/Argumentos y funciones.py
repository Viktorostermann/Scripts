
# --- Funciones y Argumentos
# --- Sumatoria --- # 
def sum_vals(a, b):
    print(a + b)
    sum_vals(4,2)

# --- Sustraccion --- # 
def substract(a, b):
    print(a - b)
    substract(7,5)

# --- Sustraccion con argumento default --- #
def substract(a, b=10):
    print(a - b)
    substract(1)