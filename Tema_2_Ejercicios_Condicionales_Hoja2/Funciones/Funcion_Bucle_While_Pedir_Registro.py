
def Dato(nombre): #--- Función
    print("\n")
    nombre = input("Ingrese un nombre para el registro: ")
    print("\n")
    # --- Con .strip() y lstrip(). Eliminamos o limpiamos los espacios en blanco, saltos de linea, antes o despues de la cadena de carateres.
    if nombre.lstrip() == "" and nombre.strip() == "":
        # --- Tambien se puede usar la variable creada 'nombre' con la siguiente sintaxis: while nombre == "":
        while True: 
            print("Registro en blanco. Su registro no puede ser procesado en blanco. ")
            print("\n")
            # --- Evaluo si quiere permanecer en el input o salir del script.
            salir = input("Desea Salir del Script?: Si = (Y) No = (N): ")
            print("\n")
            if ( 
                salir == "Y" or 
                salir == "y" or 
                salir == "Yes" or 
                salir == "yes" or 
                salir == "YES"
                ): # --- Si desea salir del script, imprime el mensaje y sale del ciclo While.
                print("Saliendo del programa, Hasta la proxima!")
                print("\n")
                break
            elif    (salir == "N" or 
                     salir == "n" or 
                     salir == "No" or 
                     salir == "no" or 
                     salir == "NO"
                     ): # --- Si no desea salir del script, regresa al ciclo While.
                return Dato(" ") # --- Si deseo forzar un imput. Aqui llamo la funcion nuevamente o puedo utilizar (return). Para que regrese al ciclo While, forzando al usuario incluir el registro.
    else:
        # --- aca compruebo si la variable nombre no esta vacia nuevamente para evitar espacio blanco o vacio.
        if nombre != " ": 
            print(f'Hola, {nombre}, ¡Tu registro se ha completado! A dios.!')
            print("\n")
Dato(" ") # ---> Regresamos el estado de la funcion en blanco al final del script aqui podemos llamarla directamente 
# --- Tambien podemos hacer uso de Retrun como lo he hecho acá.
