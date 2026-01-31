from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⏸️ Space", callback_data="yt_pause")],
        [
            InlineKeyboardButton(
                text="📦 Полноэкранный режим", callback_data="yt_change_size"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎲 Рандомное видео", callback_data="yt_random_video"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔎 Поиск", callback_data="yt_search_videos"
            ),
        ],
        [
            InlineKeyboardButton(text="⏪ -10", callback_data="yt_rewind_10"),
            InlineKeyboardButton(text="+10 ⏩", callback_data="yt_forward_10"),
        ],
        [
            InlineKeyboardButton(text="⏪ -30", callback_data="yt_rewind_30"),
            InlineKeyboardButton(text="+30 ⏩", callback_data="yt_forward_30"),
        ],
        [
            InlineKeyboardButton(text="⏮️ Назад", callback_data="yt_previous"),
            InlineKeyboardButton(text="Вперёд ⏩", callback_data="yt_next"),
        ],
        [
            InlineKeyboardButton(
                text="❤️ YouTube", callback_data="yt_open_main"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❌ Закрыть", callback_data="yt_close_video"
            ),
        ],
    ]
)
