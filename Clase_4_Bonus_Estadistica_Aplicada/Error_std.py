#Creo la población

import numpy as np
import matplotlib.pyplot as plt

# Crear una población con distribución normal (media=50, desviación estándar=10)
np.random.seed(42)
poblacion = np.random.normal(50, 10, 10000)

# Calcular la media real de la población
media_poblacion = np.mean(poblacion)
print(f"Media de la población: {media_poblacion:.2f}")




#TOMAMOS MUESTRAS DE LA POBLACIÓN

# Tamaño de la muestra
tamaño_muestra = 5 #PROBAR A BAJAR EL VALOR

# Número de muestras
num_muestras = 10 #DISMINUIR EL NUMERO DE MUESTRAS

# Calcular las medias de las muestras
medias_muestras = [np.mean(np.random.choice(poblacion, tamaño_muestra, replace=False)) for _ in range(num_muestras)]

# Calcular la media de las medias de las muestras
media_muestras = np.mean(medias_muestras)
print(f"Media de las medias de las muestras: {media_muestras:.2f}")



#CALCULO EL ERROR ESTANDAR DE LAS MUESTRAS

# Calcular la desviación estándar de las medias de las muestras (error estándar de la media)
error_estandar = np.std(medias_muestras, ddof=1)
print(f"Error estándar de la media: {error_estandar:.2f}")


#GRAFICO LOS RESULTADOS

# Graficar la distribución de las medias de las muestras
plt.figure(figsize=(10, 6))
plt.hist(medias_muestras, bins=30, edgecolor='k', alpha=0.7)
plt.axvline(media_poblacion, color='red', linestyle='dashed', linewidth=2, label='Media Poblacional')
plt.axvline(media_muestras, color='blue', linestyle='dashed', linewidth=2, label='Media de las Muestras')
plt.title('Distribución de las Medias de las Muestras')
plt.xlabel('Media de las Muestras')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True)
plt.show()
