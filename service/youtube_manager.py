from asyncio import sleep
from random import choice
import webbrowser
from pyautogui import click, press, hotkey

from utils.constants import YOUTUBE_SEARCH_URL, YOUTUBE_URL


MAIN_PAGE_VIDEO_COORDS = [
    (1043, 300),
    (1572, 300),
    (501, 300),
]
SEARCH_PAGE_VIDEO_COORDS = [(661, 279)]

YOUTUBE_LOAD_COOLDOWN = 4


class YoutubeManager:
    def press_key(self, key: str) -> None:
        return press(key)

    def _calculate_tens_and_fives(self, seconds: int) -> tuple[int, int]:
        tens = seconds // 10
        fives = (seconds - tens * 10) // 5
        return tens, fives

    def pause(self) -> None:
        """Ставит текущее видео на паузу (Space)"""
        return press("space")

    def remain_time(self) -> None:
        """
        Возвращает оставшееся время
        воспроизведения видео (количество секунд)
        """

    def rewind(self, seconds: int) -> None:
        """Отмотка воспроизведения видео (количество секунд)"""
        tens, fives = self._calculate_tens_and_fives(seconds)

        press("j", presses=tens, interval=0.2)
        press("left", presses=fives, interval=0.2)

    def forward(self, seconds: int) -> None:
        """Перемотка воспроизведения видео (количество секунд)"""
        tens, fives = self._calculate_tens_and_fives(seconds)

        press("l", presses=tens, interval=0.2)
        press("right", presses=fives, interval=0.2)

    def next_video(self) -> None:
        """Переключение видео на предыдущее"""
        hotkey("shift", "n")

    def previous_video(self) -> None:
        """Переключение видео на следующее"""
        hotkey("alt", "left")

    def change_size(self) -> None:
        """Изменение размера плеера (полноэкранный/обычный)"""
        press("f")

    def open_main_page(self) -> None:
        """Открывает главную страницу YouTube."""
        webbrowser.open(YOUTUBE_URL)

    def close_video(self) -> None:
        """Закрывает видеоплеер (вкладку)."""
        hotkey("ctrl", "w")

    async def random_video(self):
        """Открывает рандомное видео."""
        webbrowser.open(YOUTUBE_URL)
        await sleep(YOUTUBE_LOAD_COOLDOWN)

        x, y = choice(MAIN_PAGE_VIDEO_COORDS)
        click(x, y)

    async def search_videos(self, query: str) -> str:
        url = YOUTUBE_SEARCH_URL.format(query)

        webbrowser.open(url)
        await sleep(YOUTUBE_LOAD_COOLDOWN)

        x, y = choice(SEARCH_PAGE_VIDEO_COORDS)
        click(x, y)

        return url


youtube_manager = YoutubeManager()
