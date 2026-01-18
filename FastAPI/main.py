from fastapi import FastAPI # Importamos la clase FastAPI del modulo FastAPI

app = FastAPI() # Instanciamos la aplicacion FastAPI

@app.get("/") # Esto es el llamado o conexion a la Raiz, el LocalHost: http://127.0.0.1:8000 

async def root(): # Operacion de llamado Asicrono al endpoint raiz o servicio principal del servidor
    return {"Hello": "FastAPI"} # Retornamos un diccionario con el mensaje "Hello": "FastAPI"

# Comando para ejecutar el servidor con recarga automática: (uvicorn main:app --reload)

# uvicorn main2:app2 --reload : Ejemplo de Error.

''' 
Engtrada Bash: Consola VSCode: uvicorn FastAPI.main:app --reload

Salida Bash: Resultado Positivo del despliegue, Actualmente LocalHost: http://127.0.0.1:8000 

(.ConquerBlocks) viktore@ConquerBlocks:~/Documentos/2-Python/FastAPI$ uvicorn FastAPI.main:app --reload
INFO:     Will watch for changes in these directories: ['/home/viktore/Documentos/2-Python/FastAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [823473] using StatReload
INFO:     Started server process [823501]
INFO:     Waiting for application startup.
INFO:     Application startup complete.'''