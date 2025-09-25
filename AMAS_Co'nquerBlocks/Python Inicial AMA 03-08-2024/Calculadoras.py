'''
En esta clase, realizamos una calculadora que incluye operaciones básicas, avanzadas y lógicas. 
Además, repasamos funciones y condicionales para mejorar nuestra comprensión de estos conceptos.
'''

#Calculadora en Python

#Funciones de operaciones basicas
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "No se puede dividir entre cero"
    
# Operaciones alternas
def potencia(num1, num2):
    return num1 ** num2

def raiz_cuadrada(num):
    if num != 0:
        return num ** 0.5
    else:
        return "No se puede calcular la raíz cuadrada de un número negativo"

# Operaciones lógicas (AND, OR, NOT, XORT, NAND, NOR)

# AND => (1 y 1) = 1 / (1 y 0) = 0 / (0 y 0) = 0
def and_logico(num1, num2):
    return int (bool(num1)) and int (bool(num2)) # Ambos deben ser verdaderos

# OR => (1 o 1) = 1 / (1 o 0) = 1 / (0 o 0) = 0
def or_logico(num1, num2):
    return int (bool(num1)) or int (bool(num2)) # Al menos uno debe ser verdadero

# NOT => (1 = 0) / (0 = 1)
def not_logico(num):
    return not bool(num) # Cambia el valor de verdad

# NAND => (1 y 1) = 0 / (1 y 0) = 1 / (0 y 0) = 1 / (0 y 1) = 1
def nand_logico(num1, num2):
    return not (bool(num1) and bool(num2)) # Ambos deben ser falsos

# NOR => (1 o 1) = 0 / (1 o 0) = 1 / (0 o 0) = 0 / (0 o 1) = 0
def nor_logico(num1, num2):
    return not (bool(num1) or bool(num2)) # Al menos uno debe ser falso

# XOR => (1 y 1) = 0
def xor_logico(num1, num2):
    return (bool(num1) and not bool(num2)) or (not bool(num1) and bool(num2)) # Solo puede ser verdadero uno de los dos

def mostrar_menu():
    print("\n")
    print("Bienvenido a las calculadoras de AMA")
    print("")
    print("Seleccione una operación:")
    print("\n")

    print("1. Suma")
    print("")
    print("2. Resta")
    print("")
    print("3. Multiplicación")
    print("")
    print("4. División")
    print("")
    print("5. Potencia")
    print("")
    print("6. Raíz cuadrada")
    print("")
    print("7. AND")
    print("")
    print("8. OR")
    print("")
    print("9. NOT")
    print("")
    print("10. NAND")
    print("")
    print("11. NOR")
    print("")
    print("12. XOR")
    print("\n")
    print("Marque 0 para Salir")
    print("\n")

def obtener_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1, num2

def calculadora():
  while True:
    mostrar_menu()
    operacion = input("Ingrese el número de la operación que desea realizar: ")

    if operacion in ["1", "2", "3", "4", "5", "7", "8", "9", "10", "11", "12", "13"]:
        num1, num2 = obtener_numeros()
        if operacion == "1":
            resultado = suma(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        
        elif operacion == "2":
            resultado = resta(num1, num2)
            print(f"El resultado de la resta es: {resultado}")
        
        elif operacion == "3":
            resultado = multiplicacion(num1, num2)
            print(f"El resultado de multiplicación es: {resultado}")
        
        elif operacion == "4":
            resultado = division(num1, num2)
            print(f"El resultado de la division es: {resultado}")
        
        elif operacion == "5":
            resultado = potencia(num1, num2)
            print(f"El resultado de la potencia es: {resultado}")
        
        elif operacion == "7":
            resultado = and_logico(num1, num2)
            print(f"El resultado de la operación OR es: {resultado}")   
        
        elif operacion == "8":
            resultado = or_logico(num1, num2)
            print(f"El resultado de la operación NOT es: {resultado}")
        
        elif operacion == "10":
            resultado = nand_logico(num1, num2)
            print(f"El resultado de la operación NAND es: {resultado}")
        
        elif operacion == "11":
            resultado = nor_logico(num1, num2)
            print(f"El resultado de la operación NOR es: {resultado}")
        
        elif operacion == "12":
            resultado = xor_logico(num1, num2)
            print(f"El resultado de la operación XOR es: {resultado}")
        
    elif operacion == "6":
            num = int(input("Ingrese el número para calcular la raíz cuadrada: "))
            resultado = raiz_cuadrada(num)
            print(f"El resultado de la raiz cuadrada es: {resultado}")

    elif operacion == "9":
            resultado = not_logico(num)
            print(f"El resultado de la operación NOT es: {resultado}")
        
    elif operacion == "0":
        print("¡Hasta luego!")
        break
        
    else:
        print("Operación no disponible. Por favor, seleccione una operación válida.")


calculadora()