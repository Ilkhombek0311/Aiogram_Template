from aiogram.types import Message
from aiogram.filters import CommandStart

from loader import dp
from utils.misc.parse_mode_html import html_decoder


@dp.message(CommandStart())
async def bot_start(message: Message) -> None:
    full_name = await html_decoder(message.from_user.full_name)
    await message.answer(f"Salom, {full_name}!")
