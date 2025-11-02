print("------------------------------------------------------------------------------------------")

# --- Imprime una lista de nombres correspodnientes a Botes con Bucle FOR()) ---
print("--Imprime una lista de nombres correspodnientes a Botes--")
print("\n")
print("Hola tus embarcaciones son las siguientes de la lista")
print("\n")
embarcaciones = ['Bote', 'Yate', 'Velero', 'Catamaran']
for embarcaciones in embarcaciones:
    print(embarcaciones)
print("------------------------------------------------------------------------------------------")

# 2da --- Segunda forma de imprimir La lista trabajando con el indice del objeto FOR() ---
print("\n")
print("------------------------------------------------------------------------------------------")
print("------2da Segunda forma de imprimir La lista ---------------")
print("\n")
embarcaciones = ['Bote', 'Yate', 'Velero', 'Catamaran']
for i in (range(0,3)):
    print(embarcaciones[i])
    mensaje = " Claro..! si me compras una embarcacion, yo eligiria un " + embarcaciones [1].title()
    print("\n")
print(mensaje)
print("------------------------------------------------------------------------------------------")

# --- 3ra Forma trabajando con el indice pero agregando el paso donde inicia o finaliza el indice del FOR() in RANGE() :ejemplo sintaxis: Nombre_Variable.APPEND() ---
print("\n")
print("------------------------------------------------------------------------------------------")
print("-----Agregando otro nombre a la lista con APPEND()----------")
embarcaciones = ['Bote', 'Yate', 'Velero', 'Catamaran']
print("Lista original de Barcos:", embarcaciones)
for i in range(0, 2, len(embarcaciones)):
    print(embarcaciones[i]) ## Aqui agregamos un nuevo elemento a la lista con APPEND()
    embarcaciones.append('Buque')
    print("Lista Nueva de Barcos:",embarcaciones)
print("------------------------------------------------------------------------------------------")

# --- Añadir elementos a una lista vacia utilizando FOR() in RANGE()---
print("\n")
print("------------------------------------------------------------------------------------------")
print("----Añadir elementos desde una lista vacia con FOR() in RANGE()------------------")
embarcaciones = []
print("Lista vacia: " , embarcaciones)
for i in range(0, len(embarcaciones)):
    print("Esta embarcacion es un:", embarcaciones[i].title())
if embarcaciones == [ ]:
    print("La lista esta vacia")
    print("Agregaremos una nave al primer registro de la lista por usted")
    embarcaciones.append('Destructor')
    print("Lista nueva: " , embarcaciones)
print("------------------------------------------------------------------------------------------")
print("\n")
