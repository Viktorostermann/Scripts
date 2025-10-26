

class Coche():
    def __init__(self, marca, modelo, anio):
         '''Inicializa los atributos del coche'''
         self.marca = marca
         self.modelo = modelo
         self.anio = anio
         self.contador_kilometros = 0

    def crear_descripcion(self):
        pass 
    #-- snipet --
        descripcion = f"{self.anio} {self.marca} {self.modelo}"
        return descripcion.title()

    def leer_kilometros(self):
        '''Muestra el valor del contador de kilometros'''
        print(f"Este coche tiene {self.contador_kilometros} kilometros recorridos.")

    def actualizar_kilometros(self, kilometros):
        '''Establece el valor del contador de kilometros'''
        self.contador_kilometros = kilometros
        if kilometros >= self.contador_kilometros:
            self.contador_kilometros = kilometros
        else:
            print("No puedes reducir el valor de los kilometros.")

mi_cohe = Coche("Toyota", "Corolla", 2020)
mi_coche_usado.actualizar_kilometros(15000)
mi_coche_usado.leer_kilometros()
mi_cohe_usado.actualizar_kilometros(12000)  # Intento de reducir los kilometros
mi_coche_usado.leer_kilometros()