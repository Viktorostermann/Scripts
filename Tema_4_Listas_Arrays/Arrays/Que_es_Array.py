''' Array
Un array es una estructura de datos que permite almacenar y manipular una 
colección de elementos de un mismo tipo de dato. En Python, los arrays son'''

'''Para usar un array debemos usar un modeluo o debes importar la libreria numpy'''

import array as vector
my_array = vector.array('i', [1,2,3,4,5,6,7,8,9,10])
print(type(my_array))

import numpy as np
my_array = np.array([1,2,3,4,5,6,7,8,9,10])
print(type(my_array))
