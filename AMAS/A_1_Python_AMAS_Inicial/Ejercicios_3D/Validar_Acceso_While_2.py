'''
Supongamos que eres un administrador de sistemas
y necesitas validar el acceso a una aplicación web.
Crea un script que verifique si nombre de usuario y contraseña
son correctos. Que permita el acceso si ambos son correctos,
si no, debe mostrar un mensaje de error.
'''

# Lista de nombres de usuarios
lista_nombres_usuarios = ["admin", "user1", "user2"]
# Lista de contraseñas
lista_password_usuarios = ["admin123", "user123", "user456"]

# Función principal de autenticación
def autenticar():
    while True:
        # Pedir credenciales
        nombre_usuario = input('Introduce tu nombre de usuario: ')
        password_usuario = input('Introduce tu contraseña: ')
        
        # Verificar credenciales
        credenciales = False
        for i in range(len(lista_nombres_usuarios)):
            if lista_nombres_usuarios[i] == nombre_usuario and lista_password_usuarios[i] == password_usuario:
                credenciales = True
                # Mostrar resultado
                if credenciales == True:
                    print("Acceso permitido")
                    print("Bienvenido", nombre_usuario)
                break
        else:
            print("Acceso denegado")
            print("No se ha podido validr tu usuario y contraseña")
            
            # Preguntar si desea volver a intentar
            volver_a_intentar = input("¿Deseas volver a intentar? (s/n): ").lower()
            if volver_a_intentar != 's':
                print("Gracias por usar el programa. ¡Hasta luego!")
                break

if __name__ == "__main__":
        autenticar()