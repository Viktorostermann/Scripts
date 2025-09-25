from geolite import geolite

# Abre el lector de la Base de Datos GeoLite2
reader = geolite.reader()

# Realiza una consulta, por ejemplo, con la IP 8.8.8.8
result = reader.get('8.8.8.8')
print(result)
print("\n")
result = reader.get('1.1.1.1')
print(result)
print("\n")

# Cierra el lector cuando ya no se necesite
geolite.close()