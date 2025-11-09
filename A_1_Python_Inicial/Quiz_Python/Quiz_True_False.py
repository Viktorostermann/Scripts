A = True
B = False
C = "Error detectado"
D = None

x = 4

# Operador lógico AND para comparar valores numéricos
try:
    resultado = (x > 3 and x < 10)
    print(resultado)
    seleccion = A if resultado else B

    # Captura de excepciones específicas y asignación predeterminada
except (NameError, ZeroDivisionError, SyntaxError, TypeError, Exception) as e: 

    # Imprime el tipo de la excepción ocurrida
    print("Ocurrió un error:", type(e).__name__) 
    seleccion = C
else:
    if resultado is None: # Si no se ha producido ninguna excepción, establece 'seleccion' como verdadero
        seleccion = D

print("Selección correcta:", seleccion)
