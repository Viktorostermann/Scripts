'''Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
aquellas palabras que no tienen ninguna letra prohibida
'''

# --- Crear lista de palabras aleatorias y otras de letras prohibidas
Lista_Palabras_Aleatorias = ["casa" , "perro", "gato", "libro", "raton"]
Lista_Letras_Prohibidas = ["a", "u"]

# --- Crear lista de palabras filtradas
palabras_filtradas = [ ]

# --- Bucle para recorrrer la lista de palabras
for palabra in Lista_Palabras_Aleatorias:

# Bucle si los objetos tienen al guna letra prohibida
    for Lista_Letras_Prohibidas in Lista_Letras_Prohibidas:
        
        if Lista_Letras_Prohibidas in palabra:
            incluir = False
            break

    if incluir:
        palabras_filtradas.append(palabra)        
    
# --- Comprobar si cada palabra u objeto tine alguna letra prohibidas

# --- Imprimimos por pantalla las tres listas
print("Lista de palabras aleatorias: ", Lista_Palabras_Aleatorias)
print("Lista de letras prohibidas: ", Lista_Letras_Prohibidas)
