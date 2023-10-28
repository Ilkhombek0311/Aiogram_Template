from aiogram.types import Message
from aiogram.filters import Command

from loader import dp


@dp.message(Command(commands="help"))
async def bot_help(message: Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
