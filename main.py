from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('5990386981:AAG4tmYahizbWKDrd0Z4vgdPNsIjIaWo-9Q')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб странницу', web_app=WebAppInfo(url='https://music.yandex.ru/home?=')))
    await message.answer('Привет', reply_markup=markup)


executor.start_polling(dp)
