''' DATOS CLIENTES: 
Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene 
el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La 
segunda base de datos contiene el nombre del cliente, la dirección y el historial de 
pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y 
devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en 
ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre.'''

Base_Datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", "maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]
Base_Datos2 =  [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), ("Luis", "Calle 789", ["Libro4"])]

# Encontrar los clientes comunes en ambas bases de datos
nombres1 = {cliente[0] for cliente in Base_Datos1} # Obtener los nombres de los clientes en la primera base de datos
nombres2 = {cliente[0] for cliente in Base_Datos2} # Obtener los nombres de los clientes en la segunda base de datos

nombres_comunes = nombres1.intersection(nombres2) # Encontrar los nombres comunes en ambas bases de datos
print(nombres_comunes) # Imprimir los nombres comunes en ambas bases de datos

# Crea una lista de Tuplas con los clientes comunes
Clientes_Comunes = []

for cliente_1 in Base_Datos1: # Iterar sobre la primera base de datos
    if cliente_1[0] in nombres_comunes: # Verificar si el cliente de la primera base de datos está en los nombres comunes
        for cliente_2 in Base_Datos2: # Iterar sobre la segunda base de datos para encontrar el cliente comun
            if cliente_2[0] == cliente_1[0]: # Verificar si el nombre del cliente es el mismo en ambas bases de datos
                Clientes_Comunes.append((cliente_1[0], cliente_1[1], cliente_1[2], cliente_2[1], cliente_2[2])) # Agregar el cliente común a la lista de clientes comunes
                break
print(Clientes_Comunes)  # Imprimir la lista de clientes comunes as np Tuplas