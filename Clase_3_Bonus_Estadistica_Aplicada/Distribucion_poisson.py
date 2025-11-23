import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# 1. Simulación del proceso de dropout

# Parámetros
num_neuronas = 100
lambda_poisson = 0.5
num_iteraciones = 1000

# Función para simular el dropout usando distribución de Poisson
def simular_dropout(num_neuronas, lambda_poisson):
    return poisson.rvs(mu=lambda_poisson, size=num_neuronas)
    # Esta función se llama para cada una de las 100 neuronas, y así determinamos cuántas de ellas se desactivan en cada iteración.

# Simular el dropout en 1000 iteraciones
neurons_off_counts = []

for _ in range(num_iteraciones):
    dropout_mask = simular_dropout(num_neuronas, lambda_poisson)
    num_neurons_off = np.sum(dropout_mask)
    neurons_off_counts.append(num_neurons_off)

# 2. Calcular y mostrar el número medio de neuronas desactivadas
mean_neurons_off = np.mean(neurons_off_counts)
print(f'Número medio de neuronas desactivadas en {num_iteraciones} iteraciones: {mean_neurons_off:.2f}')

# 3. Graficar la distribución de neuronas desactivadas
plt.hist(neurons_off_counts, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title('Distribución de Neuronas Desactivadas en 1000 Iteraciones')
plt.xlabel('Número de Neuronas Desactivadas')
plt.ylabel('Frecuencia')
plt.show()