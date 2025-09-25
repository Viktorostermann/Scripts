import webhooks
import opentelemetry
import pywhatkit

def send_notification(message):
    webhooks.send("Notificación", "Has received a message", "amine@tu号码")  # ejemplar

# Monitorear mensajes
webhooks.add_callback("message", lambda data: send_notification(data))

from opentelemetry import call

call.start("call1", 9524, "+1234567890", "Pablo", "Has received a call from XYZ")

def monitor_call():
    while True:
        # Verificar si hay una nueva llamada
        pass

# Ejecutar en background
call_task = lambda: monitor_call()
call.start("Call monitor", "", "", "", False, True)  # Indica si debe detenerse
call.join(call_task)