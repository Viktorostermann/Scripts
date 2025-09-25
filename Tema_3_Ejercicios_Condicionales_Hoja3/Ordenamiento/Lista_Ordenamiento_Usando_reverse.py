# --- Metodo de ordenamiento REVERSE() para mantener el orden de la lista y LEN() para saber longitud de lista ---
print()
print("      ----- Metodo de ordenamiento REVERSE() para ordenar los primeros al final y los ultimos al principio de lista -----")
coches = ['bmw', 'audi', 'seat']
print("\n")
print("Lista actual de coches:", coches ,len(coches) ,"Unidades")
coches.reverse()

print()
print("Lista de coches con metodo REVERSE():" ,coches ,len(coches) ,"Unidades")
coches.reverse()
print("Lista actual de coches:", coches)
print()

print("Lista Reordenada con metodo SORTED(): " ,coches ,len(coches) ,"Unidades")
print("Lista actual de coches:", sorted(coches))
print()

print("Total de coches en la lista:", len(coches), "Unidades")
print("\n")