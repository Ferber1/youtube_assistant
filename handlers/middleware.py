from aiogram import BaseMiddleware
from aiogram.types import Message

from config import settings


class CheckUserMiddleware(BaseMiddleware):
    """Проверка на владельца бота."""
    async def __call__(self, handler, event: Message, data):
        if event.from_user.id != settings.owner_id:
            return

        return await handler(event, data)
