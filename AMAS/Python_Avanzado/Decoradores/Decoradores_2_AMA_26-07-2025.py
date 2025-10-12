'''
Implementamos un decorador llamado reintentar_3_veces, que permite 
*reintentar automáticamente la ejecución de una función hasta tres veces* 
en caso de error, con pausas de un segundo entre intentos. Además, 
desarrollamos otro decorador llamado validar_datos que *verifica los tipos de datos* 
de los argumentos antes de ejecutar una función, lanzando errores si no se cumplen los requisitos. 
'''

# Decorador de reintentos automaticos
import time
import random


def reintentar_3_veces (func):
    # Warpper que reintenta ejecutar una funcion hasta 3 veces
    # Eeperar 1 segundo entre intentos

    def wrapper(*args,**kwargs):
        intentos = 3
        for i in range(intentos):
            try:
                return func (*args,**kwargs)
            except Exception as e:
                if i == intentos -1: # Ultimo intento - 1 significa que estamos en el ultimo intento
                    raise e # Si es el ultimo intento, lanza el error execepcion
                print (f" Intento {i+1} fallido, reintentando...")
                time.sleep(1)
    return wrapper

@reintentar_3_veces
def conectar_servidor():
    # Simula la conexion a un servidor que puede fallar
    valor_randomico = random.random()
    print("")
    print(valor_randomico)
    print("")
    if valor_randomico < 0.5:
        raise ConnectionError("No se pudo conectar al servidor")
    return "Conexion exitosa"
    
try:
    print(conectar_servidor())
    print("")
except Exception as e:
    print(f"Error al conectar al servidor: {e}")
    print("")
