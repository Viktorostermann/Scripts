# Preguntar la edad del usuario
edad = int(input("¿Cuál es tu edad? "))
    
# Preguntar si tiene una entrada
tiene_entrada = input("¿Tienes una entrada? (sí/no): ").strip().lower()

# Verificar si puede ingresar a la sala de cine
if edad < 7 or tiene_entrada == 'sí':
    mensaje = "Puedes ingresar a la sala de cine."
else:
    mensaje = "Compra una entrada primero."
        
print(mensaje)