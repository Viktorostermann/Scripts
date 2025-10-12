''' 
Supongamos que eres un administrador de sistemas
y necesitas validar el acceso a una aplicación web.
Crea un script que verifique si nombre de usuario y contraseña
son correctos. Que permita el acceso si ambos son correctos,
si no, debe mostrar un mensaje de error.
'''
# Lista de nombres de usuairo
lista_nombres_usuarios = ["admin", "user1", "user2"]
# Lista de contraseñas
lista_password_usuarios = ["admin123", "user123", "user456"]

# Recorrer la lista de ususarios y coontraseñas
credenciales = False
def autenticacion():
    # Pedir al usurio su nombre de usuario
    nombre_usuario = input('Introduce tu nombre de usuario: ')
    # Pedir al usurio su contraseña
    password_usuario = input('Introduce tu contraseña: ')
    # Recorrer la lista de nombres de usuario
    for i in range(len(lista_nombres_usuarios)):
    # Comprobar si el nombre de usuario es correcto
        if nombre_usuario == lista_nombres_usuarios[i]:
            print("Nombre de usuario correcto")
            # Comprobar si la contraseña es correcta
            if password_usuario == lista_password_usuarios[i]:
                print("Contraseña correcta")
            # Si el nombre de usuario y la contraseña son correctos
                credenciales = True
            # si el nombre de usuario y la contraseña son correctos
            if credenciales == True:
             print("Acceso permitido. Bienvenido", nombre_usuario)
             break
        # Si Nombre usuario y contraseña no son correctos 
    else:
        if nombre_usuario not in lista_nombres_usuarios:
            print("Nombre de usuario incorrecto")
        if password_usuario not in lista_password_usuarios:
            print("Contraseña incorrecta")
        if nombre_usuario not in lista_nombres_usuarios and password_usuario not in lista_password_usuarios:
            print("Nombre de usuario o Contraseña incorrecta")
            print("Acceso denegado. Por favor, verifica tus credenciales.")
        credenciales = False
        # Preguntar al usuario si desea volver a intentar
        volver_a_intentar = input("¿Deseas volver a intentar? (s/n): ")
        if volver_a_intentar.lower() == "s":
            autenticacion()
        else:
            print("Gracias por usar el programa. ¡Hasta luego!")
# Llamar a la función de autenticación
autenticacion()