import asyncio
import logging
import sys

from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup() -> None:
    # Adminga xabar yuborish
    await on_startup_notify()

    # Default commandalar
    await set_default_commands()

    try:
        # And the run events dispatching
        await dp.start_polling(bot)
    finally:
        await bot.session.close(on_startup_notify())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(on_startup())
