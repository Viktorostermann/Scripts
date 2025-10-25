import pandas as dataloader # Cargador de datos
print (dataloader.__version__)


print("------------------------------------------------------------------------------------------")
# --- Imprime una lista de nombres correspodnientes a Botes ---
print("--Imprime una lista de nombres correspodnientes a Botes--")
print("\n")
print("Hola tus embarcaciones son las siguientes de la lista")
print("\n")
embarcaciones = ['Bote', 'Yate', 'Velero', 'Catamaran']
print(embarcaciones)
print("------------------------------------------------------------------------------------------")

# 2da --- Segunda forma de imprimir La lista ---
print("\n")
print("------------------------------------------------------------------------------------------")
print("------2da Segunda forma de imprimir La lista ---------------")
print("\n")
embarcaciones = ['Bote', 'Yate', 'Velero', 'Catamaran']
mensaje = " Y claro, si me compras una embarcacion, yo eligiria un " + embarcaciones [1].title()
print(mensaje)
print("------------------------------------------------------------------------------------------")

# --- Agregando otro nombre a la lista con APPEND(), ejemplo sintaxis: Nombre_Variable.APPEND() ---
print("\n")
print("------------------------------------------------------------------------------------------")
print("-----Agregando otro nombre a la lista con APPEND()----------")
embarcaciones = ['Bote', 'Yate', 'Velero', 'Catamaran']
print("Lista original de Barcos:", embarcaciones)
## Aqui se agrega el nuevo elemento
embarcaciones.append('Buque')
print("Lista Nueva de Barcos:",embarcaciones)
print("------------------------------------------------------------------------------------------")

# --- Añadir elementos desde una lista vacia ---
print("\n")
print("------------------------------------------------------------------------------------------")
print("----Añadir elementos desde una lista vacia------------------")
embarcaciones = []
print("Lista vacia: " , embarcaciones)
embarcaciones.append('Destructor')
print("Lista nueva: " , embarcaciones)
print("------------------------------------------------------------------------------------------")
print("\n")

# --- Añadir un elemento en cualquier lugar de la lista con INSERT(), ejemplo sintaxis: Nombre_Variable.insert(numero_ubicacion_variable, string_nombre_añadir) ---
print("\n")
print("------------------------------------------------------------------------------------------")
print("-----Añadir un elemento en cualquier lugar de la lista con INSERT()----")
embarcaciones = ['Bote', 'Yate', 'Velero', 'Catamaran']
print("Lista de embarcaciones original: " , embarcaciones)
embarcaciones.insert(0, 'Pesqueros')
print("\n")
print("Lista de embarcaciones modificada: " ,embarcaciones)
print("------------------------------------------------------------------------------------------")
print("\n")

# --- Borrando el ultimo elemento de una lista con POP(), ejemplo sintaxis: Nombre_Variable.pop()
print("----Borrando el ultimo elemento de una lista con POP()----")
embarcaciones = ['Bote', 'Yate', 'Velero', 'Catamaran']
print("Lista de navios Original:", embarcaciones)
embarcaciones.pop()
print("La embarcacion Eliminada fue 'Catamaran', compara lista anterior:", embarcaciones)
print("------------------------------------------------------------------------------------------")
print("\n")

# 2da --- Imprimiendo el ultimo elemento de una lista eliminado con POP(), ejemplo sintaxis: Nombre_Variable.pop()
print("----Imprimiendo el ultimo elemento de una lista eliminado con POP()----")
print("\n")
embarcaciones = ['Bote_2', 'Yate_2', 'Velero_2', 'Catamaran_2']
print(embarcaciones)
print("\n")
embarcaciones_Eliminadas = embarcaciones.pop()
print(embarcaciones_Eliminadas, "Fue Eliminado de la lista")
print("\n")
print("Embarcaciones en Lista actual:", embarcaciones)
print("------------------------------------------------------------------------------------------")
print("\n")

# 3ra --- Imprimiendo el ultimo elemento de una lista con POP() añadiendo el indice de la lista, ejemplo sintaxis: Nombre_Variable.pop(Numero_Indice)
print("---Imprimiendo el ultimo elemento de una lista con POP() añadiendo el indice de la lista----")
print("\n")
embarcaciones = ['Bote_2', 'Yate_2', 'Velero_2', 'Catamaran_2']
print(f"Esta es tu lista original de Barcos:", embarcaciones)
print("\n")
embarcaciones_Eliminadas = embarcaciones.pop(0)
print(embarcaciones, "Quedan en lista")
print("\n")
print("Embarcaciones Eliminadas fue:", embarcaciones_Eliminadas)
print("------------------------------------------------------------------------------------------")
print("\n")

# ----Borrando Elementos de la lista con REMOVE(), ejemplo sintaxis: Nombre_Variable.remove('Nombre_String_Elemento')
# ---- REMOVE() Solo elimina la primera entrada del elemento seleccionado. Si existe otro elemento con el mismo nombre. No lo hace de manera recurrente por si sola.
print("---Imprimiendo elemento eliminado de lista con REMOVE() ----")
print("\n")
embarcaciones = ['Bote_2', 'Yate_2', 'Velero_2', 'Catamaran_2']
print("Esta es tu lista original de Barcos:", embarcaciones)
print("\n")
embarcaciones.remove('Bote_2')
print("Esta es tu lista de Barcos Eliminados: " , embarcaciones_Eliminadas)
print("\n")
print("Esta es tu lista Actual de Barcos:", embarcaciones)
print("\n")

# ----Borrando Elementos de la lista con (DEL) - Que es una palabra Clave (Keyword) , ejemplo sintaxis: 
print("---Imprimiendo elemento eliminado de lista con REMOVE() ----")
print("\n")
embarcaciones = ['Bote_2', 'Yate_2', 'Velero_2', 'Catamaran_2']
print("Esta es tu lista original de Barcos:", embarcaciones)
print("\n")
del embarcaciones[1]
print("Esta es tu lista Actual de Barcos:", embarcaciones)
print("\n")