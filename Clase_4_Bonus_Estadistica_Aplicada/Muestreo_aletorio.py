import numpy as np

#generamos una poblacion de ejemplo
poblacion=np.arange(1,101) #Poblacion del 1 al 100

tamaño_muestra=10

#Seleccionamos la muestra usando un muestro simple

muestra_aleatoria_simple=np.random.choice(poblacion,tamaño_muestra,replace=False)
print('Muestra aleatoria simple:',muestra_aleatoria_simple)