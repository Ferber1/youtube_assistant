from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message

from config import settings
from service import youtube_manager
from utils.keyboards import START_KEYBOARD


router = Router()


@router.message(CommandStart(ignore_case=True))
async def _start(message: Message):
    return await message.answer(
        f"[{settings.version_repr}] "
        f"<b>Youtube Assistant</b> for you,\n{message.from_user.first_name}",
        parse_mode="HTML",
        reply_markup=START_KEYBOARD,
    )


@router.message()
async def _press_key(message: Message):
    youtube_manager.press_key(message.text)
    return await message.answer(f"✅ {message.text}")
