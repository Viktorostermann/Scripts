
# --- Funciones y Argumentos
print("")
# --- Sumatoria --- # 
print("Sumatoria")
def sum_vals(a, b):
    print(f"{a} + {b} = ", a + b)
sum_vals(4,2)
print("")

# --- Sustraccion --- # 
print("Sustraccion")
def substract(a, b):
    print(f"{a} - {b} = ", a - b)
substract(7,5)
print("")

# --- Sustraccion con argumento default --- #
print("Sustraccion con argumento default")
def substract(a, b=10):
    print(f"{a} - {b} = ", a - b)
substract(1)
print("")