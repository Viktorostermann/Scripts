'''Estadistica descriptiva'''

import pandas as pd

#Cargamos el dataset en un dataframe de Pandas
df = pd.read_csv('data.csv')
print(df.describe())

    #La función describe() nos devuelve una tabla con los siguientes datos:
    #count: número de elementos no nulos.
    #mean: media aritmética.
    #std: desviación típica.
    #min: valor mínimo.
    #max: valor máximo.
    #25%, 50% y 75%: cuartiles (valores que dividen la muestra en cuatro partes iguales).
    #percentiles: valores que dividen la muestra en tantos porcentajes como se indiquen.

 
 