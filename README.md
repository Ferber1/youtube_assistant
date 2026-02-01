# Youtube Assistant
- Это Telegram-бот для помощи в дистанционном управлении видео на YouTube.

## Фичи:
<img width="265" height="349" alt="image" src="https://github.com/user-attachments/assets/f6ba5dc8-91af-4175-8b40-d4e2ccc8661b" />

## Стэк
- **Python 3.13**
- **Aiogram 3.x**
- **PyAutoGui**
- **Pydantic-settings**

## Установка
Linux/Mac (for Windows use Git Bash)
```
git clone https://github.com/Ferber1/youtube_assistant/tree/master
cd youtube_assistant
python3 -m venv venv  # requires Python 3.13
. venv/scripts/activate
pip install -r requirements.txt
cp .env.example .env
nano .env  # <-- Вставляем нужные переменные

# ВАЖНО! Перед включением включить ENG раскладку.
python main.py
```

## Как получить значения для .env
- `BOT_TOKEN`: В Telegram создаём своего бота через @BotFather. Получаем API-ключ ✅
- `OWNER_ID`: В Telegram пишем боту @userinfobot или похожему. Получаем ID ✅

## Использование
- По команде `/start` бот отзывается и выводит главное меню.

## Автор
- [Никита Сидоренко](https://vk.com/salmatov7), 2026
