
# --- Metodo de ordenamiento SORT() --- Ordena elementos de una lista por orden alfabetico o por numero de manera permanente
print("\n")
coches = []
coches = ['bmw'.title(), 'audi'.title(), 'seat'.title()]
#coches.sort()

print("                                   ----- Lista actual de coches -----")
print("                                        ", coches)
print(" * Ejemplo (1)")
print(" - Lista actual de coches desordenada: " , coches )
print(" - Tipo o Clase de objeto: " , type(coches[0-2]))
print()

print(" * Ejemplo (3)")
print(" - impresion del ultimo indice de lista usando --> -1:", coches)
print(" - El ultimo coche de lista es: " ,coches[-1])
print(" - Lista ordenada de coches actualizada: " , coches)
print()

print(" * Ejemplo (4)")
print(" - Añadiendo un dato al ultimo indice de lista usando --> (.append):", coches)
print(" - Añadiendo un nuevo auto al ultimo indice de lista usando --> (.append):", coches[-1].title())
coches.append('fiat'.title())
print(" - Lista ordenada de coches actualizada: " , coches)
print()

coches.insert(0, 'renault'.title())

print(" * Ejemplo (6)")
print(" - Eliminando el ultimo indice de la lista usando --> (.pop): ", coches , "Hay", len(coches) , "unidades")
coches_eliminados = coches.pop() # De esta forma manipulamos la lista de acuerdo a las condiciones que querramos
print(" - Lista ordenada de coches actualizada: " , coches , "Ahora quedan", len(coches) , "unidades")
print(" - Coche eliminado: " , coches_eliminados)
print()

#Con la instruccion (.remove) en coche_renault = 'renault'.title() / No se puede invocar un string para imprimir el coche eliminado. Por eso se debe asignar el pase de parametro a una variable.
print(" * Ejemplo (7)")
print(" - Eliminando otro coche indicado de lista pero usando --> (.remove): " , coches , "Hay", len(coches) , "unidades") # Remove solo elimina la primera entrada donde encuentre el nombre indicado sin iteracion quiere decir que si existe otro coche con el mismo nombre. No lo hace de manera recurrente por si sola.
coche_renault = 'renault'.title()
coches.remove('renault'.title())
print(" - Lista ordenada de coches actualizada: " , coches , "Ahora quedan", len(coches) , "unidades")
print(" - Coche eliminado: " , coche_renault)
print()

# Del es una palabra especial reservada. Del elimina el coche indicado de la lista sin importar si existe otro coche con el mismo nombre. Lo hace de manera recurrente por si sola.
# Del elimina totalmente el elemento de una lista y no se recupera. Se debe tener especial cuidado con este metodo ya que elimina totalmente el elemento de la lista.
# Para evitar una perdida de informacion con (del) se recomienda crear un pase de parametro o intercambio de valor de variable indicando el indice especifico de lista o elemento a eliminar

print(" * Ejemplo (8)")
print(" - Eliminando otro coche indicado de lista pero con (del):" , coches[2])
coches_del = coches # Pase de parametro que evita la perdida de toda la lista al usar (del)
del coches[2] # (del) es una KeyWord que trabaja con los objetos padre o raiz de listas o objetos.
print(" - Lista actual de coches: ", coches)
print()




