'''Crea una lista llamada frutas que contengan los siguientes nombres de frutas como cadenas
de caracteres: manzana, plátano, cereza, pera, higo, frambuesa y fresa'''

#  1--- Crear lista de Frutas ---
frutas = ['manzana', 'plátano', 'cereza', 'pera', 'higo', 'frambuesa', 'fresa']

# 2---- Usa la función len() para imprimir la longitud de la lista frutas ---
print("Longitud de la lista de frutas:", len(frutas))
print("\n")

# 3--- Accede al objeto numero 3 de la lista e imprímelo or consola ---
print("Tercera fruta de la lista:", frutas[2])
print("\n")

#.[!NOTE]. 4--- Modifica el segundo objeto de la lista y cambiado a mora --- 
# --- Accede al objeto indice 1 de la lista e cambia su valor a mora ---
frutas[1] = 'mora'
print("Fruta modificada en la lista:", frutas[1])
print("\n")

# 5--- Añade el string mango al final de la lista ---
frutas.append('mango')
print("Nueva lista de frutas:", frutas)
print("\n")

# 6--- Usa el método insert() y añade el string “uva“ año comienzo de la lista ---
frutas.insert(0, 'uva')
print("Nueva lista de frutas con 'uva' añadida:", frutas)
print("\n")

# 7--- Usa un bucle para recorrer la lista e imprimir cada fruta por la consola ---
print("Listado de frutas:")
for fruta in frutas:
    print(fruta)
print("\n")

# 8--- Usa el método pop() para eliminar el último elemento de la lista y guárdalo en una variable llamada “ultima_fruta“ ---
ultima_fruta = frutas.pop()
print("Ultima fruta eliminada:", ultima_fruta)
print("\n")

# 9--- Realiza un bucle que recorra la lista e imprima cada una de las frutas por consola ---
print("Listado de frutas después de eliminar la última:")
for fruta in frutas:
    print(fruta)
print("\n")

# 10---  Modifica el script para que imprima también la longitud de cada nombre de fruta por consola ---
print("Listado de frutas y su longitud:")
for fruta in frutas:
    print(fruta, "-", "Tiene" ,len(fruta) , "letras")
print("\n")

# 11---  Modifica el script para que recorra la lista de frutas y solo imprima aquellos nombres que tengan más de 5 caracteres ---
for fruta in frutas:
    if len(fruta) > 5:
        print(fruta, "-", "Tiene" ,len(fruta) ,"Letras")
    # --- print(fruta), "-" + "Tiene", len(fruta) , "Letras"
print("\n")

# 12--- Usa el método remove() para borrar el string “cereza“ de la lista ---
Fruta_Eliminada = frutas.remove('cereza')
print("Fruta indice 2, ó de posicion 3, fue eliminada:", frutas)
print("\n")

# 13--- Usa el método clear() para vaciar la lista.---
frutas.clear()
print("El listado de frutas esta vacio", frutas)
print("\n")

       