#  Declaramos variables..
p = int(input ('¿Cuantos palos tienes en tu inventario?'))
t = int(input('¿Cuantos tablones tienes en tu inventario?'))

#  Condiciones..
if p >= 7 or t >= 4:
    print('Puedes construir una escalera')
else:
    print ('No puedes construir una escalera')