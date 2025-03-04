# Используем последний образ genotek base
FROM genotek/r-base:20210121

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения и файлы
COPY . .

# Создаем shell-скрипт
#RUN echo '#!/bin/sh' > /script.sh
#RUN echo 'date' >> /script.sh
#RUN chmod +x /script.sh

# Открываем порт 5005
EXPOSE 5005

# Запускаем приложение
CMD ["python3", "app.py"]

# Запускаем приложение
CMD ["python3", "app.py"]