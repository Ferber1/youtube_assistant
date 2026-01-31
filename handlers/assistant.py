import webbrowser
from aiogram import Router
from aiogram.types import CallbackQuery

from service import youtube_manager


def parse_seconds_from_call_data(call_data: str) -> int:
    """Парсинг: yt_rewind_10 --> 10"""
    return int(call_data.split("_")[-1])


router = Router()


@router.callback_query(lambda call: call.data == "yt_pause")
async def _pause(call: CallbackQuery):
    youtube_manager.pause()

    await call.answer("✅ Пауза")


@router.callback_query(lambda call: call.data == "yt_change_size")
async def _change_size(call: CallbackQuery):
    youtube_manager.change_size()

    await call.answer("✅ Полноэкранный режим")


@router.callback_query(lambda call: call.data == "yt_remain_time")
async def _remain_time(call: CallbackQuery):
    youtube_manager.remain_time()

    await call.answer("❌ Сколько длится")


@router.callback_query(lambda call: call.data.startswith("yt_rewind"))
async def _yt_rewind(call: CallbackQuery):
    seconds = parse_seconds_from_call_data(call.data)
    youtube_manager.rewind(seconds)

    await call.answer(f"✅ -{seconds} секунд")


@router.callback_query(lambda call: call.data.startswith("yt_forward"))
async def _yt_forward(call: CallbackQuery):
    seconds = parse_seconds_from_call_data(call.data)
    youtube_manager.forward(seconds)

    await call.answer(f"✅ +{seconds} секунд")


@router.callback_query(lambda call: call.data == "yt_next")
async def _yt_next(call: CallbackQuery):
    youtube_manager.next_video()

    await call.answer("✅ Вперёд")


@router.callback_query(lambda call: call.data == "yt_previous")
async def _yt_previous(call: CallbackQuery):
    youtube_manager.previous_video()

    await call.answer("✅ Назад")


@router.callback_query(lambda call: call.data == "yt_random_video")
async def _yt_random_video(call: CallbackQuery):
    await youtube_manager.random_video()

    await call.answer("✅ Рандомное видео")


@router.callback_query(lambda call: call.data == "yt_open_main")
async def _yt_open_main(call: CallbackQuery):
    youtube_manager.open_main_page()

    await call.answer("✅ YouTube")


@router.callback_query(lambda call: call.data == "yt_close_video")
async def _yt_close_video(call: CallbackQuery):
    youtube_manager.close_video()

    await call.answer("✅ Закрыть вкладку")
