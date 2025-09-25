'''Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
o sí mismo.'''

# Solucion B:
# --- Bucle que recorre los numeros del 2 al 100
for x in range(2, 101):
        primo = True
        i = 2
        while primo == True and i < x:
            if x % i == 0:
                primo = False
            i += 1
            break
        if primo:
            print(x)