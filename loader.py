from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from data.config import BOT_TOKEN

dp = Dispatcher()
bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
