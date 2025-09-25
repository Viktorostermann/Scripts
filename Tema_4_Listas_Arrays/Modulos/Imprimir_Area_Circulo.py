import Constantes

print(Constantes.PI)
radio = float(input("Ingrese el radio del circulo: "))
area = Constantes.PI * radio ** 2
print("El area del circulo es: " ,area)
print("El area del circulo es: " ,Constantes.PI * radio ** 2)

# Imprime el area del circulo
def imprimir_area_circulo(radio):
    area = Constantes.PI * radio ** 2
    print("El area del circulo es: ", area)
imprimir_area_circulo(radio)
