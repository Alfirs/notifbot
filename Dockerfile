# Используем официальный образ Python в качестве базового
FROM python:3.9-slim-buster

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем необходимые пакеты
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем переменные окружения (если необходимо)
# ENV BOT_TOKEN=YOUR_BOT_TOKEN
# ENV ADMIN_CHAT_ID=YOUR_ADMIN_CHAT_ID

# Открываем порт 8080 для внешнего доступа (если используете вебхуки)
EXPOSE 8080

# Запускаем main.py при запуске контейнера
CMD ["python", "main.py"]
