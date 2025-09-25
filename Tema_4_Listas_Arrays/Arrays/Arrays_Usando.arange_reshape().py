import numpy as np

b = np.arange(1,10).reshape((3,3))
suma_array = b.sum(0)
print (b)
print("")
print (suma_array)