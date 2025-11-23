import numpy as np
import matplotlib.pyplot as plt
# scikit-learn removed to avoid unresolved import; use numpy.polyfit instead
from scipy.stats import pearsonr, spearmanr

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Variable independiente (reshape para convertirlo en una matriz columna)
Y = np.array([2, 3, 5, 7, 11])  # Variable dependiente

#ajustar el modelo usando numpy.polyfit (evita dependencia de scikit-learn)
coeffs = np.polyfit(X.flatten(), Y, 1)  # devuelve [pendiente, intercepto]
b = coeffs[0]
a = coeffs[1]

Y_pred = b * X.flatten() + a

print(f"Intersección (a): {a}")
print(f"Pendiente (b): {b}")

#calculo de la correlacion pearson
correlacion_pearson, _ = pearsonr(X.flatten(), Y)

#Calcular el coeficiente de Spearman
correlacion_spearman = spearmanr(X.flatten(), Y)

print(f"Coeficiente de correlación de Pearson: {correlacion_pearson}")
print(f"Coeficiente de correlación de Spearman: {correlacion_spearman}")

plt.scatter(X,Y,color='blue') #Datos originales
plt.plot(X,Y_pred,color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Lineal')
plt.show()