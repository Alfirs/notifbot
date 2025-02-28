# main.py
import asyncio # Импортируем asyncio для асинхронного программирования
import logging # Импортируем logging для ведения логов

from telegram.ext import Application, ChatJoinRequestHandler, CommandHandler # Импортируем необходимые классы из telegram.ext
from telegram import Update # !!! ДОБАВЬТЕ ЭТУ СТРОКУ !!! Импортируем класс Update из telegram

from handlers import handle_join_request # Импортируем функцию обработки заявок из handlers.py
from config import BOT_TOKEN # Импортируем токен бота из config.py

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO # Формат и уровень логирования
)
# Задаем более высокий уровень логирования для httpx, чтобы избежать логирования каждого GET и POST запроса
logging.getLogger("httpx").setLevel(logging.WARNING)

async def start(update, context):
    """Отправляет приветственное сообщение при команде /start"""
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Я бот, который уведомляет админа о заявках на вступление.")

def main() -> None:
    """Запускает бота."""
    # Создаем приложение и передаем токен бота
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Добавляем обработчик события запроса на вступление в чат
    application.add_handler(ChatJoinRequestHandler(handle_join_request))

    # Запускаем бота в режиме polling (периодический опрос Telegram API)
    application.run_polling(allowed_updates=Update.ALL_TYPES) # Разрешаем все типы обновлений


if __name__ == "__main__":
    main()
