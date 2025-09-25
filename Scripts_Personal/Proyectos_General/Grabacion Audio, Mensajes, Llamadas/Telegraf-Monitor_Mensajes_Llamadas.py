import webhooks
from telegraf import call

def send_notification(message):
    webhooks.send("Notificación", "Has received a message", "viktoremiletic@gmail.com")  # ejemplar

# Monitorear mensajes
webhooks.add_callback("message", lambda data: send_notification(data))

from telegraf import call

call.start("call1", 9524, "+1234567890", "Pablo", "Has received a call from XYZ")

def monitor_call():
    while True:
        # Verificar si hay una nueva llamada
        pass

# Ejecutar en background
call_task = lambda: monitor_call()
call.start("Call monitor", "", "", "", False, True)  # Indica si debe detenerse
call.join(call_task)


'''from twilio.rest import Client

# Credenciales de Twilio
TWILIO_SID = "TU_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "TU_AUTH_TOKEN"
TWILIO_NUMBER = "TU_NUMERO_TWILIO"

# Inicializar cliente Twilio
twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Función para enviar notificación por SMS
def send_notification(message, phone_number):
    twilio_client.messages.create(
        body=message,
        from_=TWILIO_NUMBER,
        to=phone_number
    )
    print(f"Notificación enviada a {phone_number}: {message}")

# Función para realizar una llamada con Twilio
def make_call(phone_number):
    call = twilio_client.calls.create(
        twiml="<Response><Say>Hola, tienes una llamada automática.</Say></Response>",
        from_=TWILIO_NUMBER,
        to=phone_number
    )
    print(f"Llamada realizada a {phone_number}. ID: {call.sid}")

# Simular recepción de mensaje y llamada
send_notification("Has recibido un mensaje", "+1234567890")
make_call("+1234567890")
'''