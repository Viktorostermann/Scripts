#  Figuras Geometricas
# En este ejemplo, tenemos una clase base Rectangulo y una clase derivada Cuadrado.
# Sin embargo, Cuadrado no cumple con el principio de sustitucion de Liskov
# porque al cambiar el ancho o alto de un Cuadrado, se altera su comportamiento esperado
# en comparacion con un Rectangulo. Esto puede llevar a resultados inesperados
# cuando se utiliza un Cuadrado en lugar de un Rectangulo.



# Por ejemplo de Nota 2 pie de pagina:

class Figura:
    pass

class Rectangulo(Figura): # 
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def obtener_area(self):
        return self.ancho * self.alto
    
    def set_ancho(self, ancho):
        #self.ancho = ancho # ''' Si activo esta linea, el codigo funciona correctamente forzando el comportamiento esperado.'''
        self.alto = ancho

    def set_alto(self, alto):
        #self.alto = alto # ''' Si activo esta linea, el codigo funciona correctamente forzando el comportamiento esperado. '''
        self.ancho = alto
# ___________________________________________________________________________________________________

class Cuadrado(Figura):
    def __init__(self, lado):
        #super().__init__(lado, lado)
        self.lado = lado

    '''def set_ancho(self, ancho):
        self.ancho = ancho
        #self.alto = ancho # Suprimimos esta linea para evitar que el comportamiento sea diferente al de un rectangulo. Esto relacionado a Nota 2.'''

    def set_alto(self, lado): # Anteriormente el set_alto tenia asignado(self, alto) y era el mismo que en Rectangulo
        self.lado = lado
        #self.ancho = alto # Suprimimos esta linea para evitar que el comportamiento sea diferente al de un rectangulo. Esto relacionado a Nota 2.

    def obtener_area(self):
        return self.lado * self.lado

    '''def ajustar_area_rectangulo(rectangulo: Rectangulo, nuevo_ancho, nuevo_alto):
    rectangulo.set_ancho(nuevo_ancho)
    rectangulo.set_alto(nuevo_alto)
    return rectangulo.obtener_area()'''

def imprimir_area(figura:Figura):
    print(f"El Area: ", figura.obtener_area())


# ___________________________________________________________________________________________________

# Prueba del codigo haciendo uso de las clases Rectangulo y Cuadrado cambiando el set_alto y set_ancho

# Dimensiones iniciales
rectangulo = Rectangulo(4, 5)
cuadrado = Cuadrado(4)

imprimir_area(rectangulo) # 4 ,6
imprimir_area(cuadrado)


# Seteamos nuevas dimensiones #

# Cambiando las dimensiones del rectangulo 6 * 7
rectangulo.set_alto(6)
rectangulo.set_ancho(7)
imprimir_area(rectangulo) # 4 ,6

# Cambiando las dimensiones del cuadrado a lado 2 * 2
cuadrado.set_alto(2)
imprimir_area(cuadrado)

'''area_rectangulo = ajustar_area_rectangulo(rectangulo, 6, 7) # 4 ,6'''
'''area_cuadrado = ajustar_area_rectangulo(cuadrado, 6, 7)'''

'''print(f"Area del Rectangulo ajustado: {area_rectangulo}")  # Salida esperada: 42
print(f"Area del Cuadrado ajustado: {area_cuadrado}")  # Salida esperada: 49'''

# El area del cuadrado no es correcta segun el comportamiento esperado de un rectangulo.
# Esto demuestra que Cuadrado no puede sustituir a Rectangulo sin alterar el comportamiento del codigo,
# violando asi el principio de sustitucion de Liskov.


# Nota: 
'''Para cumplir con el principio de sustitucion de Liskov, la clase Cuadrado deberia no heredar de Rectangulo,
o deberia implementar metodos que no alteren el comportamiento esperado de un Rectangulo.
Para hacerlo podriamos bien eliminar los set_ancho y set_alto de la clase Cuadrado,
o hacer que estos metodos no modifiquen ambos atributos simultaneamente.'''

# Nota 2:
''' Tambien podriamos crear otra clase base llamada Figura, y tanto Rectangulo como Cuadrado heredan de Figura.
De esta manera, ambas clases pueden tener sus propias implementaciones sin interferir entre si,
cumpliendo asi con el principio de sustitucion de Liskov.'''


