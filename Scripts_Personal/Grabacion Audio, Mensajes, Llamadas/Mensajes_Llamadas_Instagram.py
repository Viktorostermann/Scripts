'''Requisitos:

Instala las dependencias:
1- Bash: pip install telethon twilio
2- Obtén las credenciales de: Telegram: API ID y API Hash desde Telegram MyApps.
3- Twilio: Account SID, Auth Token y un número de Twilio desde Twilio.'''

'''¿Cómo usarlo?
1- Envía mensajes: await send_telegram_message("@usuario", "Hola desde el bot!")
2- Realiza llamadas: make_call("+51999999999")
3- Recibe mensajes en tiempo real: Se imprimen en consola automáticamente.'''


from telethon import TelegramClient, events
from twilio.rest import Client

# Credenciales de Telegram
API_ID = "TU_API_ID"
API_HASH = "TU_API_HASH"
PHONE_NUMBER = "TU_NUMERO_TELEGRAM"

# Credenciales de Twilio
TWILIO_SID = "TU_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "TU_AUTH_TOKEN"
TWILIO_NUMBER = "TU_NUMERO_TWILIO"

# Inicializar clientes
telegram_client = TelegramClient("session_name", API_ID, API_HASH)
twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Función para enviar mensaje por Telegram
async def send_telegram_message(user, message):
    await telegram_client.send_message(user, message)
    print(f"Mensaje enviado a {user}: {message}")

# Función para hacer una llamada con Twilio
def make_call(to_number):
    call = twilio_client.calls.create(
        twiml="<Response><Say>Hola, esto es una llamada automática.</Say></Response>",
        from_=TWILIO_NUMBER,
        to=to_number
    )
    print(f"Llamada realizada a {to_number}: {call.sid}")

# Escuchar mensajes entrantes
@telegram_client.on(events.NewMessage)
async def handle_message(event):
    print(f"Mensaje recibido de {event.chat_id}: {event.text}")

# Ejecutar cliente de Telegram
with telegram_client:
    telegram_client.run_until_disconnected()
