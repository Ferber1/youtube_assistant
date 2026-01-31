from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from service import youtube_manager
from utils.states import SearchState  # noqa


router = Router()


@router.callback_query(lambda call: call.data == "yt_search_videos")
async def _yt_search_videos(call: CallbackQuery, state: FSMContext):
    await state.set_state(SearchState.search)

    return await call.answer("🔎 Введите запрос", show_alert=True)


@router.message(SearchState.search)
async def _search(message: Message, state: FSMContext):
    text = message.text

    url = await youtube_manager.search_videos(text)

    await state.clear()

    return await message.answer(
        f"✅ Открыто: [{text}]({url})", parse_mode="Markdown"
    )
