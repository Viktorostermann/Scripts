'''
EJERCICIOS HOJA 7
TEMA: FUNCIONES

OBJETIVO: FAMILIARIZACIÓN CON EL USO EL USO DE RETURN Y
MODULOS.

Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y veri que si los valores
ingresados cumplen con los requisitos especi cados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.”
'''


# Funcion para validar el formulario
def validar_formulario(nombre, email, telefono): 
    if len(nombre) < 3: # Verificamos que el nombre tenga mas de tres (3) letras
        return False
    
    if "@" not in email or "." not in email: # Verificamos que el email tenga un @ y un .
        return False
    
    if int(telefono) != 9 or not telefono.isdigit(): # Verificamos que el telefono tenga nueve digitos y sea numerico
        return False
    
    return True

print("")
# Pedimos al usuario informacion
print("")
nombre = input("Ingrese su nombre: ")
email = input("Ingrese su email: ")
telefono = int(input("Ingrese su telefono: "))

print("")
valido = validar_formulario(nombre, email, telefono)
if valido:
    print("Formulario valido")
else:
    print("Formulario no valido")
print("")

# Validamos la informacion formulario

## Si la validacion retorna True  mostramos mensaje de exito
## Si la validacion retorna False mostramos mensaje de error




