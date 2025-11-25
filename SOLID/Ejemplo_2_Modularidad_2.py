# Ejercicio 1: Herencia Multi-nivel

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class GestorCorreos: # Gestor de correos, es familia o subclase de la clase Usuario, (No principal) = Instancia de la clase Usuario.
    def enviar_correo(self, destinatario, asunto, mensaje):
        print("\n")
        print(f"Enviando correo a {destinatario}") 
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print("")


    def guardar_registro(self, accion):
        # Logica para guardar registro de usuario
        print(f"Guardando registro para {self.nombre}: {accion}")
        print("")

class RegistroAcciones:
    def guardar_registro(self, accion):
        print(f"Guardando registro para {self.nombre}: {accion}")
        print("")

class GestorUsuarios:
    def __init__ (self, gestor_correos, registro_acciones):
        self.usuarios = []
        self.gestor_correos = gestor_correos
        self.registro_acciones = registro_acciones
    def agregar_usuario(self, usuario, email):
        usuario = Usuario(usuario, email)
        self.usuarios.append(usuario)
        self.gestor_correos.enviar_correo(
        usuario.email, "Bienvenida", "Gracias por registrarte en nuestro sistema. " \
                        "Estamos encantados de tenerte con nosotros.")

        self.registro_acciones.guardar_registro(usuario.nombre, "Guardando registro....")
        print("")
        print("Usuario agregado correctamente.")


# Ejemplo de uso:
registro_acciones = RegistroAcciones()
gestor_correos = GestorCorreos()
gestor_usuarios = GestorUsuarios(gestor_correos, RegistroAcciones())
gestor_usuarios.agregar_usuario("Danny Miletic", "danny@example.com")