# --- Crear un script para comparar la relacion entre dos grupos de alumnos, Grupo A y Grupo B
("\n")
# --- Instrucciones

## - Pedir al usuario indique:
# 1- Chica o Chico
Genero = input("Indica tu Genero (Chica/Chico): ")
("\n")
# 2- Nombre
Nombre = input("Ingresa tu nombre: ")
nombre_chicas_A = "EHIJKLM"
nombre_chicos_A = "ABCDEFGHRSTUVWXYZ"
("\n")


# --- Elegir grupo al que corresponden los alumnos
## --- Grupo Chicas:
if Genero.lower() == "chica":
    # 1- E hasta M --> Grupo A
    if Nombre[0].upper() in nombre_chicas_A:
        print("El alumno pertenece al Grupo A")
    ## El resto pertenece al Grupo B
    else:
        print("El alumno pertenece al Grupo B")
        ("\n")
## --- Grupo Chicos:
elif Genero.lower() == "chico":
    # 2- A hasta H, R hasta Z --> Grupo A
    if Nombre[0].upper() in nombre_chicos_A:
        print("Tu grupo es A")
    else:
        print("Tu grupo es B")
        ("\n")
else:
    print("ERROR: Ingrese nuevamente el genero, genero no existe")
    ("\n")
# --- End of file ---
exit()
