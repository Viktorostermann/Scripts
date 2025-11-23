from collections import Counter
import numpy as np
import pandas as pd

import pandas as pd

# tu archivo usa punto y coma como separador
df = pd.read_csv("/home/viktore/Documentos/2-Python/Clase_1_Bonus_Estadistica_Aplicada/salary_data.csv", sep=";")

print("")
print("✅ Archivo cargado correctamente")
print("")
print(df.head())
print("")

def calculo(vector):
    vector=np.array(vector)


vector = [1,2,3,4,5,6,7,8,9,8,6,5,7,5]

calculo(vector)
print("")