import numpy as np

print("")
a = np.array([1,2,3,4], dtype=np.int16)
print("Original array: ", a)

print("")
b = a.view(dtype=np.int32)
print("Vista float: ", b)
print("")

b = a.view(dtype=np.int64)
print("Vista float: ", b)
print("")

