# El objetivo es crear un programa con el que puedas calcular tus ahorros anuales. El programa deberá calcular: 
# 1- Cuánto puede ahorrar una persona dado su ingreso por horas.
# 2- Horas trabajadas y gasto de vida semanal

# 1- Pedir nuestro nombre y después imprima un saludo por pantalla de tipo: ‘Hola <Nombre>
nombre = input("Cual es su nombre: ")
print("Hola!",nombre)

# 2- Guarda el dinero ganado por hora y las horas trabajadas en la semana en dos variables diferentes
dinero_x_hora = float(input("Indique la cantidad de dinero que gana al trabajar durante 1 hora: "))
horas_semana  = float(input("¿Cuantas horas trabajaste durante la semana?: "))
semana        = float(input("Indique cuantas semanas labora al año?: "))

# 3- Multiplica ambas variables para obtener el salario semanal
Salario_Semana = float(dinero_x_hora * horas_semana)
ganancia_anual = float(Salario_Semana * semana)

# 4- Ahora imprime por pantalla un mensaje del tipo: ‘<Nombre> tiene unas ganancias anuales de: <cantidad> euros
print("Victor, usted tiene un ingreso semanal de: ", Salario_Semana , "y un ingereso anual de: ", ganancia_anual ,"EUR")

# 5- Pide los gastos semanales por pantalla y guárdalos en una variable.
gastos_semana = float(input("Indica el gasto semanal por favor: "))
gasto_anual   = float(gastos_semana * semana)

# 6- Los ahorros anuales serán la resta entre lo ganado durante el año menos los gastos anuales
ahorros = float (ganancia_anual - gasto_anual)
print("Amigo victor haciendo el cálculo, usted tiene un ahorro de: ",ahorros, "EUR")

