# RAP_v2.py - Registro, Análisis y Presentación de puntajes (versión secuencial)

''' REGISTRO DE PUNTAJES:
 
Implementa un programa en Python que permita registrar y mantener un 
seguimiento de los puntajes de un juego. El programa debe permitir a los 
jugadores ingresar sus nombres y puntajes, almacenarlos en un 
diccionario y proporcionar funcionalidades para mostrar el puntaje más 
alto, el promedio de puntajes y la cantidad total de jugadores.''' 

puntajes = {}

def registrar_puntaje():
    nombre = input("Nombre del jugador: ")
    try:
        puntaje = int(input("Puntaje: "))
        puntajes[nombre] = puntaje
        print(f"✅ Puntaje registrado para {nombre}: {puntaje} puntos")
    except ValueError:
        print("⚠️ Puntaje inválido. Debe ser un número entero.")

def mostrar_puntaje_mas_alto():
    if puntajes:
        jugador = max(puntajes, key=puntajes.get)
        print(f"🏆 Puntaje más alto: {jugador} con {puntajes[jugador]} puntos")
    else:
        print("📭 No hay puntajes registrados.")

def calcular_promedio():
    if puntajes:
        promedio = sum(puntajes.values()) / len(puntajes)
        print(f"📊 Promedio de puntajes: {promedio:.2f}")
    else:
        print("📭 No hay puntajes registrados.")

def mostrar_total_jugadores():
    print(f"👥 Total de jugadores: {len(puntajes)}")

def mostrar_menu():
    print("\n--- Menú RAP ---")
    print("1. Registrar puntaje")
    print("2. Mostrar puntaje más alto")
    print("3. Calcular promedio de puntajes")
    print("4. Mostrar total de jugadores")
    print("5. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        registrar_puntaje()
    elif opcion == "2":
        mostrar_puntaje_mas_alto()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        mostrar_total_jugadores()
    elif opcion == "5":
        print("👋 Saliendo del programa.")
        return False
    else:
        print("❌ Opción no válida. Intenta de nuevo.")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        continuar = ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()

