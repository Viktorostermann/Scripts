import numpy as np
import pandas as pd

# Población de ejemplo con conglomerados
data = {
    'individuos': np.arange(1, 51),
    'conglomerados': np.repeat(np.arange(1, 11), 5)  # 10 conglomerados con 5 individuos cada uno
}
poblacion = pd.DataFrame(data)

print(poblacion)

conglomerados_seleccionados=np.random.choice(poblacion['conglomerados'].unique(),size=2,replace=False)

muestra_por_conglomerados=poblacion[poblacion['conglomerados'].isin(conglomerados_seleccionados)]

print("Muestra por conglomerados \n",muestra_por_conglomerados)