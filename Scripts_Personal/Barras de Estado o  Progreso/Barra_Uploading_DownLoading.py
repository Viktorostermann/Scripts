# -*- coding: utf-8 -*-
from tqdm import tqdm
import time

elementos = range(100)

print("\n")
for i in tqdm(elementos, desc="Cargando", unit="elementos"):
    # Simular trabajo
    time.sleep(0.1)  # Simular trabajo

# from tqdm import tqdm
print("\n")
print("Carga completa")
print("\n")
