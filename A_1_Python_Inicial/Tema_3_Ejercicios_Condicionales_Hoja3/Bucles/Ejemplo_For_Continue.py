for i in range(10):
 if i == 3:
  break
 print()
 print("Hola, Estamos dentro del if del continue y del break por el Numero" ,i)
 if i > 3 or i == 4:
  continue
print()
print(" - El numero" ,i ,"esta dentro del if pero fuera del Break y ademas llegamos al numero" , i+1,". Por eso salimos del bucle")
print()
print(" - Ya estamos fuera del Bucle y del programa porque el numero" ,i ,"Sobre paso la condición")
print()