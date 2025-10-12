"""
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que
pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no. 
"""

# --- Pedir al usuario que ingrese su nombre, edad y nota media
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nota_media = float(input("Ingrese su nota media: "))
print("\n")
print("\n")

# --- Comprobar si el estudiante puede optar a la beca
# --- Nota media >8 + edad 17 -21
if nota_media >= 8 and edad >= 17 and edad <= 21:
    # --- Si cumple con los requisitos imprimimos que puede optar a la beca
    print(f"{nombre} puede optar a la beca.")
else:
    # --- Si no cumple con los requisitos imprimimos que no puede optar a la beca
    print(f"{nombre} no puede optar a la beca.")
    ("\n")