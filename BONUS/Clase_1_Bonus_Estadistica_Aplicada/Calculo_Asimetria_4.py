import os
import pandas as pd
import numpy as np
from scipy.stats import skew

def normal_dist():
    media = 0
    desviacion_estandar = 1
    tamaño = 100000

    datos = np.random.normal(loc=media, scale=desviacion_estandar, size=tamaño)
    Data = pd.Series(datos)
    print("- Curtosis (datos simulados):", Data.kurtosis())
    print("")

    csv_path = "/home/viktore/Documentos/2-Python/Clase_1_Bonus_Estadistica_Aplicada/salary_data.csv"

    if not os.path.exists(csv_path):
        print(f"❌ No se encontró el archivo en: {csv_path}")
        return

    df = pd.read_csv(csv_path, sep=";")
    print("✅ Archivo cargado correctamente")
    print(df.head())
    print("Columnas disponibles:", df.columns)
    print("")

    # Validar columnas antes de usarlas
    if "income" in df.columns:
        print("Asimetria de salarios:", df["income"].skew())
        print("Curtosis de Salario:", df["income"].kurtosis())
        print("")
    else:
        print("⚠️ La columna 'income' no existe en el CSV")

    if "age" in df.columns:
        print("Asimetria de Edad:", skew(df["age"].dropna()))
        print("")
    else:
        print("⚠️ La columna 'age' no existe en el CSV")

if __name__ == "__main__":
    normal_dist()
