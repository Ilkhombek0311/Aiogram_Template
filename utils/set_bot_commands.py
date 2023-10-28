from aiogram.types import BotCommand, BotCommandScopeDefault
from loader import bot


async def set_default_commands():
    commands = [
        BotCommand(command="start", description="Bo'tni ishga tushirish."),
        BotCommand(command="help", description="Yordam!")
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


