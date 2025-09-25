import numpy as np
import matplotlib.pyplot as plt

# Función de activación (sigmoide)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Datos de entrada
inputs = np.array([0.5, 0.3, 0.2])

# Pesos y sesgo
weights = np.array([0.4, 0.6, 0.1])
bias = 0.1

# Cálculo de la salida de la neurona
output = sigmoid(np.dot(inputs, weights) + bias)

# Visualización
plt.plot(inputs, label='Inputs')
plt.plot(weights, label='Weights')
plt.axhline(y=output, color='r', linestyle='-', label='Output')
plt.legend()
plt.title('Comportamiento de una Neurona Artificial')
plt.show()