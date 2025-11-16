#  Variableee :D

temp = int(input('¿Cual es la temperatura afuera?'))
#  Condicion

if temp <= 0:
    print("Hace mucho frio, ponte un abrigo y un sombrero")
elif temp <= 12:
    print("Hace frío, ponte un abrigo")
elif temp <= 25:
    print("¡Está caluroso, que disfrutes tu salida!")
elif temp <= 32:
    print("Está muy caluroso, ponte una gorra.")
#  Hacemos lo que nos pide "1.-":

elif temp >=33:
    print("Esta MUY caluroso afuera! mejor no salgas...")