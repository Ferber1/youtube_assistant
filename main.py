import asyncio
from aiogram import Bot, Dispatcher

from config import settings
from handlers import register_handlers


async def main():
    bot = Bot(settings.bot_token)
    dp = Dispatcher()

    register_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopped")
