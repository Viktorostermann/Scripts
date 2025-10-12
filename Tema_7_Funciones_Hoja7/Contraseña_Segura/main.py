# Programa principal para solicitar contraseñas
# Validar contraseña
# Si la contraseña es segura, mostrar mensaje de éxito
# Si la contraseña no es segura o valida, mostrar mensaje de error y sugerir nueva contraseña

import validador 
import generador

def solicitar_contrasena_segura():
    contrasena = input("Ingrese una contraseña: ")
    valida = validador.validar_contraseña(contrasena)
    
    if valida:
        print("")
        print("La contraseña es válida")
    else:
        print("")
        print("La contraseña no es válida, se sugierencia crear una más segura")
        sugerencia = generador.generar_contrasena_segura()
        print("")
        print(f"Su nueva contraseña es {sugerencia}")
        print("")

# Llamado de la funcion principal para ejecutar el programa
solicitar_contrasena_segura()
