import numpy as np

a = np.array([106535353126], dtype=np.int32)
print(" Original array: ", a)

b = a.view(dtype=np.float32)
print("Vista float: ", b)

