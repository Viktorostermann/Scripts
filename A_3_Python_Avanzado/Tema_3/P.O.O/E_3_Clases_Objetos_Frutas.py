
class Caja_de_Frutas():
    def __init__(self, nombre, color, peso, caducidad, sabor):
        self.nombre = nombre
        self.color = color
        self.sabor = sabor # El atributo sabor puede ser "dulce" or "acido" if sabor not in ["dulce", "ácido"] else sabor = None # Si el valor no está en la lista, se asigna dulce por defecto.
        self.peso = peso    # En gramos
        self.caducidad = caducidad  # En días

    def descripcion(self):
        print(f"La fruta es {self.nombre}, de color {self.color}, sabor {self.sabor} y pesa {self.peso} gramos. La caducidad es de {self.caducidad} dias.")

# Ejemplo de uso con una fruta (Manzana)
print("")
manzana = Caja_de_Frutas("manzana", "rojo", peso = 150, caducidad = 15, sabor = "ácido")
manzana.descripcion()
print("Lista de atributos del objeto manzana: ", manzana.__dict__) # Muestra los atributos del objeto manzana como diccionario.
print("")

# Ejemplo de uso con otra fruta (Banana)
print("")
banana = Caja_de_Frutas("banana", "amarillo", peso = 120, caducidad = 7, sabor= "dulce")
banana.descripcion()
print("Lista de atributos del objeto banana: ", list(banana.__dict__.keys())) # Muestra los atributos del objeto banana como diccionario.
print("") 