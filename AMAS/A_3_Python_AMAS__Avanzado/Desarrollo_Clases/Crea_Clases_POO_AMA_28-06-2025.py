'''Creamos una clase base llamada LectorArchivo encargada de abrir y leer archivos de texto, 
y una clase derivada llamada AnalizadorTexto que heredaba sus métodos, agregaba funcionalidades 
para procesar el texto. Aplicamos técnicas de limpieza como la eliminación de signos de puntuación 
y la conversión a minúsculas con lower(), y utilizamos estructuras como diccionarios para contar la frecuencia de palabras. 
Finalmente, determinamos cuál era la palabra más repetida en el texto. Este ejercicio reforzó el uso de clases, herencia, manejo de excepciones, y procesamiento de cadenas, 
todo desarrollado paso a paso en un entorno con celdas tipo notebook.'''

# Tip 1 : 
# 
# - Creamos una clase base llamada Lector Archivo
# - Creamos una clase derivada llamada Analizador Texto
# - Heredamos los métodos de la clase base LectorArchivo a la clase derivada Analizador Texto
# - Aplicamos técnicas de limpieza como la eliminación de signos de puntuación y la conversión a minúsculas.
# - Utilizamos estructuras como diccionarios para contar la frecuencia de palabras.
# - Finalmente, determinamos cuál era la palabra más repetida en el texto.

import os
import string

import os
import string

# Creacion de Clase Lector Archivo #
# ------------------------------------------------------------------------------------------------
class LectorArchivo:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.contenido = ""

# Creacion de Funcion Leer Archivo #
# ------------------------------------------------------------------------------------------------
    def leer_archivo(self):
        try:
            with open(self.nombre_archivo, "r", encoding="utf-8", errors="replace") as f:
                self.contenido = f.read()
                print("")
                print(f"Nombre del archivo: {self.nombre_archivo}")
                print(f"Longitud de palabra: {len(self.contenido)} caracteres")
                print(f"Contenido del archivo: {self.contenido.strip()}")
            return True
        except Exception as e:
            print(f"Error al leer el archivo, dañado o corrupto: {e}")
            return False

# Creacion de Clase Analizador Texto #
# ------------------------------------------------------------------------------------------------
class AnalizadorTexto(LectorArchivo):
    def __init__(self, nombre_archivo):
        super().__init__(nombre_archivo)
        self.frecuencia_palabras = {}

# Creacion de Funcion Contar Palabras #
# ------------------------------------------------------------------------------------------------
    def contar_palabras(self):
        if not self.contenido:
            if not self.leer_archivo():
                return False

        signos_puntuacion = string.punctuation
        palabras_limpias = []

        for palabra in self.contenido.lower().split():
            palabra_limpia = palabra.strip(signos_puntuacion)
            if palabra_limpia:
                palabras_limpias.append(palabra_limpia)

        for palabra in palabras_limpias:
            if palabra in self.frecuencia_palabras:
                self.frecuencia_palabras[palabra] += 1
            else:
                self.frecuencia_palabras[palabra] = 1
        return True

# Creacion de Funcion Palabra Mas Repetida #
# ------------------------------------------------------------------------------------------------
    def palabra_mas_repetida(self):
        if not self.frecuencia_palabras:
            if not self.contar_palabras():
                return None

        max_frecuencia = max(self.frecuencia_palabras.values())
        palabras_max = [p for p, f in self.frecuencia_palabras.items() if f == max_frecuencia]

        if max_frecuencia == 1:
            print("No hay palabras repetidas.")
        else:
            print(f"[REPETICIONES] Palabras más repetidas ({max_frecuencia} repeticiones):")
            for palabra in palabras_max:
                print(f" - '{palabra}'")

        return palabras_max, max_frecuencia

# Creacion de Funcion Main #
# ------------------------------------------------------------------------------------------------
# Ejecución
if __name__ == "__main__":
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "texto.txt")
    analizador = AnalizadorTexto(ruta)

    if analizador.contar_palabras():
        print("\n[FREQUENCIA] Diccionario completo:")
        for palabra, frecuencia in analizador.frecuencia_palabras.items():
            print(f"'{palabra}': {frecuencia}")
        print("")  # Espaciado visual
        analizador.palabra_mas_repetida()

