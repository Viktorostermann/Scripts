from collections import Counter
import numpy as np
import pandas as pd

def calculo(vector):
    vector=np.array(vector)


vector = [1,2,3,4,5,6,7,8,9,8,6,5,7,5]

# Calculo de Vector
df = pd.read_csv("salary_data.csv")