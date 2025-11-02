''' Archivo ejemplo de archivo mensaje de excepciones o errores '''

def dividir(a, b): # Función para dividir dos números con manejo de excepciones
    try:
        print (5/0)
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
    finally:
        print('Operación de división finalizada.')


    '''try:
        resultado = a / b
        print("División realizada con éxito.")
        return resultado
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except TypeError:
        print("Los operandos deben ser numéricos.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        print("Operación de división finalizada.")


# Ejemplos de uso
print(dividir(10, 2))  # División correcta
print(dividir(10, 0))  # División por cero
print(dividir(10, 'a'))  # Tipo incorrecto'''