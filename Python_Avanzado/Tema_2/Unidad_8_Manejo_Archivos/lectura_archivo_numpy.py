''' Leer un archivo de texto con NumPy '''

import numpy as np

# Ejemplo_1:  Leer el contenido del archivo 'datos.txt' utilizando NumPy
archivo = np.genfromtxt('datos.txt', delimiter=',')
print(archivo)

# Crear datos de ejemplo
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('datos_guardados.txt', data, delimiter=',')

# Guardar datos en un archivo CSV
np.savetxt('datos_guardados.csv', data, delimiter=',', fmt='%d')

# Leer datos desde un archivo CSV
data = np.genfromtxt('datos_guardados.csv', delimiter=',', dtype=int)
print(data)

# Guardar datos en un archivo de texto
np.savetxt('datos_guardados.txt', data, delimiter=',', fmt='%d')

# Leer datos desde un archivo de texto
data = np.genfromtxt('datos_guardados.txt', delimiter=',', dtype=int)
print(data)