empleados = {}
print(type(empleados), "--->",empleados )

continuar = True
while  continuar:
    print("1. Agregar empleado")
    print("2. Actualizar salario de empleados")
    print("3. Mostrar lista de empleados")
    print("4. Calcular promedio salaraial por departamento")
    print("5. Salir")
    opcion = input("Ingrese una opcion: ")
    print("\n")

# Agregar Opcion Empleado
    if opcion == "1":

        nombre = input("Ingrese el nombre del empleado: ")
        departamento = input("Ingrese el departamento del empleado: ")
        salario = float(input("Ingrese el salario del empleado: "))

        empleados[nombre] = {
            "departamento": departamento,
            "salario": salario
        }
        
        print("Empleado agregado con exito")

    # Actualizar salario de empleados
    elif opcion == "2":
        print("Actualizar salario de empleados")
        nombre = input("Ingrese el nombre del empleado: ")
        #Comprobamos si el id_empleado o nombre del empleado existe en el diccionario
        if nombre in empleados:
            print("Empleado encontrado")
            # Pedimos el nuevo salario
            nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))
            # Actualizamos el salario en el diccionario
            empleados[nombre]["salario"] = nuevo_salario
            print("Salario actualizado con exito")
        # Si el id_empleado no existe en el diccionario o base de datos
        else: 
            print("El empleado no existe en Base de datos")
            print("\n")

    # Mostrar lista de empleados
    elif opcion == "3":
        print("Mostrar lista de empleados")
        # recorremos el diccionario empleados pares clave-valor => (id_empleado, datos)
        for nombre, datos in empleados.items():
            salario = datos["salario"] # Extraemos el salario
            departamento = datos["departamento"] # Extraemos el departamento
            # Imprimimos los datos del empleado
            print(f"Nombre: {nombre}, Salario: {salario}, Departamento: {departamento}")
            print("\n")

    # Calcular promedio salaraial por departamento
    elif opcion == "4":
        departamento = input("Ingrese el departamento: ")
        
        # Inicializamos variables
        departamento =  departamento.lower()
        total_salarios = 0
        contador = 0

        # Recorremos el diccionario empleados pares clave-valor => (id_empleado, datos)
        for id_empleado in empleados.values():
            # Comprobamos si el departamento coincide con el ingresado
            if id_empleado["departamento"] == departamento.lower():
                total_salarios = total_salarios + id_empleado["salario"]
                contador = contador + 1
        
        # Si hay empleados en el departamento
        if contador > 0:
            promedio_salarios = total_salarios / contador
            print(f"El promedio salarial del departamento {departamento} es: {promedio_salarios}")
            print("\n")
        #
        else:
            print(f"No hay empleados en el departamento {departamento}")
            print("\n")
               
    # Salir
    elif opcion == "5":
        print("Salir")
        print("\n")
        continuar = False
    else:
        print("Opcion invalida. Por favor, elija una opcion valida.")