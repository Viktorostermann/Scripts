# Ejercicio 1: Herencia Multi-nivel

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        

    def enviar_correo(self, asunto, mensaje):
        # Logica para enviar correo electronico
        print("\n")
        print(f"Enviando correo a {self.email}") 
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print("")

    def guardar_registro(self, accion):
        # Logica para guardar registro de usuario
        print(f"Guardando registro para {self.nombre}: {accion}")
        print("")

class GestoUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario, email):
        usuario = Usuario(usuario, email)
        self.usuarios.append(usuario)
        usuario.enviar_correo("Bienvenida", "Gracias por registrarte en nuestro sistema.")
        usuario.guardar_registro("Registro de usuario exitoso")

# Ejemplo de uso:
gestor_usuarios = GestoUsuarios()
gestor_usuarios.agregar_usuario("Danny Miletic", "danny@example.com")