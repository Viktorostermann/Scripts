from collections import Counter
import numpy as np
import pandas as pd
from scipy.stats import skew

print("")
def normal_dist():
	
    # Parametros de la distribucion normal
    media = 0
    desviacion_estandar = 1
    tamaño=100000

    # Generacion de datos aleatorios
    datos = np.random.normal(loc=media, scale=desviacion_estandar, size=tamaño)

    Data=pd.Series(datos)
    print("- Curtosis:",Data.kurtosis())
    print("")


    # tu archivo usa punto y coma como separador
    df = pd.read_csv("/home/viktore/Documentos/2-Python/A_4_Bonus_Estadistica_Aplicada/salary_data.csv", sep=";")

    # Calculo ASimetria
    print(df.head())
    print("")

    Asimetria = df.income.skew()
    print("Asimetria de salarios:", Asimetria)
    print("")

# Es decir, la asimetria es positiva, es decir la mayoria de los salarios se encuentran en la parte izquierda.
# ES decir hay mas salarios bajos que altos

# Numpy no tiene esa funcion por lo que podriamos utilizar otra libreria de datascience Scipy.


    Asimetria = skew(df.age)
    print("Asimetria de Edad:", Asimetria)  
    print("")

# Es decir, la asimetria es positiva, es decir la mayoria de las personas se encuentra en la parte izquierda.
# son mayores que la media

    curtosis = df.income.kurtosis()
    print("Curtosis de Salario:", curtosis) # La curtsis es negativa, esto quiere decir que el pico de la distribucion es menor al esperado para una distribucion normal.
    print("")

if __name__ == "__main__":
	normal_dist()


