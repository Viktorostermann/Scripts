'''Cómo funciona
✅ Manejo de mensajes con Aiogram 
✅ Realización de llamadas con Twilio 
✅ Fácil de integrar y configurar

Este bot permite que un usuario envíe el comando /call +51999999999 en Telegram, 
y automáticamente se realizará la llamada con Twilio.'''

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from twilio.rest import Client

# Token de Telegram y credenciales de Twilio
TELEGRAM_TOKEN = "TU_BOT_TOKEN"
TWILIO_SID = "TU_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "TU_AUTH_TOKEN"
TWILIO_NUMBER = "TU_NUMERO_TWILIO"

# Inicializar bot y dispatcher
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Cliente Twilio para llamadas
twilio_client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Manejar mensajes de /call para hacer una llamada
@dp.message_handler(commands=['call'])
async def make_call(message: types.Message):
    phone_number = message.text.split()[-1]  # Extraer número de teléfono
    call = twilio_client.calls.create(
        twiml="<Response><Say>Hola, esto es una llamada automática desde Telegram Bot.</Say></Response>",
        from_=TWILIO_NUMBER,
        to=phone_number
    )
    await message.reply(f"Llamada realizada a {phone_number}. ID: {call.sid}")

# Iniciar bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
