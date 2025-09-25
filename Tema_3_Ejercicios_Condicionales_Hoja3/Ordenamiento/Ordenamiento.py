
# --- Metodo de ordenamiento SORT() ---

print("\n")
coches = ['bmw', 'audi', 'seat']
print("Lista actual de coches desordenada: " , coches)
print("\n")
coches.sort()
print("Lista ordenada de coches: " , coches)
print("\n")

# --- Metodo de ordenamiento SORTED() para mantener el orden de la lista ---
print("--- Metodo de ordenamiento SORTED() para mantener el orden de la lista")
coches = ['bmw', 'audi', 'seat']
autos = sorted(coches)
print("\n")
print(autos)
print("\n")
print("Lista actual de coches desordenada: " ,sorted(coches))
print("\n")

# --- Metodo de ordenamiento REVERSE() para mantener el orden de la lista y LEN() para saber longitud de lista ---
print("\n")
print("--- Metodo de ordenamiento REVERSE() para ordenar los primeros al final y los ultimos al principio de lista")
coches = ['bmw', 'audi', 'seat']
print("\n")
print("Lista actual de coches:", len(coches))
print("Lista actual de coches:", coches)
coches.reverse()
print("\n")
print("Lista de coches con metodo REVERSE():" , len(coches))
print("Lista actual de coches:", coches)
print("\n")
print("Lista Reordenada con metodo SORTED(): " , sorted(coches))
print("Lista Original de coches:", coches)
print("\n")