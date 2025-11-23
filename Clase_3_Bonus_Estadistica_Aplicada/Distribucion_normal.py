
import scipy.stats as stats

# Parámetros de la distribución normal
mu = 170  # Media
sigma = 12  # Desviación estándar

# Definir los límites del intervalo
x1 = 189  # Límite inferior del intervalo
x2 = 190  # Límite superior del intervalo

# x1 = 174  # Límite inferior del intervalo
# x2 = 175  # Límite superior del intervalo


# Calcular la probabilidad P(x1 < X < x2) donde X ~ N(mu, sigma)
# Usamos la función de distribución acumulativa (CDF) de la distribución normal
prob = stats.norm.cdf(x2, mu, sigma) - stats.norm.cdf(x1, mu, sigma)

# Imprimir el resultado 
print(f"La probabilidad de que un alumno mida entre {x1} cm y {x2} cm es aproximadamente {prob*100:.4f} %")
