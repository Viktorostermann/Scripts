from collections import Counter
import numpy as np
import pandas as pd

# tu archivo usa punto y coma como separador
df = pd.read_csv("/home/viktore/Documentos/2-Python/Clase_1_Bonus_Estadistica_Aplicada/salary_data.csv", sep=";")

# print(df.head())
Rango=df.income.max()-df.income.min()
print("")
print("✅ Los Archivos fueron cargados correctamente")
print("")

# Calculo del Rango
#print(" - El rango de la funcion es: ",Rango)
#rango_numpy=np.max(df.age)-np.min(df.age)
#print("El rango de Numpy es: ",rango_numpy)
#print("")   

# Calculo de la Media
#Varianza=df.age.var()
#print(" - La Media de la Edad es:",df.age.mean())
#print("")

# Calculo de la Varianza de Numpy
#Varianza=df.age.var()
#print(" - Media",df.age.mean())
#print("")
#print(" - Varianza Edad: " , (Varianza))

#print("")   
#Varianza_np=np.var(df.age)
#print(" - Varianza Edad Numpy: " ,(Varianza_np))
#print("")

print("Varianzas Poblacionales")
Varianzas=df.age.var(ddof=0)
print("Varianza Edad:",Varianzas)
Varianza_np=np.var(df.age,ddof=0)
print("Varianza Edad Numpy:",Varianza_np)
print("")

# Desviaciones Estandar
ds=df.age.std()
print("Desviación STD Funcion:" ,ds)
print("")

ds_np=np.std(df.age)
print("Desviacion STD Numpy:" ,ds_np)
print("")