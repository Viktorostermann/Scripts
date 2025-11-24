Numeros_de_telefono = {}
Numeros_de_telefono["John"] = "555-1234"
Numeros_de_telefono["Max"] = "555-6789"
Numeros_de_telefono["Steve"] = "444-4321" 
Numeros_de_telefono["Kenny"] = "867-5309"
print(Numeros_de_telefono)

letra = input('¿Los nombres que empiezan por qué letra quieres ver?') 
for llave in Numeros_de_telefono.keys():
    if llave[0] == letra:
        print(llave, "su valor es:", Numeros_de_telefono[llave])