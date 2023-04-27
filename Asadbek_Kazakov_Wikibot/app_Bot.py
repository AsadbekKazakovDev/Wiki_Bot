"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import wikipedia


from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang("uz")
API_TOKEN = '6151458205:AAECrsh-sTsXxyM3MqitIr5wd4nUvZ0X0_U'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Asadbek Kazakovning uzbekcha Wikipedia telegram botiga xush kelibsiz\nSiz izlamoqchi bulgan malumotingizni kiriting :")



@dp.message_handler()
async def search_wikipedia(message: types.Message):
    try:
        send = wikipedia.summary(message.text)
        await message.answer(send)
    except:
        await message.answer("Siz izlamoqchi bulgan malumot topilmadi, qaytadan urining!!!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
