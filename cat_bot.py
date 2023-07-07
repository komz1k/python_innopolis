from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

import requests


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer("Напиши мне /cat и я пришлю тебе котика)")


@dp.message_handler(commands=["cat"])
async def send_cat(message: types.Message):
    url1 = ' https://api.thecatapi.com/v1/images/search'
    response = requests.get(url1).json()
    a = []
    for i in range(1):
        a.append(response[i]["url"])
    pic = a[0]
    await bot.send_photo(message.chat.id, pic)
    a.pop(0)


executor.start_polling(dp, skip_updates=True)




