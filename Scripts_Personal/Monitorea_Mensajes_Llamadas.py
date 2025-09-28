# [WEBHOOKS-MOCK] Simulación de sistema de notificaciones
_callbacks = {}

def send(title, message, recipient):
    print(f"[WEBHOOK] {title} → {message} → {recipient}")

def add_callback(event, func):
    _callbacks[event] = func

def trigger(event, data):
    if event in _callbacks:
        _callbacks[event](data)

# [NOTIFY] Función de envío de notificación
def send_notification(message):
    send("Notificación", message, "Hola Viktore")

# [WEBHOOKS-REGISTER] Registrar callback para mensajes
add_callback("message", lambda data: send_notification(data))

# [TELEGRAF-MOCK] Simulación de envío de métrica tipo llamada
def send_call_metric(call_id, port, phone, caller, message):
    print(f"[CALL-METRIC] ID:{call_id} | Port:{port} | Caller:{caller} | Phone:{phone} | Msg:{message}")

# Enviar evento de llamada
send_call_metric("call1", 9524, "+51939182565", "Victor", "Has received a call from Linux_Ubuntu")

# [CALL-MONITOR] Simulación de monitoreo en background
import threading
import time

def monitor_call():
    while True:
        print("[CALL-MONITOR] Verificando llamadas...")
        time.sleep(5)

# Ejecutar en background
threading.Thread(target=monitor_call, daemon=True).start()

# Simular recepción de mensaje
trigger("message", "Has received a message from XYZ")
