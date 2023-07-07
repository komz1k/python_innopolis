from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer("Напиши мне что-то и я повторю")


@dp.message_handler()
async def repeat_handler(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True)
