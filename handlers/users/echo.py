from aiogram.types import Message

from loader import dp


# Echo bot
@dp.message()
async def bot_echo(message: Message):
    await message.answer(message.text)
