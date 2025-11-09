
A = "Hello World!"
B = "Goodbye"
C = 15
D = 20
E = "Error detectado"
F = None

n = 20 
if n == 15:
    print( "Hello World!")
else:
    print("Goodbye")

# Operador lógico AND para comparar valores numéricos
try:
    resultado = (n < 20 and n <= 25)
    print(resultado)
    seleccion = A if resultado else B

    # Captura de excepciones específicas y asignación predeterminada
except (NameError, ZeroDivisionError, SyntaxError, TypeError, Exception) as e: 

    # Imprime el tipo de la excepción ocurrida
    print("Ocurrió un error:", type(e).__name__) 
    seleccion = A
else:
    if resultado is None: # Si no se ha producido ninguna excepción, establece 'seleccion' como verdadero
        seleccion = D

print("La selección correcta es:", A)
