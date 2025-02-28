# handlers.py
from telegram import Update # Импортируем класс Update, представляющий обновление от Telegram
from telegram.ext import ContextTypes # Импортируем класс ContextTypes для работы с контекстом обработчика
from config import ADMIN_CHAT_ID # Импортируем ID чата администратора из файла config.py

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик новых заявок на вступление в чат.
    Отправляет уведомление администратору."""
    chat_join_request = update.chat_join_request # Получаем объект запроса на вступление в чат
    user = chat_join_request.from_user # Получаем информацию о пользователе, подавшем заявку

    # Формируем сообщение с информацией о пользователе
    message = (
        f"Новая заявка на вступление от:\n" # Начало сообщения
        f"User ID: {user.id}\n" # ID пользователя
        f"Username: @{user.username}\n" # Имя пользователя (если есть)
        f"First Name: {user.first_name}\n" # Имя пользователя
        f"Last Name: {user.last_name if user.last_name else ''}"  # Фамилия пользователя (если указана)
    )

    try:
        # Отправляем сообщение администратору
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=message)
    except Exception as e:
        # Обрабатываем исключения (например, если бот заблокирован админом)
        print(f"Ошибка при отправке сообщения администратору: {e}")
        # Опционально: отправляем сообщение об ошибке в чат для логов (раскомментируйте и настройте, если нужно)
        # await context.bot.send_message(chat_id=YOUR_LOG_CHAT_ID, text=f"Ошибка: {e}")  #Раскомментируйте и настройте, если нужно

    # Опционально: автоматическое одобрение или отклонение заявки (будьте осторожны!)
    # await chat_join_request.approve() # Автоматически одобряем заявку
    # await chat_join_request.decline() # Автоматически отклоняем заявку
    print(f"Заявка на вступление обработана для пользователя: {user.id}") # Логируем обработку заявки


# Здесь можно добавить другие обработчики для других функций бота
